# -*- coding: utf-8 -*-

import os

from config import Config

from model.data import Data
from model.network import Network

if __name__ == '__main__':
  dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), Config.CURRENT_MODEL_BASE_PATH)
  data = Data()
  data.load_data_from_file(os.path.join(dir_path, 'data.nosync/all_data.npy'))
  model = Network(data, os.path.join(dir_path, 'log.nosync/network/run1'))
  model.train()
