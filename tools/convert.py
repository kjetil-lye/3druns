

import h5py
import netCDF4

import sys
outname = sys.argv[1].replace('.nc', '.hdf5')
with h5py.File(outname, 'w') as outfile:
    grp = outfile.create_group('CORE')
    with netCDF4.Dataset(sys.argv[1]) as infile:
        for var in infile.variables.keys():
            shape = infile.variables[var].shape
            dset = outfile.create_dataset(var, shape)
            if len(shape) == 1:
                d = infile.variables[var]
                dset[:] = d
            
            elif len(shape) == 2:
                d = infile.variables[var][:,:,0]
                dset[:,:] = d
            else:

                d = infile.variables[var][:,:,:]
                dset[:,:,:] = d
        for attr in infile.ncattrs():
            outfile.attrs[attr] = infile.getncattr(attr)
            
