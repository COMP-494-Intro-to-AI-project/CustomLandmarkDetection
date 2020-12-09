# USAGE
# python tune_predictor_hyperparams.py
# import the necessary packages
from pyimagesearch import config
from sklearn.model_selection import ParameterGrid
import multiprocessing
import numpy as np
import random
import time
import dlib
import cv2
import os
import cProfile
import re

dlib.test_shape_predictor(config.TEST_PATH, config.TEMP_MODEL_PATH)
