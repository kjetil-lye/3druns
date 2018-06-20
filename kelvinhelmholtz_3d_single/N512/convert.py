import netCDF4
import h5py

import sys

with netCDF4.Dataset(sys.argv[1]) as f:
    for k in f.variables.keys():
        d = f.variables[k]
        with h5py.File(sys.argv[1].replace('.nc', '.h5')) as fout:
            q = fout.create_dataset(k, data=d)
