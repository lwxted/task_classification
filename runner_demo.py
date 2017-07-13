# -*- coding: utf-8 -*-

from model.embedding import Embedding
from model.network import Network

import numpy as np
import jieba
import os

import sys

base_path = os.path.dirname(os.path.realpath(__file__))
model = Network(None, os.path.join(base_path, 'log.nosync/network_demo/run1'))
model.load_model(os.path.join(base_path, 'model.nosync/lstm_early_stopping_without_conc'))

path = os.path.join(base_path, 'word2vec_model/wiki.zh.nosync/wiki.zh.vec')
embedding = Embedding()
embedding.load_w2v_model(path, False)

max_steps = 15
n_embedding = 300

categories = [
  '订会议室',
  '设置闹钟',
  '拨打电话',
  '查询天气',
  '订火车票',
  '订飞机票',
  '取消会议',
  '设置提醒'
]

def run(s):
  print(s)
  seg_list = jieba.cut(s)
  words = [w for w in seg_list]
  print('/'.join(words))
  feature = [embedding.of(w) for w in words]
  if len(feature) < max_steps:
    for i in range(len(feature), max_steps):
      feature.append(np.zeros(n_embedding))
  prediction = model.run_dummy(feature, np.array([1, 0, 0, 0, 0, 0, 0, 0]))
  for i, p in enumerate(prediction.tolist()[0]):
    print(categories[i], '{}%'.format(float(p) * 100.0))

if __name__ == '__main__':
  s = sys.argv[1]
  run(s)
