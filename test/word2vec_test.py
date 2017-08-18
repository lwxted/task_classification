# -*- coding: utf-8 -*-

from gensim.models.keyedvectors import KeyedVectors
model = KeyedVectors.load_word2vec_format("./word2vec_model/wiki.zh.nosync/wiki.zh.vec", binary=False)
print(model.wv.most_similar("预订"))
