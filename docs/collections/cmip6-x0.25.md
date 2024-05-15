(cmip6-x0.25)=

# CMIP6

Model-based, climate projection data is derived from the Coupled Model Inter-comparison Project-Phase 6 (CMIP6). CMIP is a standard framework for the analysis of coupled atmosphere-ocean general circulation models (GCMs) providing projections of future temperature and precipitation according to designated scenarios. CMIP efforts are overseen by the [World Climate Research Program](https://wcrp-cmip.org/cmip-phase-6-cmip6/), which supports the coordination for the production of global and regional climate model compilations that advance scientific understanding of the multi-scale dynamic interactions between the natural and social systems affecting climate.

CMIP6 projections are shown through five Shared Socioeconomic Pathway (SSPs) Scenarios, designated by total radiative forcing (W/m2) reached by the end of the century. Scenarios are used to represent the climate response to different plausible future societal development storylines and associated contrasting emission pathways to outline how future emissions and land use changes translate into responses in the climate system. These represent possible future greenhouse gas concentration trajectories adopted by the Intergovernmental Panel on Climate Change (IPCC).

CMIP6 global products are downscaled and bias corrected at 0.25-degree, available for 1950-2100

## cmip6-x0.25 Structure

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

### *Collection*

- cmip6-x0.25

### *Variable*

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

### *Product*

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

### *Scenario*

| **Scenario Code** | **Scenario Label** |
| --- | --- |
| ssp126 | SSP1-2.6 |
| ssp245 | SSP2-4.5 |
| ssp370 | SSP3-7.0 |
| ssp585 | SSP5-8.5 |

<br>

### *Aggregation*

| **Aggregation Code** | **Aggregation Label** |
| --- | --- |
| annual | Annual |
| monthly | Monthly |
| seasonal | Seasonal |

<br>

### *Model*

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

### *Time Period*

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

### *Percentile*

| **Percentile Code** | **Percentile Label** |
| --- | --- |
| median | Median or 50th Percentile of the Multi-Model Ensemble |
| p10 | 10th Percentile of the Multi-Model Ensemble |
| p90 | 90th Percentile of the Multi-Model Ensemble |

<br>

### *Product Type*

| **Produce Type Code** | **Product Type Label** |
| --- | --- |
| climatology| climatology |
| heatplot | heatplot |
| timeseries | timeseries |
| timeseries-smooth | Time Series-smooth |

<br>

### *Statistic*

mean; max
