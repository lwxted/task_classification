# -*- coding: utf-8 -*-

import numpy as np
import os
import shutil

from gensim.models.keyedvectors import KeyedVectors

class Embedding(object):

  def load_w2v_model(self, model_path, binary):
    self.model_path = model_path
    self.model = KeyedVectors.load_word2vec_format(self.model_path, binary=binary)
    self.vocab = list(self.model.vocab)                         # ['a', 'b', ...]
    self.inv_vocab = {v : i for i, v in enumerate(self.vocab)}  # {'a' : 0, 'b' : 1}
    self.vocab_size_orig = len(self.vocab)
    self.vocab_size = len(self.vocab)
    self.embedding_size = 300
    self.embeddings = [None] * self.vocab_size
    for i, v in enumerate(self.vocab):
      self.embeddings[i] = self.model.word_vec(v)
    self.range_max = np.max(self.embeddings)
    self.range_min = np.min(self.embeddings)

  def __random_embedding(self):
    return np.random.uniform(-1.0, 1.0, self.embedding_size)

  def of(self, word):
    if word not in self.inv_vocab:
      print('word {} not in embedding'.format(word))
      self.inv_vocab[word] = self.vocab_size
      self.vocab.append(word)
      self.vocab_size += 1
      random_embedding = self.__random_embedding()
      self.embeddings.append(random_embedding)
    return self.embeddings[self.inv_vocab[word]]

  def persist(self):
    if self.vocab_size == self.vocab_size_orig:
      return

    with open(self.model_path, 'a') as f:
      for i in range(self.vocab_size_orig, self.vocab_size):
        f.write(self.vocab[i] + ' ' + ' '.join(str(n) for n in self.embeddings[i].tolist()) + '\n')

    tmp_name = self.model_path + '_tmp'
    os.rename(self.model_path, tmp_name)

    with open(tmp_name, 'r') as r_tmp:
      with open(self.model_path, 'w') as w:
        r_tmp.readline()
        w.write(str(self.vocab_size) + ' ' + str(self.embedding_size) + '\n')
        shutil.copyfileobj(r_tmp, w)

    os.remove(tmp_name)

  def emb(self):
    return self.embbeddings

if __name__ == '__main__':
  pass
