import numpy as np
import pandas as pd
import os
import dicom
import cPickle as pickle
import random

def sample_creator(array_list, patient, test, samplenum, xdim,ydim,zdim):
    """
    insert odd numbered dimensions, will take n-1/2 in each direction

    returns positive_array, negative_array, positive_df, negative_df
    """
    positive_case_list =list()
    positive_case_names = list()
    positive_x = list()
    positive_y = list()
    positive_z = list()


    negative_case_list = list()
    negative_case_names = list()
    negative_x = list()
    negative_y = list()
    negative_z = list()

    arraynum = len(array_list)

    casesnum_pos = samplenum/ arraynum
    casesnum_neg = samplenum/ arraynum

    ## Identify number of nodules per Scan Number
    nodulenum_list = list()
    for i in xrange(len(patient)):
        nodulenum_list.append(len(test[test["Scan Number"] == patient["Patient_ID"].iloc[i]]))

    #return nodulenum_list
    xcut = (xdim -1)/2
    ycut = (ydim - 1)/2
    zcut = (zdim -1)/2


    ## cut arrays

    for num in xrange(arraynum):
        case_counter_pos = 0
        case_counter_neg = 0

        nodulenum = nodulenum_list[num]
        xaxis = array_list[num].shape[0]
        yaxis = array_list[num].shape[1]
        zaxis = array_list[num].shape[2]

        if nodulenum == 1:

            xcoord = float(test[test["Scan Number"] == patient["Patient_ID"].iloc[num]]["nodule_x"])
            ycoord = float(test[test["Scan Number"] == patient["Patient_ID"].iloc[num]]["nodule_y"])
            zcoord = float(test[test["Scan Number"] == patient["Patient_ID"].iloc[num]]["nodule_z"])


            xmin = xcoord - xcut
            xmax = xcoord + xcut
            ymin = ycoord - zcut
            ymax = ycoord + ycut
            zmin = zcoord - zcut
            zmax = zcoord + zcut

            #Collection of Positive Cases
            while case_counter_pos < casesnum_pos:
                xrand = random.randint(xmin,xmax)
                yrand = random.randint(ymin,ymax)
                zrand = random.randint(zmin,zmax)

                xlow = xrand - xcut
                xhigh = xrand + xcut + 1
                ylow = yrand - ycut
                yhigh = yrand + ycut + 1
                zlow = zrand - zcut
                zhigh = zrand + zcut + 1

                positive_case_list.append(array_list[num][xlow:xhigh, ylow:yhigh, zlow:zhigh])
                positive_case_names.append(patient["Patient_ID"].iloc[num])
                positive_x.append(xrand)
                positive_y.append(yrand)
                positive_z.append(zrand)

                case_counter_pos += 1



            #Collection of Negative Cases
            while case_counter_neg < casesnum_neg:
                xhl = random.randint(0,1)
                yhl = random.randint(0,1)
                zhl = random.randint(0,1)

                if xhl == 0:
                    xrand = random.randint(0,xmin-xcut)
                elif xhl == 1:
                    xrand = random.randint(xmax+xcut, xaxis)

                if yhl == 0:
                    yrand = random.randint(0,ymin-ycut)
                elif yhl == 1:
                    yrand = random.randint(ymax+ycut, yaxis)

                if zhl == 0:
                    zrand = random.randint(0,zmin-zcut)
                elif zhl == 1:
                    zrand = random.randint(zmax+zcut, zaxis)

                xlow = xrand - xcut
                xhigh = xrand + xcut + 1
                ylow = yrand - ycut
                yhigh = yrand + ycut + 1
                zlow = zrand - zcut
                zhigh = zrand + zcut + 1

                negative_case_list.append(array_list[num][xlow:xhigh, ylow:yhigh, zlow:zhigh])
                negative_case_names.append(patient["Patient_ID"].iloc[num])
                negative_x.append(xrand)
                negative_y.append(yrand)
                negative_z.append(zrand)

                case_counter_neg += 1

        elif nodulenum ==2:
            nodx = pd.DataFrame(test[test["Scan Number"] == patient["Patient_ID"].iloc[num]]["nodule_x"])
            nody = pd.DataFrame(test[test["Scan Number"] == patient["Patient_ID"].iloc[num]]["nodule_y"])
            nodz = pd.DataFrame(test[test["Scan Number"] == patient["Patient_ID"].iloc[num]]["nodule_z"])

            #resetting index
            newIndexList = [0,1]
            nodx["ni"] = newIndexList
            nody["ni"] = newIndexList
            nodz["ni"] = newIndexList
            nodx = nodx.set_index("ni")
            nody = nody.set_index("ni")
            nodz = nodz.set_index("ni")

            xcoord1 = float(nodx.iloc[0])
            xcoord2 = float(nodx.iloc[1])
            ycoord1 = float(nody.iloc[0])
            ycoord2 = float(nody.iloc[1])
            zcoord1 = float(nodz.iloc[0])
            zcoord2 = float(nodz.iloc[1])

            #Collection of Positive Cases
            while case_counter_pos < casesnum_pos:

                case1or2 = random.randint(1,2)

                if case1or2 == 1:
                    xmin = xcoord1 - xcut
                    xmax = xcoord1 + xcut
                    ymin = ycoord1 - zcut
                    ymax = ycoord1 + ycut
                    zmin = zcoord1 - zcut
                    zmax = zcoord1 + zcut

                    xrand = random.randint(xmin,xmax)
                    yrand = random.randint(ymin,ymax)
                    zrand = random.randint(zmin,zmax)

                    xlow = xrand - xcut
                    xhigh = xrand + xcut + 1
                    ylow = yrand - ycut
                    yhigh = yrand + ycut + 1
                    zlow = zrand - zcut
                    zhigh = zrand + zcut + 1

                    positive_case_list.append(array_list[num][xlow:xhigh, ylow:yhigh, zlow:zhigh])
                    positive_case_names.append(patient["Patient_ID"].iloc[num])
                    positive_x.append(xrand)
                    positive_y.append(yrand)
                    positive_z.append(zrand)

                    case_counter_pos += 1

                elif case1or2 == 2:

                    xmin = xcoord2 - xcut
                    xmax = xcoord2 + xcut
                    ymin = ycoord2 - zcut
                    ymax = ycoord2 + ycut
                    zmin = zcoord2 - zcut
                    zmax = zcoord2 + zcut

                    xrand = random.randint(xmin,xmax)
                    yrand = random.randint(ymin,ymax)
                    zrand = random.randint(zmin,zmax)

                    xlow = xrand - xcut
                    xhigh = xrand + xcut + 1
                    ylow = yrand - ycut
                    yhigh = yrand + ycut + 1
                    zlow = zrand - zcut
                    zhigh = zrand + zcut + 1

                    positive_case_list.append(array_list[num][xlow:xhigh, ylow:yhigh, zlow:zhigh])
                    positive_case_names.append(patient["Patient_ID"].iloc[num])
                    positive_x.append(xrand)
                    positive_y.append(yrand)
                    positive_z.append(zrand)

                    case_counter_pos += 1

            while case_counter_neg < casesnum_neg:

                case1or2 = random.randint(1,2)

                if case1or2 == 1:
                    xmin = xcoord1 - xcut
                    xmax = xcoord1 + xcut
                    ymin = ycoord1 - zcut
                    ymax = ycoord1 + ycut
                    zmin = zcoord1 - zcut
                    zmax = zcoord1 + zcut

                    xhl = random.randint(0,1)
                    yhl = random.randint(0,1)
                    zhl = random.randint(0,1)

                    if xhl == 0:
                        xrand = random.randint(0,xmin-xcut)
                    elif xhl == 1:
                        xrand = random.randint(xmax+xcut, xaxis)

                    if yhl == 0:
                        yrand = random.randint(0,ymin-ycut)
                    elif yhl == 1:
                        yrand = random.randint(ymax+ycut, yaxis)

                    if zhl == 0:
                        zrand = random.randint(0,zmin-zcut)
                    elif zhl == 1:
                        zrand = random.randint(zmax+zcut, zaxis)

                    xlow = xrand - xcut
                    xhigh = xrand + xcut + 1
                    ylow = yrand - ycut
                    yhigh = yrand + ycut + 1
                    zlow = zrand - zcut
                    zhigh = zrand + zcut + 1

                    negative_case_list.append(array_list[num][xlow:xhigh, ylow:yhigh, zlow:zhigh])
                    negative_case_names.append(patient["Patient_ID"].iloc[num])
                    negative_x.append(xrand)
                    negative_y.append(yrand)
                    negative_z.append(zrand)

                    case_counter_neg += 1

                elif case1or2 == 2:
                    xmin = xcoord2 - xcut
                    xmax = xcoord2 + xcut
                    ymin = ycoord2 - zcut
                    ymax = ycoord2 + ycut
                    zmin = zcoord2 - zcut
                    zmax = zcoord2 + zcut

                    xhl = random.randint(0,1)
                    yhl = random.randint(0,1)
                    zhl = random.randint(0,1)

                    if xhl == 0:
                        xrand = random.randint(0,xmin-xcut)
                    elif xhl == 1:
                        xrand = random.randint(xmax+xcut, xaxis)

                    if yhl == 0:
                        yrand = random.randint(0,ymin-ycut)
                    elif yhl == 1:
                        yrand = random.randint(ymax+ycut, yaxis)

                    if zhl == 0:
                        zrand = random.randint(0,zmin-zcut)
                    elif zhl == 1:
                        zrand = random.randint(zmax+zcut, zaxis)

                    xlow = xrand - xcut
                    xhigh = xrand + xcut + 1
                    ylow = yrand - ycut
                    yhigh = yrand + ycut + 1
                    zlow = zrand - zcut
                    zhigh = zrand + zcut + 1

                    negative_case_list.append(array_list[num][xlow:xhigh, ylow:yhigh, zlow:zhigh])
                    negative_case_names.append(patient["Patient_ID"].iloc[num])
                    negative_x.append(xrand)
                    negative_y.append(yrand)
                    negative_z.append(zrand)

                    case_counter_neg += 1

    positive_array = np.zeros([len(positive_case_list), positive_case_list[0].shape[2], positive_case_list[0].shape[0],positive_case_list[0].shape[1]])
    for i in xrange(len(positive_case_list)):
        for j in xrange(positive_case_list[i].shape[0]):
            for k in xrange(positive_case_list[i].shape[1]):
                for l in xrange(positive_case_list[i].shape[2]):
                    positive_array[i,l,j,k] = positive_case_list[i][j,k,l]

    negative_array = np.zeros([len(negative_case_list), negative_case_list[0].shape[2], negative_case_list[0].shape[0],negative_case_list[0].shape[1]])
    for i in xrange(len(negative_case_list)):
        for j in xrange(negative_case_list[i].shape[0]):
            for k in xrange(negative_case_list[i].shape[1]):
                for l in xrange(negative_case_list[i].shape[2]):
                    negative_array[i,l,j,k] = negative_case_list[i][j,k,l]
    positive_df = pd.DataFrame({"Patient_ID": positive_case_names, "X":positive_x, "Y" : positive_y, "Z": positive_z})
    negative_df = pd.DataFrame({"Patient_ID": negative_case_names, "X":negative_x, "Y" : negative_y, "Z": negative_z})


    return positive_array, negative_array, positive_df, negative_df
