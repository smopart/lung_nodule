import numpy as np
import pandas as pd
import os
import dicom
import cPickle as pickle
import random

#Loading Data
second_ten_positive = pickle.load(open("../data/41_41_7/second_ten_positive_array.p","rb"))
third_ten_positive = pickle.load(open("../data/41_41_7/third_ten_positive_array.p","rb"))
fourth_ten_positive = pickle.load(open("../data/41_41_7/fourth_ten_positive_array.p","rb"))
fifth_ten_positive = pickle.load(open("../data/41_41_7/fifth_ten_positive_array.p","rb"))
sixth_ten_positive = pickle.load(open("../data/41_41_7/sixth_ten_positive_array.p","rb"))
seventh_ten_positive = pickle.load(open("../data/41_41_7/seventh_ten_positive_array.p","rb"))

second_ten_negative = pickle.load(open("../data/41_41_7/second_ten_negative_array.p","rb"))
third_ten_negative = pickle.load(open("../data/41_41_7/third_ten_negative_array.p","rb"))
fourth_ten_negative = pickle.load(open("../data/41_41_7/fourth_ten_negative_array.p","rb"))
fifth_ten_negative = pickle.load(open("../data/41_41_7/fifth_ten_negative_array.p","rb"))
sixth_ten_negative = pickle.load(open("../data/41_41_7/sixth_ten_negative_array.p","rb"))
seventh_ten_negative = pickle.load(open("../data/41_41_7/seventh_ten_negative_array.p","rb"))

second_ten_positive = pd.read_csv("../data/41_41_7/second_ten_positive_df.csv")
second_ten_negative = pd.read_csv('../data/41_41_7/second_ten_negative_df.csv')

third_ten_positive = pd.read_csv("../data/41_41_7/third_ten_positive_df.csv")
third_ten_negative = pd.read_csv('../data/41_41_7/third_ten_negative_df.csv')

fourth_ten_positive = pd.read_csv("../data/41_41_7/fourth_ten_positive_df.csv")
fourth_ten_negative = pd.read_csv('../data/41_41_7/fourth_ten_negative_df.csv')

fifth_ten_positive = pd.read_csv("../data/41_41_7/fifth_ten_positive_df.csv")
fifth_ten_negative = pd.read_csv('../data/41_41_7/fifth_ten_negative_df.csv')

sixth_ten_positive = pd.read_csv("../data/41_41_7/sixth_ten_positive_df.csv")
sixth_ten_negative = pd.read_csv('../data/41_41_7/sixth_ten_negative_df.csv')

seventh_ten_positive = pd.read_csv("../data/41_41_7/seventh_ten_positive_df.csv")
seventh_ten_negative = pd.read_csv('../data/41_41_7/seventh_ten_negative_df.csv')

#Creating full arrays
full_positive_array = np.concatenate((second_ten_positive,third_ten_positive,fourth_ten_positive,fifth_ten_positive,sixth_ten_positive,seventh_ten_positive))
full_negative_array = np.concatenate((second_ten_negative, third_ten_negative, fourth_ten_negative, fifth_ten_negative, sixth_ten_negative, seventh_ten_negative))

positive_list = [second_ten_positive, third_ten_positive, fourth_ten_positive, fifth_ten_positive, sixth_ten_positive, seventh_ten_positive]
negative_list = [second_ten_negative, third_ten_negative, fourth_ten_negative, fifth_ten_negative, sixth_ten_negative, seventh_ten_negative]

positive_array = pd.concat(positive_list,ignore_index = True)
negative_array = pd.concat(negative_list, ignore_index = True)
true_df = pd.DataFrame([True]*positive_array.shape[0], columns=["Nodule?"])
false_df = pd.DataFrame([False]*negative_array.shape[0], columns=["Nodule?"])
positives  = pd.concat([positive_array, true_df], axis = 1)
negatives = pd.concat([negative_array, false_df], axis = 1)

#Creating Train/Test Split
train_pos = full_positive[0:400]
test_pos = full_positive[400:600]
train_neg = full_negative[0:400]
test_neg = full_negative[400:600]

train_true_y = positives.iloc[0:400]["Nodule?"]
test_true_y = positives.iloc[400:600]["Nodule?"]
train_false_y = negatives.iloc[0:400]["Nodule?"]
test_false_y = negatives.iloc[400:600]["Nodule?"]

train_x = np.concatenate([train_pos, train_neg])
test_x = np.concatenate([test_pos, test_neg])

train_y = np.concatenate([train_true_y,train_false_y])
test_y = np.concatenate([test_true_y, test_false_y])

print "train_x shape:" + str(train_x.shape)
print "train_y shape:" + str(train_y.shape)
print "-"*40
print "test_x shape:" + str(test_x.shape)
print "test_y shape:" + str(test_y.shape)

pickle.dump(train_x, open("../data/41_41_7/train_x.p","wb"))
pickle.dump(train_y, open("../data/41_41_7/train_y.p","wb"))
pickle.dump(test_x, open("../data/41_41_7/test_x.p","wb"))
pickle.dump(test_y, open("../data/41_41_7/test_y.p","wb"))
