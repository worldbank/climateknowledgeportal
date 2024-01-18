(era5-x0.25)=

# ERA5

ERA5 is the fifth generation ECMWF atmospheric reanalysis of the global climate covering the period from January 1950 to 2022. ERA5 is originally produced by the Copernicus Climate Change Service (C3S) at ECMWF at on original grid of 0.50-degree. ERA5 products derived by CCKP are downscaled and available at 0.25-degree.

## era5-x0.25 Structure

Collection:<br/>
&nbsp;&nbsp;&nbsp;Variable:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Product:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scenario:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Aggregation:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TimePeriod:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Product Type:<br/>

### *Collection*

- era5-x0.25

### *Variable*

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

### *Product*

| **Product Code** | **Product Label** |
| --- | --- |
| climatology | Climatology |
| trend | Trend |
| trendconfidence | Trend Confidence |
| trendsignificance | Trend Significance |

### *Scenario*

- historical\_era5

### *Aggregation*

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

### *Product Type*

| **Produce Type Code** | **Product Type Label** |
| --- | --- |
| climatology | climatology |
| heatplot | heatplot |
| timeseries | timeseries |
