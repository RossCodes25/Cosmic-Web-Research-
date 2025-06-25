# Cosmic Web Research
The overlap of gas, dark matter, and galaxy filaments with varying cosmology and AGN feedback. I will be using the public suite of thousands of hydrodynamical simulations via the IllustrisTNG 1P data set.

The CMD is a collection of a 2D or 3D grids of the full snapshot. Whereas in the snapshot we have information for all the particles (their position and properties) in the simulation, in a 3D grid we split the volume in 256^3 cells and record the average or total property of the particles in each cell. Information is here: https://camels-multifield-dataset.readthedocs.io/en/latest/index.html. 

And in particular: https://camels-multifield-dataset.readthedocs.io/en/latest/data.html, this is vital to this work.

The data used is detailed below:

 * **2D map (525MB)**: https://users.flatironinstitute.org/~camels/CMD/2D_maps/data/IllustrisTNG/Maps_HI_IllustrisTNG_1P_z=0.00.npy

 * **Parameter file (32KB)**: https://users.flatironinstitute.org/~camels/CMD/2D_maps/data/IllustrisTNG/params_1P_IllustrisTNG.txt

 The first 2D map file is from the IllustrisTNG 1P dataset.
        - The 1P dataset is used because we can vary both cosmological and astrophysical parameters, whereas with most others you can only vary 1. This will give fantastic insight as to which parameters change the universe the most.
        - In the 1P set, each of the 28 parameters can take 5 values (one varying at a time) so we have a total of 28x5=140 possible combination of parameters. I.e., we have 140 original 3D simulation boxes.
        Each of the 3D simulation boxes is "sliced" into 15 2D maps. So we have 140x15=2100 2D maps of neutral hydrogen map.Each 2D map is stored in a 256x256 grid.
        They are ordered such that each set of 15 2D maps that come from the same 3D simulation are stored consecutively. 

In notebook 1, I investigate nuetral hydrogen H1. 
This involves;
 - Filtering through the parameter set, finding test cases for each parameter. For example, for mass content of universe I will find cases which are different from the fiducial, but the same 2D slice of information.
 - Plots of; test cases, residual graphs, sensitivity plots for each parameter with statistics
 - Analysing and Interpretation of the above graphs, making connections to underlying physical process at play
 - Drawing a conclusion as to which parameter(s) is/are most vital to the cosmic web structure with reference to the voids an filamentary nodes.
