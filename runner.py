# -*- coding: utf-8 -*-

import os

from model.data import Data
from model.network import Network

if __name__ == '__main__':
  dir_path = os.path.dirname(os.path.realpath(__file__))
  data = Data()
  data.load_data_from_file(os.path.join(dir_path, 'data.nosync/all_data.npy'))
  model = Network(data, os.path.join(dir_path, 'log.nosync/network/run4'))
  # model.load_model(os.path.join(dir_path, 'model.nosync/cnn_early_stopping_without_conc'))
  # model.run_dummy()
  model.train()
  # model.test()
  # model.export_for_bnns(os.path.join(dir_path, 'bnns.nosync'))
