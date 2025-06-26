import numpy as np

data_dir = '/Users/rossmcphee/Desktop/CAMELS/CMD/CMD/Data/'

# First read the parameter file, which lists the specific values of each of the 28 parameters that are varied in the 1P set, for each set of 3D simulations. 
# name of the parameter file
fparams = data_dir + 'params_1P_IllustrisTNG.txt'
# read the data
params = np.loadtxt(fparams)

#Name of the file with the 2D maps - it stores 2100 maps of HI = 28 parameters x 5 values in a  x 15 slices
fname=data_dir+'Maps_HI_IllustrisTNG_1P_z=0.00.npy'

#read the data
maps_1p_TNG = np.load(fname)

print(np.shape(maps_1p_TNG)) # this tells us it is a 256x256 2D grid 