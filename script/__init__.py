# -*- coding: utf-8 -*-
# @Time    : 2020-05-23
# @Author  : 爱吃苹果的鱼

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 表示上一级目录
sys.path.insert(0, BASE_DIR+"/framework/base")
sys.path.insert(1, BASE_DIR+"/framework/api")
sys.path.insert(2, BASE_DIR+"/framework/app")
sys.path.insert(4, BASE_DIR+"/framework/driver")
sys.path.insert(5, BASE_DIR+"/framework/web")
sys.path.insert(6, BASE_DIR+"/framework/utils")
