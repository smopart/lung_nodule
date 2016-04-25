import numpy as np
import pandas as pd
import cPickle as pickle
import dicom
import os

# Collecting Patient Information

# FolderPath = "/Users/smopart/Desktop/SPIE-AAPM_Lung_CT_Challenge/DOI/"

ArrayList = list()
IDs = list()
Ages = list()
Sexes = list()

for PathDicom,b,c in os.walk(FolderPath):

    if PathDicom != FolderPath:
        lstFilesDCM = []  # create an empty list

        for dirName, subdirList, fileList in os.walk(PathDicom):
            for filename in fileList:
                if ".dcm" in filename.lower():  # check whether the file's DICOM
                    lstFilesDCM.append(os.path.join(dirName,filename))



        # Get ref file
        RefDs = dicom.read_file(lstFilesDCM[0])

        IDs.append(RefDs.PatientID)
        Ages.append(RefDs.PatientAge)
        Sexes.append(RefDs.PatientSex)

IDs = pd.DataFrame(IDs, columns = ["Patient_ID"])
Ages = pd.DataFrame(Ages, columns = ["Patient_Age"])
Sexes = pd.DataFrame(Sexes, columns = ["Patient_Sex"])

patients = pd.concat([IDs, Sexes, Ages],axis =1, ignore_index=False)

patients.to_csv("../data/patient_identification.csv", index = False)

#Creating final_training.csv for first_ten; turning strings to floats
train_patients = patients.iloc[0:10]
train_data = pd.read_csv("../data/train_data.csv")

for i in xrange(len(train_patients)):
    train_patients["Patient_ID"][i] = train_patients["Patient_ID"][i].lower()

for i in xrange(len(train_data)):
    train_data["Scan Number"][i] = train_data["Scan Number"][i].lower()

target_x = list()
target_y = list()
target_z = list()
target_dx = list()

for i in xrange(len(train_patients)):
    targetx = train_data[train_data["Scan Number"] == train_patients["Patient_ID"][i]]["nodule_x"]
    target_x.append(float(targetx))

    targety = train_data[train_data["Scan Number"] == train_patients["Patient_ID"][i]]["nodule_y"]
    target_y.append(float(targety))

    targetz = train_data[train_data["Scan Number"] == train_patients["Patient_ID"][i]]["nodule_z"]
    target_z.append(float(targetz))

# In terms of the first_ten array order
Diagnosis_list = ["benign", "benign", "benign", "benign", "benign", "malignant", "malignant", "malignant", "malignant", "malignant"]

target_x = pd.DataFrame(target_x, columns = ["Nodule_x"])
target_y = pd.DataFrame(target_y, columns = ["Nodule_y"])
target_z = pd.DataFrame(target_z, columns = ["Nodule_z"])
diagnosis = pd.DataFrame(Diagnosis_list, columns = ["Diagnosis"])

add_columns = pd.concat([target_x, target_y, target_z, diagnosis], axis = 1)
final_train = pd.concat([train_patients, add_columns], axis = 1)
final_train.to_csv("../data/final_training.csv", index=False)
