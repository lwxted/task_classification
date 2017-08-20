# -*- coding: utf-8 -*-

from model.embedding import Embedding
from model.network import Network

from extractor.utterance.all import UtteranceAll

import numpy as np
import jieba
import os
import sys
# import thulac

# thulac_seg = thulac.thulac(seg_only=True)

base_path = os.path.dirname(os.path.realpath(__file__))
model = Network(None, os.path.join(base_path, 'log.nosync/network_demo/run1'))
model.load_model(os.path.join(base_path, 'model_checkpoint/lstm_early_stopping_without_conc'))

path = os.path.join(base_path, 'word2vec_model/wiki.zh.nosync/wiki.zh.vec')
embedding = Embedding()
embedding.load_w2v_model(path, False)

max_steps = model.n_input_steps
n_embedding = model.n_embedding

categories = [
  '开关语音播报',
  '打电话',
  '发短信',
  '发邮件',
  '导航',
  '离职倾向',
  'KPI',
  '访问网站',
  '会议室预定',
  '设置提醒',
  '查日程安排',
  '查会议安排',
  '查会议室安排情况',
  '查月度工作任务',
  '查工作任务完成情况',
  '查月度预算执行情况',
  '查当月费用报销情况',
  '查借款情况',
  '查应收款',
  '查应付款',
  '查考勤',
  '查出差情况',
  '查天气',
  '查股票',
  '讲笑话',
  '讲故事',
  '讲新闻',
  '订机票',
  '订火车票'
]

def run(s, verbose=False):
  s = s.lower()
  print(' ', s)
  seg_list = jieba.cut(s)
  # seg_list = [l[0] for l in thulac_seg.cut(s)]
  words = [w for w in seg_list]
  print(' ', '/'.join(words))
  feature = [embedding.of(w) for w in words]
  if len(feature) < max_steps:
    for i in range(len(feature), max_steps):
      feature.append(np.zeros(n_embedding))
  prediction = model.run_dummy(feature, np.array([0] * model.n_classes))
  max_i = -1
  for p, i in sorted([(prec, label) for label, prec in enumerate(prediction.tolist()[0])], reverse=True)[:8]:
    if max_i == -1:
      max_i = i
    print(' ', categories[i].ljust(30), '{}%'.format(float(p) * 100.0))
  print('  ....')

  # ------

  utterance = UtteranceAll.with_category(max_i)
  if utterance is not None:
    for t in utterance.match(s, exact_match=False):
      print('  ----------------------------')
      print('  用户文本: {}'.format(t.query))
      print('  匹配类型: {}'.format(t.rule_identifier))
      print('  匹配区段: ({}, {})'.format(t.match_start, t.match_end))
      print('  匹配区段原始值: {}'.format(t.query[t.match_start:t.match_end]))
      print('  匹配槽:')
      for key, val in t.slot_mappings.items():
        print('  [{}] {} -> {}'.format(val.slot_type.__name__, key, val.slot_value))
      print('  ----------------------------')
      if verbose:
        print('  匹配表达式: {}'.format(t.raw_rule))
        print('  匹配展开表达式: {}'.format(t.matched_rule))
        print('  匹配区间:')
        for seg in t.match_segments:
          print('  {}'.format(seg))
        print('  ----------------------------')

if __name__ == '__main__':
  s = sys.argv[1]
  run(s)
