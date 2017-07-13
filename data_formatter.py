# -*- coding: utf-8 -*-

from model.embedding import Embedding

import numpy as np
import os
import random
import jieba

max_sample = 4000
max_steps = 15
n_embedding = 300

base_path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(base_path, 'word2vec_model/wiki.zh.nosync/wiki.zh.vec')
embedding = Embedding()
embedding.load_w2v_model(path, False)

data = dict()
data_dir_path = os.path.join(base_path, 'data.nosync')
for fname in os.listdir(data_dir_path):
  if '.txt' not in fname:
    continue
  train_file_path = os.path.join(data_dir_path, fname)
  with open(train_file_path, 'r') as f:
    for l in f:
      comps = l.strip().split()
      label = int(comps[1])
      if label not in data:
        data[label] = []
      data[label].append((comps[0], label))

for k in data:
  random.shuffle(data[k])
  data[k] = data[k][:min(max_sample, len(data[k]))]
  print(len(data[k]), data[k][:5])

all_data = []
all_labels = []
for k in data:
  for s, l in data[k]:
    seg_list = jieba.cut(s)
    feature = [embedding.of(w) for w in seg_list]
    if len(feature) < max_steps:
      for i in range(len(feature), max_steps):
        feature.append(np.zeros(n_embedding))
    feature = np.array(feature[:max_steps])
    all_data.append(np.reshape(feature, (max_steps * n_embedding)))
    all_labels.append(np.array([l]))

all_data_np = np.array(all_data)
all_labels_np = np.array(all_labels)

data_w_labels_np = np.hstack((all_data, all_labels))

print(all_data_np.shape)
print(all_labels_np.shape)
print(data_w_labels_np.shape)

np.save(base_path + '/data.nosync/all_data.npy', data_w_labels_np)

embedding.persist()
