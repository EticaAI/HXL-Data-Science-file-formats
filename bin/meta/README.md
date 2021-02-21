# About /bin/meta/*

This folder have an very early draft used by
[/bin/hxlquickmeta](../hxlquickmeta).

The idea is eventually abstract more what was bootstraped on
EticaAI-Data_HXL-Data-Science-file-formats
<https://docs.google.com/spreadsheets/d/1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=1066910203>
simmilar to what libraries like Pandas and Numpy do it.

TODO: Look at other abstractions beyond numpy


<!--

> https://numpy.org/doc/stable/user/basics.rec.html
> Users looking to manipulate tabular data, such as stored in csv files, may
find other pydata projects more suitable, such as xarray, pandas, or DataArray.
These provide a high-level interface for tabular data analysis and are better
optimized for that use. For instance, the C-struct-like memory layout of
structured arrays in numpy can lead to poor cache behavior in comparison.


>> https://github.com/pydata/xarray

> Xarray introduces labels in the form of dimensions, coordinates and attributes
on top of raw NumPy-like arrays, which allows for a more intuitive, more
concise, and less error-prone developer experience. The package includes a
large and growing library of domain-agnostic functions for advanced analytics
and visualization with these data structures.

>> Xarray was inspired by and borrows heavily from pandas, the popular data 
analysis package focused on labelled tabular data. It is particularly tailored
to working with netCDF files, which were the source of xarray's data model,
and integrates tightly with dask for parallel computing.

> benchmark https://github.com/pydata/xarray/issues/2799


>> netCDF

- https://www.unidata.ucar.edu/software/netcdf/examples/files.html

-->