import numpy as np
import pandas as pd
import os
import dicom
import cPickle as pickle
import random
from sample_creator import sample_creator

#Load data
final_train = pd.read_csv("final_training.csv")
patient_id = pd.read_csv("patient_identification.csv")
test_data = pd.read_csv("test_data.csv")

#Load pickled arrays
#first_ten = pickle.load(open("../data/first_ten_arrays.p", "rb" ))
second_ten = pickle.load(open("../data/second_ten_arrays.p", "rb" ))
# third_ten = pickle.load(open("../data/third_ten_arrays.p", "rb" ))
# fourth_ten = pickle.load(open("../data/fourth_ten_arrays.p", "rb" ))
# fifth_ten = pickle.load(open("../data/fifth_ten_arrays.p", "rb" ))
# sixth_ten = pickle.load(open("../data/sixth_ten_arrays.p", "rb" ))
# seventh_ten = pickle.load(open("../data/seventh_ten_arrays.p", "rb" ))

#e.g. second_ten
patient = patient_id.iloc[10:20]
test = test_data.iloc[0:13]

positive_array, negative_array, positive_df, negative_df = sample_creator(second_ten, patient, test, 100, 41, 41, 7)

positive_df.to_csv("../data/41_41_7/second_ten_positive_df.csv",index = False)
negative_df.to_csv("../data/41_41_7/second_ten_negative_df.csv", index = False)

pickle.dump(positive_array, open("../data/41_41_7/second_ten_positive_array.p", "wb" ))
pickle.dump(negative_array, open("../data/41_41_7/second_ten_negative_array.p", "wb" ))
