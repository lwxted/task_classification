#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

from model.model_config import ModelConfig
from scipy.misc import imresize

class Data(object):
  def __init__(self):
    super(Data, self).__init__()
    self.x = None
    self.y = None

    self.train_upto = 0
    self.validate_upto = 0
    self.test_upto = 0

    self.train_batch_count = 0

  def load_data_from_file(self, full_npy):
    full = np.load(full_npy)
    np.random.shuffle(full)

    self.x = full[..., :-1]
    raw_y = full[..., -1].tolist()
    self.y = []
    from model.network import Network
    for i in range(len(raw_y)):
      self.y.append([1.0 if raw_y[i] == j else 0.0 for j in range(ModelConfig.n_classes)])
    self.y = np.asarray(self.y, dtype=np.float32)

    self.train_upto = int(full.shape[0] * 6 / 10)
    self.validate_upto = self.train_upto + int(full.shape[0] * 2 / 10)
    self.test_upto = int(full.shape[0])

  def next_batch_train(self, batch_size):
    terminal_batch_count = self.train_batch_count + batch_size
    x = self.x[self.train_batch_count:terminal_batch_count]
    y = self.y[self.train_batch_count:terminal_batch_count]

    if terminal_batch_count <= self.train_upto:
      self.train_batch_count = terminal_batch_count
      return x, y

    rotated_batch_count = batch_size - x.shape[0]
    x = np.concatenate((x, self.x[:rotated_batch_count]), axis=0)
    y = np.concatenate((y, self.y[:rotated_batch_count]), axis=0)
    self.train_batch_count = rotated_batch_count
    return x, y

  def test_data_all(self):
    return self.x[self.validate_upto:self.test_upto], \
           self.y[self.validate_upto:self.test_upto]

  def validate_data_all(self):
    return self.x[self.train_upto:self.validate_upto], \
           self.y[self.train_upto:self.validate_upto]

  def num_train_data_entries(self):
    return self.train_upto
