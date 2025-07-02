import numpy as np
data_dir = '/Users/rossmcphee/Desktop/CAMELS/CMD/CMD/Data/'

def load_params():
    return np.loadtxt(data_dir + 'params_1P_IllustrisTNG.txt')

def load_maps_hi():
    return np.load(data_dir + 'Maps_HI_IllustrisTNG_1P_z=0.00.npy')

def load_maps_mgas():
    return np.load(data_dir + 'Maps_Mgas_IllustrisTNG_1P_z=0.00.npy')

def load_maps_mcdm():
    return np.load(data_dir + 'Maps_Mcdm_IllustrisTNG_1P_z=0.00.npy')

# next add stellar mass, see if it'd be worth it to compare. Computationally may be heavy
# also import MCDM VELOCITIES, make a quiver plot see if itd what we expect.


#print(np.shape(maps_1p_TNG_HI)) # this tells us it is a 256x256 2D grid 
#print(np.shape(maps_1p_TNG_MGAS))

# New addition of M gas to this also, again not completely sure how this pans out
# Seems quite cluttered