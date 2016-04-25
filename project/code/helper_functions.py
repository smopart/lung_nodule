import gzip
import numpy as np
import pandas as pd
import cPickle as pickle
import time
from datetime import datetime

import sklearn
from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, precision_recall_curve, f1_score, confusion_matrix, roc_curve, auc, roc_auc_score
from sklearn import metrics

import matplotlib
matplotlib.use("Pdf")
import matplotlib.pyplot as plt

def confusion_matrix_self(y_true, y_predict):
    '''
               actual
             __1____0__
 predicted   1|TP | FP|
             0|FN | TN|

    '''
    confused = confusion_matrix(y_true,y_predict)
    TN = confused[0][0]
    FP = confused[0][1]
    FN = confused[1][0]
    TP = confused[1][1]
    confusion_mat = np.array([[TP, FP],[FN, TN]])
    return confusion_mat

def threshold_creator(fitted_model, X_test, y_test):
    ''' Create Thresholds of Classification models Accuracy,Precision,
    Recall, F1 score as the threshold voting rule of the random forest
    is changed in increments of 0.01 (graphs made with 101 different threshold values)
    '''


    #Initializing Values
    threshold_list = []
    accuracy_list = []
    precision_list = []
    recall_list = []
    f1_list = []
    confusion_matrix_list = []
    expected_profit_list = []
    threshold = 0.00

    #Acquiring Predicted Probabilities
    predicted_probs= fitted_model.predict_proba(X_test)
    col_true = predicted_probs[:,1]


    while threshold <= 1.0:
        y_predict = col_true > threshold
        confusion_matrix_instance = confusion_matrix_self(y_test,y_predict)

        threshold_list.append(threshold)
        accuracy_list.append(accuracy_score(y_test, y_predict))
        precision_list.append(precision_score(y_test, y_predict))
        recall_list.append(recall_score(y_test, y_predict))
        f1_list.append(f1_score(y_test, y_predict))
        confusion_matrix_list.append(confusion_matrix_instance)
        threshold += 0.01


    return threshold_list, accuracy_list, precision_list, recall_list, f1_list

def plotting_thresholds(threshold_list, accuracy_list, precision_list, recall_list, f1_list):

    fig = plt.figure()

    ax1 = fig.add_subplot(221)
    ax1.plot(threshold_list,accuracy_list)
    ax1.set_xlabel('Threshold', fontsize=10)
    ax1.set_ylabel('Accuracy', fontsize=10)

    ax2 = fig.add_subplot(222)
    ax2.plot(threshold_list,precision_list)
    ax2.set_xlabel('Threshold', fontsize=10)
    ax2.set_ylabel('Precision', fontsize=10)

    ax3 = fig.add_subplot(223)
    ax3.plot(threshold_list,recall_list)
    ax3.set_xlabel('Threshold', fontsize=10)
    ax3.set_ylabel('Recall', fontsize=10)

    ax4 = fig.add_subplot(224)
    ax4.plot(threshold_list,f1_list)
    ax4.set_xlabel('Threshold', fontsize=10)
    ax4.set_ylabel('F1 Score', fontsize=10)

    plt.tight_layout()

def roc_curve_plot(actual, predictions):
    false_positive_rate, true_positive_rate, thresholds = roc_curve(actual, predictions)
    roc_auc = auc(false_positive_rate, true_positive_rate)

    plt.figure()
    plt.title('Receiver Operating Characteristic')
    plt.plot(false_positive_rate, true_positive_rate, 'b',
    label='AUC = %0.2f'% roc_auc)
    plt.legend(loc='lower right')
    plt.plot([0,1],[0,1],'r--')
    plt.xlim([0,1.0])
    plt.ylim([0,1.0])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()
