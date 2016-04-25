import numpy as np
import pandas as pd
import os
import dicom
import cPickle as pickle

import moviepy.editor as mpy
from PIL import Image
from scipy.misc import imresize

#FolderPath = "/Users/smopart/Desktop/lung_sample"

FolderPath = "/Users/smopart/Desktop/lung_sample"
lstFilesDCM = []  # create an empty list

for dirName, subdirList, fileList in os.walk(FolderPath):
    for filename in fileList:
        if ".dcm" in filename.lower():  # check whether the file's DICOM
            lstFilesDCM.append(os.path.join(dirName,filename))

# Get ref file
RefDs = dicom.read_file(lstFilesDCM[0])

# Load dimensions based on the number of rows, columns, and slices (along the Z axis)
ConstPixelDims = (int(RefDs.Rows), int(RefDs.Columns), len(lstFilesDCM))

# Load spacing values (in mm)
ConstPixelSpacing = (float(RefDs.PixelSpacing[0]), float(RefDs.PixelSpacing[1]), float(RefDs.SliceThickness))

# The array is sized based on 'ConstPixelDims'
CT_Scan_Array = np.zeros(ConstPixelDims, dtype=RefDs.pixel_array.dtype)

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
    CT_Scan_Array[:, :, (int(ds.SliceLocation)-int(minimum))] = ds.pixel_array

images_list = list()
for i in xrange(CT_Scan_Array.shape[2]):
    image0 = CT_Scan_Array[:,:,i]
    images_list.append(imresize(image0, 0.5))

my_clip = mpy.ImageSequenceClip(images_list,fps = 10)
my_clip.write_gif("static/img/ct.gif",fps=10)
