from __future__ import print_function
import cPickle as pickle
import moviepy.editor as mpy
from PIL import Image
from scipy.misc import imresize
import numpy as np

def create_movie(array, name):
    '''
    Creates a 1-channel grayscale movie at 10 frames per second
    array: a 3-dimensional array
    name: name of output gif file [e.g."myvideo.gif"]
    '''
    images_list = list()
    for i in xrange(array.shape[2]):
        image0 = array[:,:,i]
        images_list.append(imresize(image0, 1.0))

    my_clip = mpy.ImageSequenceClip(images_list,fps = 10)
    my_clip.write_gif(name,fps=10)


def create_color_movie(ct,prob_map,threshold, color, color_intensity = 1000, name):
    '''
    Creates a 3-channel, 10-frames per second color movie in .gif formatting
    Inputs:
    ct: a 3-dimensional 1-channel array of a CT-scan
    prob_map: a 3-dimensional array containing the voxel probability outputs of a
            neural network
    threshold: desired probability threshold for shading
               values greater than the threshold will be shaded
    color: Choose 1 of the following: ["red", "green", "blue"]
            desired shading color of output
    color_intensity: desired pixel intensity of probability shading
                    Default = 1000
    name: file name of desired output [e.g. "myvideo.gif"]
    '''
    images_list = list()

    prob_map[prob_map > threshold] = 1*color_intensity
    prob_map[prob_map <= threshold] = 0

    color_filter = ct + prob_map
    for i in xrange(ct.shape[2]):
        image_array = np.zeros((ct.shape[0],ct.shape[1],3))

        if color == "blue":
            image0  = ct[:,:,i]
            image1 =  ct[:,:,i]
            image2 = color_filter[:,:,i]

        elif color == "red":
            image0  = color_filter[:,:,i]
            image1 =  ct[:,:,i]
            image2 = ct[:,:,i]

        elif color == "green":
            image0  = ct[:,:,i]
            image1 =  color_filter[:,:,i]
            image2 = ct[:,:,i]

        image_array[:,:,0] = imresize(image0,1.0)
        image_array[:,:,1] = imresize(image1,1.0)
        image_array[:,:,2] = imresize(image2,1.0)

        images_list.append(image_array)

    my_clip = mpy.ImageSequenceClip(images_list,fps = 10)
    my_clip.write_gif(name,fps=10)
