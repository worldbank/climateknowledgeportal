# World Bank – Climate Change Knowledge Portal Data Collections on AWS

## Overview

The World Bank’s Climate Change Knowledge Portal (CCKP) provides open access to a comprehensive suite of climate and climate change resources derived from the latest generation of climate data archives. Products are based on a consistent and transparent approach with a systematic way of pre-processing the raw observed and model-based projection data to enable inter-comparable use across a broad range of applications. Climate products consist of basic climate variables as well as a large collection (~70+) of more specialized, application-orientated variables and indices across different scenarios. Precomputed data can be extracted per specified variables, select timeframes, climate projection scenarios, as multi-model ensembles or by individual models. CCKP adheres to data distribution standards defined under the Coupled Model Intercomparison Project (CMIP) and its contributions to the Intergovernmental Panel on Climate Change (IPCC) Assessment Reports and latest scientific methodologies identified by the World Meteorological Organization and climate science community.

This data archive consists of global gridded NetCDF files that represent ~35 models, 70+ variables, 5 SSPs, multiple climatology periods, 3 temporal aggregations (annual, seasonal, monthly), plus additional statistics for specific variable presentations.

Climate products are global and are available for the following **collections**:

**cmip6-x0.25:** CMIP6 downscaled, bias corrected 0.25-degree – 1950-2100;<br/>
**era5-x0.25:** EAR5 global 0.25-degree – 1950-2020;<br/>
**cru-x0.5:** CRU global 0.50-degree – 1901-2022;<br/>
**pop-x0.25:** Population global 0.25-degree – 1995-2100 (Gridded Population of the World Version 4).

## Accessing Climate Change Knowledge Portal Data On AWS
You can access these data via the link, `<AWS CLI link TBD>` and using the web interface via the AWS console. To get a list for all variables and climate indicators available for the CMIP6 data at 0.25x0.25 degree resolution, this sub-directory will list them (using the <font color='#E83E8C'>--no-sign-request</font> flag since this bucket is public):

## Climate Change Knowledge Portal File Structure
The collections of WB-CCKP raster data stored under the root AWS S3 bucket `<AWS CLI link TBD>`.  The different collections, their variables and datasets with individual raster products (netCDF files) are organized by a hierarchy of facets that follow this structure:

### Example file: (with ‘..’ representing the root of the CCKP S3 bucket)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ../<font color='#FF0000'>Sub-Level 1</font>/<font color='#ED7D31'>Sub-Level 2</font>/<font color='#FFD966'>Sub-Level 3</font>/Sub-Level 4 (data)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ../<font color='#FF0000'>collection</font>/<font color='#ED7D31'>variable</font>/<font color='#FFD966'>Model</font>-<font color='#C45911'>scenario</font>/filename.nc<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; with filename.nc being:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <font color='#A8D08D'>product</font>-<font color='#ED7D31'>variable</font>-<font color='#B4C6E7'>aggregationperiod</font>-<font color='#4472C4'>statistic</font>\_<font color='#FF0000'>collection</font>\_<font color='#FFC000'>modelwithscenario</font>\_<font color='#538135'>category</font>\_<font color='#404040'>percentile</font>\_<font color='#AEAAAA'>timeperiod</font>.nc

### Sub-Level 1 - Collection:
Under the CCKP root, the first level is the level of “Collection” (*cmip6-x0.25*, *era5*, *cru*, …). This represents the fundamental dataset collection. Inside each of these collections, the same structure is offered, albeit with potentially different entries.

### Sub-Level 2 – Variable:
The first sub-level is the level of the variable. These are basic climate variables (*tas*, *pr*, …) as well as climate indicators derived from basic variables (*txx*, *rx1day*, *cdd*, *hi35*, …).

### Sub-Level 3 – Dataset:
Below each of these “variables” (or indicators), there is the “Dataset”, which represents the source itself. This facet is more granular than the collection, because at this level the different versions and individual simulations are being distinguished. For example, the model *access-cm2* with model simulation variant *r1i1p1f1* for the simulation covering the historical period is an exactly defined, single simulation (one model run). This allows to distinguish this dataset from an entry of *“access-cm2-r2i1p1f1-historical”* (note difference in variant label *r2* vs *r1*). For observational data with evolving versions, the dataset level distinguishes these entries: *cru-ts4.07-historical* is different from *cru-ts4.07-historical*.

### Sub-Level 4 – Data:
The final level stores the actual data files where the content is being distinguished in the file naming convention.:

### File Naming Convention:
The file names are designed to be self-explanatory, meaning they can be copied somewhere and still retain the full information of the collection, variable and dataset source in addition to the actual content. The facets in the file name are as follows:

### File Naming Convention:
The file names are designed to be self-explanatory, meaning they can be copied somewhere and still retain the full information of the collection, variable and dataset source in addition to the actual content. The facets in the file name are as follows:

### Example:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ../<font color='#FF0000'>cmip6-x0.25</font>/<font color='#ED7D31'>tas</font>/<font color='#FFD966'>access-cm2-r1i1p1f1-</font><font color='#C45911'>historical</font>/<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <font color='#A8D08D'>climatology</font>-<font color='#ED7D31'>tas</font>-<font color='#B4C6E7'>annual</font>-<font color='#4472C4'>mean</font>\_<font color='#FF0000'>cmip6-x0.25</font>\_<font color='#FFC000'>access-cm2-r1i1p1f1-historical</font>\_<font color='#538135'>climatology</font>\_<font color='#404040'>mean</font>\_<font color='#AEAAAA'>1995-2014</font>.nc

### <ins> Examples at various sub-levels and facets: </ins>
<font color='#FF0000'>Collection: {cmip6-x0.25,cru-x0.5,era5-x0.25,pop-x1,…}</font><br/>
&nbsp;&nbsp;&nbsp;<font color='#ED7D31'>Variable: {tas,tasmax,tasmin,txx,tnn,…}</font><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#FFD966'>Datasetwithscenario: {ensemble-all-historical, access-cm2-r1i1p1f1-historical…}</font><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#538135'>ProductType: {timeseries,climatology,heatplot}</font><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#A8D08D'>Product: {timeseries,climatology,anomaly,trend,trendsignificance,…}</font><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#B4C6E7'>AggregationPeriod: {annual,seasonal,monthly}</font><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#4472C4'>Statistic: {mean,min,max}</font><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#AEAAAA'>TimePeriod: {1950-2014,2015-2100,2020-2039,….}</font><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#404040'>Percentile: {mean,median,p10,p90,…}</font><br/>

Note, the “scenario”, which is a sub-level of the Dataset, is also a separate facet that can be searched, so that a specific projection scenario can be selected (historical, ssp126, ssp245, …).

### <ins> Priority structure for search: </ins>
<font color='#FF0000'>Collection: {cmip6-x0.25,cru-x0.5,era5-x0.25,pop-x1,…}</font><br/>
&nbsp;&nbsp;&nbsp;<font color='#ED7D31'>Variable: {tas,tasmax,tasmin,txx,tnn,…}</font><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#A8D08D'>Product: {timeseries,climatology,anomaly,trend,…}</font><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#C45911'>Scenario: {historical,ssp119,ssp126,ssp245,ssp370,ssp585}</font><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#B4C6E7'>Aggregation: {annual,seasonal,monthly</font><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#FFD966'>Model including scenario {ensemble-all-historical,access-cm2-r1i1p1f1-ssp126}</font><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#AEAAAA'>TimePeriod: {1950-2014,2015-2100,2020-2039,….}</font><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#404040'>Percentile: {mean,median,p10,p90}</font><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#538135'>ProductType: {timeseries,climatology,heatplot}</font><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#4472C4'>Statistic: {mean,min,max}</font><br/>

### <ins> Single file query example: </ins>
Collection: cmip6-x0.25<br/>
&nbsp;&nbsp;&nbsp;Variable: tas<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Product: trend<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scenario: ssp585<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Aggregation: annual<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Model: ensemble-all<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TimePeriod: 1971-2020<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Percentile: mean<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Product Type: climatology<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Statistic: mean<br/>

## Available Selections Per Each Collection

### CMIP6
Model-based, climate projection data is derived from the Coupled Model Inter-comparison Project-Phase 6 (CMIP6). CMIP is a standard framework for the analysis of coupled atmosphere-ocean general circulation models (GCMs) providing projections of future temperature and precipitation according to designated scenarios. CMIP efforts are overseen by the [World Climate Research Program](https://wcrp-cmip.org/cmip-phase-6-cmip6/), which supports the coordination for the production of global and regional climate model compilations that advance scientific understanding of the multi-scale dynamic interactions between the natural and social systems affecting climate.

CMIP6 projections are shown through five Shared Socioeconomic Pathway (SSPs) Scenarios, designated by total radiative forcing (W/m2) reached by the end of the century. Scenarios are used to represent the climate response to different plausible future societal development storylines and associated contrasting emission pathways to outline how future emissions and land use changes translate into responses in the climate system. These represent possible future greenhouse gas concentration trajectories adopted by the Intergovernmental Panel on Climate Change (IPCC).

CMIP6 products downscaled and bias corrected at 0.25-degree and represent an update from the recent downscaled NEX-GDDP-CMIP6
See for raw data access: https://www.nasa.gov/nasa-earth-exchange-nex/gddp/downscaled-climate-projections-nex-gddp-cmip6/

### cmip6-x0.25 Structure
Collection:<br/>
&nbsp;&nbsp;&nbsp;Variable:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Product:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scenario:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Aggregation:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Model:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TimePeriod:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Percentile:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Product Type:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Statistic:<br/>

*Collection:* cmip6-x0.25:

*Variable:*
| **Variable Code** | **Variable Label** |
| --- | --- |
| cdd65 | Cooling Degree Days (ref-65°F) |
| fd | Number of Frost Days (Tmin < 0°C) |
| hd30 | Number of Hot Days (Tmax > 30°C) |
| hd35 | Number of Hot Days (Tmax > 35°C) |
| hd40 | Number of Hot Days (Tmax > 40°C) |
| hd45 | Number of Hot Days (Tmax > 45°C) |
| hdd65 | Heating degree days (ref-65°F) |
| id | Number of Ice Days (Tmax < 0°C) |
| pr | Precipitation |
| prpercnt | Precipitation Percent Change |
| r20mm | Number of Days with Precipitation >20mm |
| r50mm | Number of Days with Precipitation >50mm |
| rx1day | Average Largest 1-Day Precipitation |
| rx5day | Average Largest 5-Day Cumulative Precipitation |
| sd | Number of Summer Days (Tmax > 25°C) |
| tas | Average Mean Surface Air Temperature |
| tasmax | Average Maximum Surface Air Temperature |
| tasmin | Average Minimum Surface Air Temperature |
| tnn | Minimum of Daily Min-Temperature |
| tr | Number of Tropical Nights (T-min > 20°C) |
| tr23 | Number of Tropical Nights (T-min > 23°C) |
| tr26 | Number of Tropical Nights (T-min > 26°C) |
| tr29 | Number of Tropical Nights (T-min > 29°C) |
| tx84rr | Excess Mortality |
| txx | Maximum of Daily Max-Temperature |

<br>

*Product:*
| **Product Code** | **Produce Label** |
| --- | --- |
| anomaly| Anomaly |
| anomalysignificance | Anomaly Significance |
| climatology | Climatology |
| natvar | Natural Variability |
| natvarhigh | Natural Variability-high |
| natvarlow | Natural Variability-low |
| trend | Trend |
| trendconfidence | Trend Confidence |
| trendsignificance | Trend Significance |
| yearofchange | Year of Change |

<br>

*Scenario:*
| **Scenario Code** | **Scenario Label** |
| --- | --- |
| ssp126 | SSP1-2.6 |
| ssp245 | SSP2-4.5 |
| ssp370 | SSP3-7.0 |
| ssp585 | SSP5-8.5 |

<br>

*Aggregation:*
| **Aggregation Code** | **Aggregation Label** |
| --- | --- |
| annual | Annual |
| monthly | Monthly |
| seasonal | Seasonal |

<br>

*Model:*
| **Model Code** | **Modeling Center** |
| --- | --- |
| access-cm2 | CSIRO (Commonwealth Scientific and Industrial Research Organization, Australia), and ARCCS (Australian Research Council Centre of Excellence for Climate System Science |
| awi-cm-1-1 | Alfred Wegener Institute |
| bcc-csm2-mr | Beijing Climate Center, China Meteorological Administration |
| cams-csm1-0 | Canadian Centre for Climate Modelling and Analysis |
| cmcc-esm2 | Euro-Mediterranean Center on Climate Change |
| cnrm-cm6-1 | Centre National de Recherches Meteorologiques |
| cnrm-esm2-1 | Centre National de Recherches Meteorologiques / Centre Européen de Recherche et Formation Avancées en Calcul Scientifique |
| ec-earth2 | EC-Earth-Consortium |
| ec-earth3-veg | EC-Earth-Consortium |
| ec-earth3-veg-lr | EC-Earth-Consortium |
| fgoals-g3 | China Academy of Sciences |
| gfdl-cm4 | Geophysical Fluid Dynamics Laboratory, NOAA |
| gfdl-esm4 | Geophysical Fluid Dynamics Laboratory, NOAA |
| gfdl-esm5 | Geophysical Fluid Dynamics Laboratory, NOAA |
| hadgem3-gcs1-II | UK Met Office Hadley Centre |
| inm-cm4-8 | Institute for Numerical Mathematics |
| inm-cm5-0 | Institute for Numerical Mathematics |
| ipsl-cm6a-lr | The Institute Pierre Simon Laplace |
| kiost-esm | Korea Institute of Ocean Science and Technology |
| miroc-es2l | Atmosphere and Ocean Research Institute (The University of Tokyo), Center for Climate system Research - National Institute for Environmental Studies |
| mpi-esm1-2hr | Max Planck Institute for Meteorology (MPI-M) |
| mpi-esm1-2-lr | Max Planck Institute for Meteorology (MPI-M) |
| mri-esm2-0 | Meteorological Research Institute |
| nesm3 | Nanjing University of Information Science and Technology |
| noresm2-lm | Norwegian Climate Centre |
| noresm2-mm | Norwegian Climate Centre |
| ukesm1-0-II | National Institute of Meteorological Sciences, Korea |Meteorological Administration-Climate Research Division |
| Ensemble_all | Multi-Model Ensemble |

\*Note: Not all models used in production of every variable, SSP

<br>

*Time Period:*
| **Time Period** |
| --- |
| 1995-2014 |
| 2020-2039 |
| 2040-2059 |
| 2060-2079 |
| 2080-2099 |
| 1950-2014 |
| 2015-2100 |

<br>

*Percentile:*
| **Percentile Code** | **Percentile Label** |
| --- | --- |
| median | Median or 50th Percentile of the Multi-Model Ensemble |
| p10 | 10th Percentile of the Multi-Model Ensemble |
| p90 | 90th Percentile of the Multi-Model Ensemble |

<br>

*Product Type:*
| **Produce Type Code** | **Product Type Label** |
| --- | --- |
| climatology| climatology |
| heatplot | heatplot |
| timeseries | timeseries |
| timeseries-smooth | Time Series-smooth |

<br>

*Statistic:*
mean; max

### ERA5
ERA5 is the fifth generation ECMWF atmospheric reanalysis of the global climate covering the period from January 1950 to present. ERA5 is originally produced by the Copernicus Climate Change Service (C3S) at ECMWF at on original grid of 0.50-degree. ERA5 products derived by CCKP are downscaled and available at 0.25-degree.

### era5-x0.25 Structure
Collection:<br/>
&nbsp;&nbsp;&nbsp;Variable:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Product:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scenario:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Aggregation:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TimePeriod:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Product Type:<br/>

*Collection:* era5-x0.25:

*Variable:*
| **Variable Cove** | **Variable Label** |
| --- | --- |
| fd | Number of Frost Days (Tmin < 0°C) |
| pr | Precipitation |
| rx1day | Average Largest 1-Day Precipitation |
| rx5day | Average Largest 5-Day Cumulative Precipitation |
| tas | Average Mean Surface Air Temperature |
| tasmax | Average Maximum Surface Air Temperature |
| tasmin | Average Minimum Surface Air Temperature |
| tnn | Minimum of Daily Min-Temperature |
| tr | Number of Tropical Nights (T-min > 20°C) |
| txx | Maximum of Daily Max-Temperature |

<br>

*Product:*
| **Product Code** | **Product Label** |
| --- | --- |
| climatology | Climatology |
| trend | Trend |
| trendconfidence | Trend Confidence |
| trendsignificance | Trend Significance |

*Scenario:* historical\_era5

*Aggregation:*
| **Aggregation Code** | **Aggregation Label** |
| --- | --- |
| annual | Annual |
| monthly | Monthly |
| seasonal | Seasonal |

<br>

*TimePeriod:*
| **Time Period** |
| --- |
| 1950-2020 |
| 1991-2020 |
| 1995-2014 |

<br>

*Product Type:*
| **Produce Type Code** | **Product Type Label** |
| --- | --- |
| climatology | climatology |
| heatplot | heatplot |
| timeseries | timeseries |

### CRU_ts4.07
CRU TS (Climatic Research Unit gridded Time Series) is the most widely used observational climate dataset. Data is presented on a 0.5° latitude by 0.5° longitude grid over all land domains except Antarctica. It is derived by the interpolation of monthly climate anomalies from extensive networks of weather station observations. The CRU TS version 4.07 gridded dataset is derived from observational data and provides quality-controlled temperature and rainfall values from thousands of weather stations worldwide, as well as derivative products including monthly climatologies and long term historical climatologies. The dataset is produced by the Climatic Research Unit (CRU) of the University of East Anglia (UEA)

### cru-x0.5 Structure
Collection:<br/>
&nbsp;&nbsp;&nbsp;Variable:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Product:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scenario:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Aggregation:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TimePeriod:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Product Type:<br/>

*Collection:* cru-x0.5:

*Variable:*
| **Variable Code** | **Variable Label** |
| --- | --- |
| pr | Precipitation |
| tas | Average Mean Surface Air Temperature |
| tasmax | Average Maximum Surface Air Temperature |
| tasmin | Average Minimum Surface Air Temperature |

<br>

*Product:*
| **Product Code** | **Product Label** |
| --- | --- |
| climatology | climatology |
| heatplot | heatplot |
| timeseries | timeseries |
| timeseries-smooth | Time Series-smooth |

*Scenario:* historical\_cru\_ts4.07

*Aggregation:*
| **Aggregation Code** | **Aggregation Label** |
| --- | --- |
| annual | Annual |
| monthly | Monthly |
| seasonal | Seasonal |

<br>

*TimePeriod:*
| **Time Period** |
| --- |
| 1901-2022 |
| 1901-1930 |
| 1931-1960 |
| 1961-1990 |
| 1991-2020 |
| 1995-2014 |

<br>

*Product Type:*
| **Product Type Code** | **Product Type Label** |
| --- | --- |
| climatology | climatology |
| heatplot | heatplot |
| timeseries | timeseries |
| timeseries-smooth | Time Series-smooth |

### Pop-x0.25, Population and Poverty
Global population data is produced in line with the socio-economic assumptions for each SSP. Historical population data is derived from the Grided Population of the World-Version 4. Poverty data classifications are derived from the International Poverty Line-Global Subnational Poverty Atlas of the World Bank Data Catalogue.

### pop-x0.25 Structure
Collection:<br/>
&nbsp;&nbsp;&nbsp;Variable:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Product:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scenario:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Aggregation:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TimePeriod:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Product Type:<br/>

*Collection:* pop-x0.25:

*Variable:*
| **Variable Code** | **Variable Label** |
| --- | --- |
| popcount | Population Count |
| popdensity | Population Density (persons/km2) |
| pov190 | Percentage of Population below $1.90/day |
| pov320 | Percentage of Population below $3.20/day |
| pov550 | Percentage of Population below $5.50/day |

<br>

*Product:*
| **Product Code** | **Product Label** |
| --- | --- |
| agepyramid | Age Pyramid |
| climatology | Climatology |
| timeseries | timeseries |

<br>

*Scenario:*
| **Scenario Code** | **Scenario Label** |
| --- | --- |
| historical | Historical |
| ssp119 | SSP1-1.9 |
| ssp126 | SSP1-2.6 |
| ssp245 | SSP2-4.5 |
| ssp370 | SSP3-7.0 |
| ssp585 | SSP5-8.5 |

*Aggregation:* annual

*TimePeriod:*
| **Time Period** |
| --- |
| 1995-2014 |
| 2020-2039 |
| 2040-2059 |
| 2060-2079 |
| 2080-2099 |
| 2010-2100 |

<br>

*Product Type:*
| **Product Type Code** | **Product Type Label** |
| --- | --- |
| climatology | climatology |
| timeseries | timeseries |

## Data Documentation
A detailed documentation of the data content can be found in the CCKP Meta Data Document at: https://climateknowledgeportal.worldbank.org/media/document/metatag.pdf

## Additional Resources
[Climate Change Knowledge Portal](https://climateknowledgeportal.worldbank.org/)<br/>
[Registry of Open Data on AWS](https://registry.opendata.aws/)

## Contributing

Contributions are welcome! If you'd like to contribute, please follow our [contribution guidelines](https://github.com/worldbank/climateknowledgeportal/blob/main/CONTRIBUTING.md).

## License

[This documentation](https://github.com/worldbank/climateknowledgeportal) is licensed under the [**World Bank Master Community License Agreement**](LICENSE).
