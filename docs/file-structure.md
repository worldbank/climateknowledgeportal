# Directory Structure and File Name

The [Climate Change Knowledge Portal (CCKP)](https://climateknowledgeportal.worldbank.org) is available as [**netCDF**](https://www.unidata.ucar.edu/software/netcdf) files.
A netCDF4 file is structured in a hierarchical directory-like format.
It consists of groups, dimensions, variables, and attributes. At the top level, there are groups that act as containers to organize data hierarchically.
The CCKP netCDF data structures are described for each collection in the following sections.

| COLLECTION LABEL   | FILE STRUCTURE | EXAMPLE |
|--------------------|----------------|---------|
| CMIP6 0.25-degree  | [](./collections/cmip6-x0.25.md) | [](../notebooks/cmip6-x0.25.ipynb) |
| CRU 0.5-degree     | [](./collections/cru-x0.5.md) | [](../notebooks/cru-x0.5.ipynb) |
| ERA5 0.5-degree    | [](./collections/era5-x0.5.md) | [](../notebooks/era5-x0.5.ipynb) |
| Population and Poverty | [](./collections/pop-x1.md) | [](../notebooks/pop-x1.ipynb) |


An example of a file path is:

```
./cmip6-x1/tas/access-cm2-r1i1p1f1-historical/climatology-tas-annual-mean_cmip6-x1_access-cm2-r1i1p1f1-historical_climatology_mean_1991-2014.nc
```