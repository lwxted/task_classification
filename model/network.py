# -*- coding: utf-8 -*-

import numpy as np
import os
import tensorflow as tf

from model.util import Util
from model.model_config import ModelConfig

dir_path = os.path.dirname(os.path.realpath(__file__))

class Network(object):
  def __init__(self, data, tensorboard_dir):
    super(Network, self).__init__()

    self.tensorboard_dir = tensorboard_dir

    self.max_learning_rate = 0.00001
    self.min_learning_rate = 0.000002
    self.decay_speed = 10.0
    self.l2_regularizer_beta = 0.0150

    self.n_input_steps = ModelConfig.n_input_steps   # max input time steps
    self.n_hidden = ModelConfig.n_hidden
    self.n_classes = ModelConfig.n_classes
    self.n_embedding = ModelConfig.n_embedding

    self.data = data
    self.sess = tf.Session()
    self.__build_network()

  def __write_summary(self, name_values, count):
    summaries = self.sess.run([self.summary_objs[t] for t in name_values], {
      self.summary_scalars[t] : name_values[t] for t in name_values
    })
    for s in summaries:
      self.writer.add_summary(s, count)
    print(', '.join(('%s : %f' % (t, name_values[t])) for t in name_values))

  def __build_network(self):
    self.params = dict()

    # ================ Input ================

    # input shape: (batch_size, time_step_size, input_vec_size)
    self.x = tf.placeholder(tf.float32, [None, self.n_input_steps, self.n_embedding])

    # xt shape: (time_step_size, batch_size, input_vec_size)
    self.xt = tf.transpose(self.x, [1, 0, 2])

    # each row has input for each lstm cell (lstm_size=input_vec_size)
    self.xr = tf.reshape(self.xt, [-1, self.n_embedding])
    # xr shape: (time_step_size * batch_size, input_vec_size)

    self.x_split = tf.split(self.xr, self.n_input_steps, 0) # split them to time_step_size (28 arrays)
    # Each array shape: (batch_size, input_vec_size)

    self.y = tf.placeholder(tf.float32, [None, self.n_classes])

    # ================ Dynamic params ================
    self.prob_keep_fc1 = tf.placeholder(tf.float32)
    self.learning_rate = tf.placeholder(tf.float32)

    # ================ Params ================
    self.params['W_fc1'] = tf.Variable(tf.random_normal([self.n_hidden * 2, self.n_classes]))
    self.params['b_fc1'] = tf.Variable(tf.random_normal([self.n_classes]))

    # ================ Graph ================
    with tf.name_scope('network'):
      self.rnn_cell_fw = tf.nn.rnn_cell.MultiRNNCell([
        tf.nn.rnn_cell.BasicLSTMCell(self.n_hidden), tf.nn.rnn_cell.BasicLSTMCell(self.n_hidden)])
      self.rnn_cell_bw = tf.nn.rnn_cell.MultiRNNCell([
        tf.nn.rnn_cell.BasicLSTMCell(self.n_hidden), tf.nn.rnn_cell.BasicLSTMCell(self.n_hidden)])
      self.outputs, self.states_fw, self.states_bw = tf.nn.static_bidirectional_rnn(self.rnn_cell_fw, self.rnn_cell_bw, self.x_split, dtype=tf.float32)
      self.output_dropped = tf.nn.dropout(self.outputs[-1], self.prob_keep_fc1)
      self.y_pred = tf.matmul(self.output_dropped, self.params['W_fc1']) + self.params['b_fc1']
      self.y_pred_softmax = tf.nn.softmax(self.y_pred)

    with tf.name_scope('optimizer'):
      self.cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=self.y_pred, labels=self.y) +
        self.l2_regularizer_beta * tf.nn.l2_loss(self.params['W_fc1']))
      self.optimizer = tf.train.RMSPropOptimizer(learning_rate=self.learning_rate).minimize(self.cross_entropy)

      self.test_prediction = tf.equal(tf.argmax(self.y_pred, 1), tf.argmax(self.y, 1))
      self.test_accuracy = tf.reduce_mean(tf.cast(self.test_prediction, tf.float32))

    with tf.name_scope('summaries'):
      summaries = ['train_accuracy', 'train_cost', 'validate_accuracy', 'validate_cost', 'learning_rate']
      self.summary_scalars = dict()
      self.summary_objs = dict()
      for s in summaries:
        self.summary_scalars[s] = tf.placeholder('float32', None, name='scalar_' + s)
        self.summary_objs[s] = tf.summary.scalar(s, self.summary_scalars[s])

    # Save variables
    self.saver = tf.train.Saver()

    # Output summaries
    self.merged_summaries = tf.summary.merge_all()
    self.writer = tf.summary.FileWriter(self.tensorboard_dir, self.sess.graph)
    tf.global_variables_initializer().run(session=self.sess)

  def train(self):
    per_batch = 32
    epochs = 100
    eval_per_n_batches = int(self.data.num_train_data_entries() / per_batch)

    avg_cost, avg_accu = 0, 0
    lowest_val_avg_cost, non_improving_count = 10000.0, 0

    for i in range(epochs * eval_per_n_batches):
      lr = Util.decaying_learning_rate(
        self.min_learning_rate,
        self.max_learning_rate,
        (self.decay_speed * eval_per_n_batches), i)
      xfeed, yfeed = self.data.next_batch_train(per_batch)
      xfeed = np.reshape(xfeed, (xfeed.shape[0], self.n_input_steps, self.n_embedding))
      _, train_cost, train_accuracy = self.sess.run(
        [self.optimizer, self.cross_entropy, self.test_accuracy], feed_dict={
        self.x : xfeed,
        self.y : yfeed,
        self.prob_keep_fc1   : 0.5,
        self.learning_rate : lr
      })
      avg_cost += train_cost
      avg_accu += train_accuracy

      if i % eval_per_n_batches == eval_per_n_batches - 1:
        xfeed, yfeed = self.data.validate_data_all()
        xfeed = np.reshape(xfeed, (xfeed.shape[0], self.n_input_steps, self.n_embedding))
        va, val_avg_cost = self.sess.run([self.test_accuracy, self.cross_entropy], feed_dict={
          self.x: xfeed,
          self.y: yfeed,
          self.prob_keep_fc1   : 1.0
        })
        self.__write_summary({
          'train_accuracy' : avg_accu / eval_per_n_batches,
          'validate_accuracy' : va,
          'train_cost' : avg_cost / eval_per_n_batches,
          'validate_cost' : val_avg_cost,
          'learning_rate' : lr
        }, int(i / float(eval_per_n_batches)))
        if val_avg_cost < lowest_val_avg_cost:
          lowest_val_avg_cost = val_avg_cost
          non_improving_count = 0
          self.saver.save(self.sess, os.path.join(dir_path, '../model_checkpoint/lstm_early_stopping_without_conc'))
        else:
          non_improving_count += 1
          print('No improvement for past %d epochs' % non_improving_count)
          if non_improving_count == 5:
            break
        avg_cost = 0
        avg_accu = 0

  def load_model(self, path):
    self.saver.restore(self.sess, path)

  def run_dummy(self, sample, label):
    return self.sess.run(self.y_pred_softmax, feed_dict={
      self.x: [sample],
      self.y: [label],
      self.prob_keep_fc1   : 1.0
    })

  def test(self):
    test_data = self.data.test_data_all()
    print(self.sess.run(self.test_accuracy, feed_dict={
      self.x: test_data[0],
      self.y: test_data[1],
      self.prob_keep_fc1   : 1.0
    }))
