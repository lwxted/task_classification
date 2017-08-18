# -*- coding: utf-8 -*-

from config import Config
from model.embedding import Embedding

import numpy as np
import os
import random
import jieba
# import thulac

# thulac_seg = thulac.thulac(seg_only=True)

max_sample = 1000
max_steps = 15
n_embedding = 300

base_path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(base_path, 'word2vec_model/wiki.zh.nosync/wiki.zh.vec')
model_path = os.path.join(base_path, Config.CURRENT_MODEL_BASE_PATH)
embedding = Embedding()
embedding.load_w2v_model(path, False)

data = dict()
data_dir_path = os.path.join(model_path, 'data.nosync')
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
  if len(data[k]) < max_sample:
    data[k] = data[k] * (max_sample // len(data[k])) + data[k][:(max_sample % len(data[k]))]
  random.shuffle(data[k])
  data[k] = data[k][:min(max_sample, len(data[k]))]
  print(len(data[k]), data[k][:5])
  print('')

all_data = []
all_labels = []
for k in data:
  for s, l in data[k]:
    seg_list = jieba.cut(s)
    # seg_list = [l[0] for l in thulac_seg.cut(s)]
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

np.save(os.path.join(model_path, 'data.nosync/all_data.npy'), data_w_labels_np)

embedding.persist()
