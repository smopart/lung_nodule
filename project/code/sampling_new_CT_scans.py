import numpy as np
import pandas as pd
import cPickle as pickle

def cut_array(array,coordinate_df,xdim,ydim,zdim):
    '''
    Returns all 3-dimensional voxel slices of a 3-dimmensional array, given the center
    coordinate of the voxel

    a helper function for array-slicer

    Inputs:
    array: 3-dimensional array that is desired to be cut
    coordinate_df: a pandas dataframe with the coordinates of the voxel centers
    xdim: the x-dimension for any given desired voxel slices
    ydim: the y-dimension for any given desired voxel slices
    zdim: the z-dimension for any given desired voxel slices

    Output: a 5-dimensional numpy array that can fed to a noLearn/Lasgne 3D convolutional layer
            of dimension (N,0,Z,X,Y),
            where N is the number of slices
            Z: the desired Z slice dimension
            X: the desired X slice dimension
            Y: the desired Y slice dimension
    '''
    cut_array_list = list()
    scaffold = np.zeros((coordinate_df.shape[0],1,zdim,xdim,ydim))

    x_len = (xdim-1)/2
    y_len = (ydim-1)/2
    z_len = (zdim-1)/2


    for i in xrange(len(coordinate_df)):
        x_center = coordinate_df.iloc[i]["x"]
        y_center = coordinate_df.iloc[i]["y"]
        z_center = coordinate_df.iloc[i]["z"]

        x_min = x_center - x_len
        x_max = x_center + x_len + 1
        y_min = y_center - y_len
        y_max = y_center + y_len + 1
        z_min = z_center - z_len
        z_max = z_center + z_len + 1

        cut = array[x_min:x_max, y_min:y_max, z_min:z_max]


        for j in xrange(zdim):
            for k in xrange(xdim):
                for m in xrange(ydim):
                    scaffold[i,0,j,k,m] = cut[k,m,j]
    return scaffold

def array_slicer(array,xdim,ydim,zdim):
    '''
    Returns all voxel slices of a 3-dimensional array, of specified size (xdim,ydim,zdim)

    Inputs:
    array: a 3-dimensional array
    xdim: the x-dimension of the desired voxel slices
    xdim: the x-dimension of the desired voxel slices
    ydim: the y-dimension of the desired voxel slices
    zdim: the z-dimension of the desired voxel slices

    Outputs:
    cut_array: a 5 dimensional array of size (N,0,Z,X,Y) that can be fed into a
                lasagne/nolearn neural net
    coordinate_df: a pandas object containing the X,Y,Z coordinates of the center
                    of each voxel
    '''
    arr_xdim = array.shape[0]
    arr_ydim = array.shape[1]
    arr_zdim = array.shape[2]

    x_step = xdim/2
    y_step = ydim/2
    z_step = zdim/2

    base_x = xdim/2 +1
    base_y = ydim/2 +1
    base_z = zdim/2 +1

    current_x = xdim/2 +1
    current_y = ydim/2 +1
    current_z = zdim/2 +1

    x_edge = arr_xdim - base_x
    y_edge = arr_ydim - base_y
    z_edge = arr_zdim - base_z

    x_list = list()
    y_list = list()
    z_list = list()

    while (current_z <= (z_edge-z_step)):
        current_z += z_step

        current_y = base_x
        while (current_y<= (y_edge-y_step)):
            current_y += y_step

            current_x = base_x
            while (current_x <= (x_edge-x_step)):
                current_x += x_step

                x_list.append(current_x)
                y_list.append(current_y)
                z_list.append(current_z)

    x_df = pd.DataFrame(x_list, columns = ["x"])
    y_df = pd.DataFrame(y_list, columns = ["y"])
    z_df = pd.DataFrame(z_list, columns = ["z"])

    coordinate_df = pd.concat([x_df, y_df, z_df], axis = 1)

    return cut_array(array,coordinate_df,xdim,ydim,zdim), coordinate_df
