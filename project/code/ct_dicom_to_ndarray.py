import numpy as np
import pandas as pd
import cPickle as pickle
import dicom
import os

ArrayList = list()
# FolderPath = "/Users/smopart/Desktop/SPIE-AAPM_Lung_CT_Challenge/DOI/"

for PathDicom,b,c in os.walk(FolderPath):

    if PathDicom != FolderPath:
        lstFilesDCM = []  # create an empty list

        for dirName, subdirList, fileList in os.walk(PathDicom):
            for filename in fileList:
                if ".dcm" in filename.lower():  # check whether the file's DICOM
                    lstFilesDCM.append(os.path.join(dirName,filename))



        # Get ref file
        RefDs = dicom.read_file(lstFilesDCM[0])

        # Load dimensions based on the number of rows, columns, and slices (along the Z axis)
        ConstPixelDims = (int(RefDs.Rows), int(RefDs.Columns), len(lstFilesDCM))

        # Load spacing values (in mm)
        ConstPixelSpacing = (float(RefDs.PixelSpacing[0]), float(RefDs.PixelSpacing[1]), float(RefDs.SliceThickness))

        x = np.arange(0.0, (ConstPixelDims[0]+1)*ConstPixelSpacing[0], ConstPixelSpacing[0])
        y = np.arange(0.0, (ConstPixelDims[1]+1)*ConstPixelSpacing[1], ConstPixelSpacing[1])
        z = np.arange(0.0, (ConstPixelDims[2]+1)*ConstPixelSpacing[2], ConstPixelSpacing[2])

        # The array is sized based on 'ConstPixelDims'
        ArrayDicom = np.zeros(ConstPixelDims, dtype=RefDs.pixel_array.dtype)

        locations = list()

        for i in xrange(len(lstFilesDCM)):
            location = dicom.read_file(lstFilesDCM[i])
            locations.append(int(location.SliceLocation))

        locations = np.array(locations)
        number_slices = locations.max()-locations.min()
        minimum = locations.min()

        # loop through all the DICOM files
        for filenameDCM in lstFilesDCM:
            # read the file
            ds = dicom.read_file(filenameDCM)
            # store the raw image data
            ArrayDicom[:, :, (int(ds.SliceLocation)-int(minimum))] = ds.pixel_array

        ArrayList.append(ArrayDicom)

first_ten = ArrayList[0:10]
second_ten = ArrayList[10:20]
third_ten = ArrayList[20:30]
fourth_ten = ArrayList[30:40]
fifth_ten = ArrayList[40:50]
sixth_ten = ArrayList[50:60]
seventh_ten = ArrayList[60:70]

pickle.dump(first_ten, open( "../data/first_ten_arrays.p", "wb" ))
pickle.dump(second_ten, open( "../data/second_ten_arrays.p", "wb" ))
pickle.dump(third_ten, open( "../data/third_ten_arrays.p", "wb" ))
pickle.dump(fourth_ten, open( "../data/fourth_ten_arrays.p", "wb" ))
pickle.dump(fifth_ten, open( "../data/fifth_ten_arrays.p", "wb" ))
pickle.dump(sixth_ten, open( "../data/sixth_ten_arrays.p", "wb" ))
pickle.dump(seventh_ten, open( "../data/seventh_ten_arrays.p", "wb" ))
