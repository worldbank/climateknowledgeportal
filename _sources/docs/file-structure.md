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

| CODE               | COLLECTION LABEL   |
|--------------------|--------------------|
| {ref}`cmip6-x0.25` | CMIP6 0.25-degree  |
| {ref}`cru-x0.25`   | CRU 0.5-degree     |
| {ref}`era5-x0.25`  | ERA5 0.5-degree    |
| {ref}`pop-x1`      | Population and Poverty |



#### <font color='#c43bc4'>Variable</font>

| CODE       | VARIABLE LABEL |
|------------|----------------|
| `cdd65`    | Cooling Degree Days (ref-65°F) |
| `fd`       | Number of Frost Days (Tmin < 0°C) |
| `hd30`     | Number of Hot Days (Tmax > 30°C) |
| `hd35`     | Number of Hot Days (Tmax > 35°C) |
| `hd40`     | Number of Hot Days (Tmax > 40°C) |
| `hd45`     | Number of Hot Days (Tmax > 45°C) |
| `hdd65`    | Heating degree days (ref-65°F) |
| `id`       | Number of Ice Days (Tmax < 0°C) |
| `pr`       | Precipitation |
| `prpercnt` | Precipitation Percent Change |
| `r20mm`    | Number of Days with Precipitation >20mm |
| `r50mm`    | Number of Days with Precipitation >50mm |
| `rx1day`   | Average Largest 1-Day Precipitation |
| `rx5day`   | Average Largest 5-Day Cumulative Precipitation |
| `sd`       | Number of Summer Days (Tmax > 25°C) |
| `tas`      | Average Mean Surface Air Temperature |
| `tasmax`   | Average Maximum Surface Air Temperature |
| `tasmin`   | Average Minimum Surface Air Temperature |
| `tnn`      | Minimum of Daily Min-Temperature |
| `tr`       | Number of Tropical Nights (T-min > 20°C) |
| `tr23`     | Number of Tropical Nights (T-min > 23°C) |
| `tr26`     | Number of Tropical Nights (T-min > 26°C) |
| `tr29`     | Number of Tropical Nights (T-min > 29°C) |
| `txx`      | Maximum of Daily Max-Temperature |


#### <font color='#803bc4'>Product</font>

| CODE                  | PRODUCT LABEL            | UNIT | DESCRIPTION |
|-----------------------|--------------------------|------|-------------|
| `agepyramid`          | Age Pyramid		       |      | A graphical illustration of the distribution of a population of a country by age groups and sex; it typically takes the shape of a "pyramid" when the population is growing. |
| `anomaly`             | Anomaly                  |      | A departure from the reference value. Using temperature as an example, a positive anomaly indicates that the projected temperature was warmer than the reference value, while a negative anomaly indicates that the projected temperature was cooler than the reference value. |
| `anomalysignificance` | Anomaly Significance     |      ||
| `climatology`	        | Climatology              |      | The calculation of uniform periods, typically 20, 30, 50-years, consisting of annual, seasonal, and monthly, averages of temperature, precipitation, and other climatological variables.|
| `natvar`	            | Natural Variability      |      ||
| `natvarhigh`	        | Natural Variability-high |      ||
| `natvarlow`	        | Natural Variability-low  |      ||
| `trend`	            | Trend                    |      |The detection, estimation and prediction of trends and associated statistical and physical significance are important aspects of understanding climate and changes in climate. Trend is the rate at which change occurs over a time period. The trend may be linear or non-linear. Information on trends are available to aid users in defining climate trends in relation to natural climate variability.|
| `trendconfidence`	    | Trend Confidence         |      ||
| `trendsignificance`   | Trend Significance       |      ||
| `yearofchange`	    | Year of Change           |      | Year of Change represents the statistically significant departure of the selected variable from the historical natural variability bounds due to the emergence of an anthropogenically forced trend. |


 #### <font color='#298929'>Type</font>

| CODE               | TYPE LABEL         |
|--------------------|--------------------|
| `climatology`      | climatology        |
| `heatplot`         | heatplot           |
| `timeseries`       | timeseries         |
| `timeseries-smooth`| Time Series-smooth |


#### <font color='#ff0000'>Percentile</font>

| CODE | PERCENTILE LABEL |
|------|------------------|
| `mean` | Mean |
| `median` | Median or 50th Percentile of the Multi-Model Ensemble |
| `p10` | 10th Percentile of the Multi-Model Ensemble |
| `p90` | 90th Percentile of the Multi-Model Ensemble |

#### <font color='#0080ff'>Time Period</font>

 The time period depends on the collection, type, variable and product.

| TIME PERIOD |
|-------------|
| 1950-2014   |
| 2015-2100   |
| 2020-2039   |
| 2040-2059   |
| 2060-2079   |
| 2080-2099   |

#### Aggregation

| CODE	     | AGGREGATION LABEL |
|------------|-------------------|
| `annual`	 | Annual            |
| `monthly`	 | Monthly           |
| `period`   | Period            |
| `seasonal` | Seasonal          |


#### Scenario

| CODE    | SCENARIO LABEL |
|---------|----------------|
| `historical`| Historical       |
| `ssp119`| SSP1-1.9       |
| `ssp126`| SSP1-2.6       |
| `ssp245`| SSP2-4.5       |
| `ssp370`| SSP3-7.0       |
| `ssp585`| SSP5-8.5       |