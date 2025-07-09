import json
import numpy as np
import tensorflow as tf
from tensorflow import keras
# import sequencial model deep learning technique use in it
from tensorflow.keras.models import sequential
# import layer for deep learning
from tensorflow.keras.layer import Dense, Embedding, GlobalAveragePooling1D 
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_seqences
from sklearn.preprocessing import LabelEncoder