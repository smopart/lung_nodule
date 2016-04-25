import lasagne
import theano

import sklearn
from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, precision_recall_curve, f1_score, confusion_matrix, roc_curve, auc, roc_auc_score
from sklearn import metrics

from lasagne import layers
from lasagne.nonlinearities import  sigmoid, softmax, rectify, tanh, linear
from lasagne.updates import nesterov_momentum, adagrad, adam
from nolearn.lasagne import NeuralNet

import gzip
import numpy as np
import pandas as pd
import cPickle as pickle
import time
from datetime import datetime


import matplotlib
matplotlib.use("Pdf")
import matplotlib.pyplot as plt
%matplotlib inline

from helper_functions import *

#Load and reshape data
train_x = pickle.load(open("/home/ubuntu/41_41_7_train_test/train_x.p","rb"))
train_y = pickle.load(open("/home/ubuntu/41_41_7_train_test/train_y.p","rb"))
test_x = pickle.load(open("/home/ubuntu/41_41_7_train_test/test_x.p","rb"))
test_y = pickle.load(open("/home/ubuntu/41_41_7_train_test/test_y.p","rb"))

train_x = train_x.astype(np.float32)
train_y = train_y.astype(np.int32)
test_x = test_x.astype(np.float32)
test_y = test_y.astype(np.int32)

train_x = train_x.reshape(train_x.shape[0],1,train_x.shape[1],train_x.shape[2],train_x.shape[3])
test_x = test_x.reshape(test_x.shape[0],1,test_x.shape[1],test_x.shape[2],test_x.shape[3])


nn = NeuralNet(
        #    layers=[('input', layers.InputLayer),
        #           ('conv1', layers.dnn.Conv3DDNNLayer),
        #            ('pool1', layers.dnn.MaxPool3DDNNLayer),
        #           ('conv2', layers.dnn.Conv3DDNNLayer),
        #            ('pool2', layers.dnn.MaxPool3DDNNLayer),
        #           ('lstm1', layers.LSTMLayer),
        #            ('hidden1', layers.DenseLayer),
        #           ('dropout1', layers.DropoutLayer),
        #            ('hidden2', layers.DenseLayer),
        #            ('output', layers.DenseLayer),
        #    ],
         #
        #    # Input Layer
        #    input_shape=(None,1, 7, 41, 41),
        #
        #  #Convolutional1 Layer
         #
        #    conv1_num_filters = 40,
        #    conv1_nonlinearity = rectify,
        #    conv1_filter_size=(3, 3, 3),
        #    conv1_stride = (1,1,1),
        #    conv1_pad = "full",
        #
        #    # Pooling1 Layer
        #    pool1_pool_size = 5,
        #
        #    #Convolutional Layer 2
        #    conv2_num_filters = 20,
        #    conv2_nonlinearity = rectify,
        #    conv2_filter_size=(3, 3,3),
        #    conv2_pad = "full",
        #
        #    #Pooling2 Layer
        #    pool2_pool_size = 2,
        #
        #     #LSTM Layer
        #    lstm1_num_units = 10,
         #
        #    #1st Hidden Layer
        #    hidden1_num_units=60,
        #    hidden1_nonlinearity=rectify,
        #
        #    #Dropout Layer
        #    dropout1_p = 0.5,
        #
        #     # 2nd Hidden Layer
        #      hidden2_num_units=10,
        #      hidden2_nonlinearity=rectify,
         #
        #    # Output Layer
        #    output_num_units=2,
        #    output_nonlinearity=softmax,
         #
        #    # Optimization
        #    update=nesterov_momentum,
        #    update_learning_rate=0.05,
        #    update_momentum=0.5,
        #    max_epochs=25,
         #
        #    update = adagrad,
        #    update_learning_rate = .07,
        #    max_epochs = 50,
         #
        #    # Others
        #    regression=False,
        #    verbose=1,
     )

nn.fit(train_x, train_y)
predict_y = nn.predict(test_x)

print "Accuracy Score: " +str(accuracy_score(test_y, predict_y))
print "Precision Score: " + str(precision_score(test_y, predict_y))
print "Recall Score: " + str(recall_score(test_y, predict_y))
print "F1 Score: " + str(f1_score(test_y, predict_y))


#Code to Create Plots *check matplotlib setting on aws GPU*

threshold_list, accuracy_list, precision_list, recall_list, f1_list = threshold_creator(nn, test_x, test_y)
plotting_thresholds(threshold_list, accuracy_list, precision_list, recall_list, f1_list)
roc_curve_plot(test_y, predict_y)
