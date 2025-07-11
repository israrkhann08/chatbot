# packages install
# pip install pyttsx3
# pip install SpeechRecognition
# pip install PyAudio
#____________________
# now we create NLP model to implement the machine can learn our language
# we create file intends.json and model_train.py
# intents.json file-->
 <p>In machine learning, a intents.json file is crucial for training conversational AI models, particularly in chatbot development. It acts as a structured knowledge base that defines the different intents (or purposes) users might have when interacting with the model, along with corresponding examples of how users might express those intents. This file essentially teaches the model what to expect and how to respond to various user inputs</p>

 # --> tensorflow keras --> SEQUENTIAL MODEL USE
 A Sequential model is appropriate for a plain stack of layers where each layer has exactly one input tensor and one output tensor.
 Link:  https://www.tensorflow.org/guide/keras/sequential_model

 # --> tensorflow keras --> LAYER Dense , Embedding , GlobalAveragePooling1D
 The tf.keras.layers.--> Dense layer in TensorFlow Keras represents a fully connected neural network layer. This means that every neuron in a Dense layer receives input from all neurons in the preceding layer.

 The Keras--> Embedding layer within TensorFlow serves as a crucial component for handling categorical data, especially in natural language processing (NLP) tasks. It transforms positive integer indices (representing categories or words) into dense, fixed-size vectors, known as embeddings

 The tf.keras.layers.--> GlobalAveragePooling1D layer in TensorFlow Keras performs a global average pooling operation on 1D temporal data. This means it calculates the average of all values along the sequence dimension for each feature, effectively reducing the sequence dimension and producing a fixed-length output vector.

 # --> TOKENIZER
 The Tokenizer class from tensorflow.keras.preprocessing.text is a utility used for text preprocessing in Keras, a high-level API for building and training deep learning models within TensorFlow. Its primary function is to convert raw text into numerical sequences, a necessary step before feeding text data into neural networks.
 Key functionalities of the Keras 

 # --> PAD_SEQUENCES
 tf.keras.preprocessing.sequence.pad_sequences is a utility function in TensorFlow Keras used for normalizing the length of sequences in a dataset. This is particularly crucial in tasks involving sequential data, such as Natural Language Processing (NLP), where input sequences (e.g., sentences) often have varying lengths.

 pip install numpy
 pip install tensorflow

import json
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Embedding, GlobalAveragePooling1D
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder


# Load data from intents.json file
with open("intents.json") as file:
    data = json.load(file)
# print("Loaded intents:", data)

training_sentences = []
training_labels = []
labels =[]
responses = []

# taking all the pattern
for intent in data['intents']:
    for pattern in intent['patterns']:
        training_sentences.append(pattern) #store all the pattern
        training_labels.append(intent['tag'])
    responses.append(intent['responses'])    

# if label is not match in the class it add in it
    if intent['tag'] not in labels:
        labels.append(intent['tag'])

#checking number of classes
number_of_classes = len(labels)    
print(number_of_classes)

# convert this tag into label encoder
label_encoder = LabelEncoder()
label_encoder.fit(training_labels) # one hot encoding
training_labels = label_encoder.transform(training_labels)

# initialize tokennizer convert ths data into tokenzier some kind of tokens
vocab_size = 1000
max_len = 20
ovv_token = "<OOV>"
embedding_dim = 16

tokenizer = Tokenizer(num_words=vocab_size, oov_token=ovv_token)
tokenizer.fit_on_texts(training_sentences)

# coming out form tokenizer
word_index = tokennizer.word_index
sequences = tokennizer.texts_to_sequences(training_sentences)
# now we need to pass my sequences into pad_sequences
padded_sequences = pad_sequences(sequences, truncating='post', maxlen=max_len)

#creating sequential model:
model = Sequential()
model.add(Embedding(vocab_size,embedding_dim, input_length=max_len ))
model.add(GlobalAveragePooling1D())
model.add(Dense(16, activation="relu"))
model.add(Dense(16, activation="relu"))
model.add(Dense(number_of_classes, activation="softmax"))

model.compile(loss='sparse_categorical_crossentropy', optimizer="adam", metrics=["accuracy"])

model.summary()
        
