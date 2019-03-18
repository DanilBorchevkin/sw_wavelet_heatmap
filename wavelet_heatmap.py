import glob
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x[:,0]**2 + x[:,1]**2)

def get_graph_from_file(in_folder, in_filename, out_folder, out_filename):
    # Get data
    t, period, wavelet, halfperiod = np.loadtxt(in_folder + "\\" + in_filename, unpack=True)
    
    # Prepare data
    # TODO there is some issue

    # Create graph
    plt.figure()
    cp = plt.contourf(X, Y, Z)
    #cp = plt.pcolor(X, Y, Z)
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