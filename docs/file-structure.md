# Directory Structure and File Name

The [Climate Change Knowledge Portal (CCKP)](https://climateknowledgeportal.worldbank.org) is available as [**netCDF**](https://www.unidata.ucar.edu/software/netcdf) files. A netCDF4 file is structured in a hierarchical directory-like format. It consists of groups, dimensions, variables, and attributes. At the top level, there are groups that act as containers to organize data hierarchically.

The **CCKP netCDF data** directory structure is as follows:

> <font color='#c4c43b'>{collection}</font>/<font color='#c43bc4'>{variable}</font>/<font color='#3bc43b'>{model-run}</font>/{file}.nc

## File Name

The **CCKP netCDF data** filename is as follows:

> <font color='#803bc4'>{product-variable}</font> _ <font color='#c4c43b'>{collection}</font> _ <font color='#3bc43b'>{model-run}</font> _ <font color='#298929'>{type}</font> _ <font color='#ff0000'>{percentile}</font> _ <font color='#0080ff'>{period}</font>.nc
>
For example,

```
./cmip6-x1/tas/access-cm2-r1i1p1f1-historical/climatology-tas-annual-mean_cmip6-x1_access-cm2-r1i1p1f1-historical_climatology_mean_1991-2014.nc
```

### <font color='#c4c43b'>Collection</font>

Click on each collection to learn more about the data available.

| CODE               | COLLECTION LABEL   |
|--------------------|--------------------|
| {ref}`cmip6-x0.25` | CMIP6 0.25-degree  |
| {ref}`cru-x0.25`   | CRU 0.5-degree     |
| {ref}`era5-x0.25`  | ERA5 0.5-degree    |
| {ref}`pop-x1`      | Population and Poverty |
