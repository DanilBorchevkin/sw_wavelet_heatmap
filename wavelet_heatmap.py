import glob
import os
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.ticker as plticker
from matplotlib.ticker import FormatStrFormatter
from defaultlist import defaultlist

def reduce_tick_labels(labels, decreaseEach):
    result = list()
    indexes_list = list()
    i = 1

    for idx, label in enumerate(labels):
        if i == 0:
            result.append(label)
            indexes_list.append(idx)
            i += 1
        elif i == decreaseEach - 1:
            i = 0
        else:
            i += 1
    
    return (result, indexes_list)


def get_graph_from_file(in_filepath, out_folder, out_filename):
    # Get data
    t, period, wavelet, halfperiod = np.loadtxt(in_filepath, unpack=True)
    
    # Prepare data

    # TODO there is some issue
    # In one row - 586 values
    # Overall there are 30 rows
    # So we need create matrix from it data like this
    #Z = [
    #    [0,1,2],
    #    [1,2,3],
    #    [4,5,6]
    #]

    Z = defaultlist(lambda: [])
    current_period = period[0]
    current_row = 0

    for i in range(len(t)):
        if current_period != period[i]:
            current_row += 1
            current_period = period[i]
        Z[current_row].append(wavelet[i])

    
    # ----------------------------------------------

    # Creating X, Y unique values list

    X = t[0 : (len(t) // (current_row + 1)) + 1]

    Y = list()
    myset = set(period)
    for val in myset:
        Y.append("{:d}".format(math.trunc(float(val))))

    # ----------------------------------------------

    # Create graph

    plt.figure(figsize=(6, 3))
    cp = plt.subplot(1, 1, 1)

    # ----------------------------------------------

    # Create contourf graph

    # For change coloring please change cmmap kvar
    cp = plt.contourf(Z, 1000, cmap=cm.gray_r)

    # ----------------------------------------------

    # Set color limits
    
    # Now for color mapping we should strict color limits
    # For get color limits please use cp.get_clim()
    # For set color limits please use cp.set_clim(vmin=<some value>, vmax=<some_value>)
    # If ve set vmin or vmax to None than value will be setup automatically from data
    
    #limits = cp.get_clim()
    #print(limits)
    cp.set_clim(vmin=None, vmax=3000)

    # ----------------------------------------------

    # Show color scale

    plt.colorbar(cp)

    # ----------------------------------------------

    # Setup labels
    plt.title(out_filename)
    plt.xlabel('UT')
    plt.ylabel('Period, min')

    xticks_labels, xticks_indexes = reduce_tick_labels(X, 100)
    yticks_labels, yticks_indexes = reduce_tick_labels(Y, 4)
    plt.xticks(xticks_indexes, xticks_labels, rotation='horizontal')
    plt.yticks(yticks_indexes, yticks_labels)

    plt.locator_params(axis='x', nbins=6)
    # ----------------------------------------------


    # Save graph to file
    plt.tight_layout()
    plt.savefig('{}/{}.png'.format(out_folder, out_filename))

    # ----------------------------------------------

    # or show the graph
    #plt.show()

    # ----------------------------------------------

def get_graph_name_from_filepath(filepath):
    result = ""

    # Get only file name
    result = os.path.basename(filepath)

    # Truncate extension
    result = result[: result.rfind(".")]

    # Truncate all before station name
    result = result[result.find("wevelet_") + len("wevelet_") :]

    # Truncate passage number
    # Some tricky moment we need second from right _
    third_ = result.rfind("_")
    second_ = result.rfind("_", 0, third_) 
    result = result[:second_] + result[third_:]

    return result

def process_all_files_in_folder(in_folder, out_folder):
    for filepath in glob.glob(in_folder + "/" + "*.dat"):
        graph_name = get_graph_name_from_filepath(filepath)
        print(" >>> Process file '{}' with output name '{}'".format(filepath, graph_name))
        get_graph_from_file(filepath, out_folder, graph_name)

def main():
    # Only for test
    #get_graph_from_file("./input", "mhat2_TEC-wevelet_ONSA_0319_1_12.dat", "./output", "test")
    process_all_files_in_folder("./input", "./output")

if __name__ == "__main__":
    main()