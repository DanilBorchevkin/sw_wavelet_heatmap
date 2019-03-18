import glob
import numpy as np
import matplotlib.pyplot as plt
from defaultlist import defaultlist

def f(x):
    return (x[:,0]**2 + x[:,1]**2)

def get_graph_from_file(in_folder, in_filename, out_folder, out_filename):
    # Get data
    t, period, wavelet, halfperiod = np.loadtxt(in_folder + "\\" + in_filename, unpack=True)
    
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

    # Create graph
    plt.figure()
    cp = plt.contourf(Z, 1000, cmap='RdGy')
    #cp = plt.pcolor(Z)
    plt.colorbar(cp)
    plt.title('Wavelet Data')
    plt.xlabel('Period, min')
    plt.ylabel('UT')

    # Save graph to file
    plt.show()
    #pass

def main():
    # Only for test
    get_graph_from_file("./input", "mhat2_TEC-wevelet_ONSA_0319_1_12.dat", "./output", "test")
    pass

if __name__ == "__main__":
    main()