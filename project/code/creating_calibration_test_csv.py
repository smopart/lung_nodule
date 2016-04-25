import numpy as np
import pandas as pd
import cPickle as pickle
import os

#Creating Calibration Set .csv file
calibration = pd.read_excel("../data/CalibrationSet_NoduleData.xlsx")
train_data=calibration.iloc[0:10]

Nodule_X = []
Nodule_Y = []
Nodule_Z = []

train_data_list = []
for i in xrange(len(train_data)):
    train_data_list.append(train_data["Nodule Center x,y Position*"][i].split(", "))

for row in xrange(len(train_data_list)):
    for col in xrange(len(train_data_list[row])):
        if col == 0:
            Nodule_X.append(float(train_data_list[row][col]))
        elif col == 1:
            Nodule_Y.append(float(train_data_list[row][col]))


for row in xrange(len(train_data["Nodule Center Image"])):
    Nodule_Z.append(train_data["Nodule Center Image"][row])

nodule_x = pd.DataFrame(Nodule_X,columns = ["nodule_x"])
nodule_y = pd.DataFrame(Nodule_Y, columns = ["nodule_y"])
nodule_z = pd.DataFrame(Nodule_Z, columns = ["nodule_z"])

train_data.drop(['Nodule Center x,y Position*', 'Nodule Center Image'], axis = 1, inplace=True)

new_columns = pd.concat([nodule_x, nodule_y, nodule_z], axis= 1)
train_data = pd.concat([train_data, new_columns], axis =1)

train_data.to_csv("../data/train_data.csv", index = False)


#Creating test_data.csv

test = pd.read_excel("../data/TestSet_NoduleData.xlsx")
test_data = test.iloc[0:73]

Nodule_X = []
Nodule_Y = []
Nodule_Z = []

test_data_list = []
for i in xrange(len(test_data)):
    test_data_list.append(test_data["Nodule Center x,y Position*"][i].split(", "))

for row in xrange(len(test_data_list)):
    for col in xrange(len(test_data_list[row])):
        if col == 0:
            Nodule_X.append(float(test_data_list[row][col]))
        elif col == 1:
            Nodule_Y.append(float(test_data_list[row][col]))


for row in xrange(len(test_data["Nodule Center Image"])):
    Nodule_Z.append(test_data["Nodule Center Image"][row])


nodule_x = pd.DataFrame(Nodule_X,columns = ["nodule_x"])
nodule_y = pd.DataFrame(Nodule_Y, columns = ["nodule_y"])
nodule_z = pd.DataFrame(Nodule_Z, columns = ["nodule_z"])

new_columns = pd.concat([nodule_x, nodule_y, nodule_z], axis= 1)
test_data = pd.concat([test_data, new_columns], axis =1)
test_data.drop(['Nodule Center x,y Position*', 'Nodule Center Image'], axis = 1, inplace=True)

test_data.to_csv("../data/test_data.csv", index = False)
