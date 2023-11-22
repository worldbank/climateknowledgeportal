# Data and Time Standards

To standardize are three main issues: (1) “name” as well as (2) data “structure” of the time/date variable, and (3) “formatting” to enable systematic identification of specific products:

## Name and Structure

### Timeseries

- Annual, Seasonal, Monthly: “time,lat,lon”

### Climatology / Anomalies / Trends / Trendsignficance / Trendconfidence / Yearofchange

- Annual, Seasonal, Monthly: “time,lat,lon”

### Heatplot

- Monthly:   “time,lat,lon”

## Data Formatting

### Annual (timeseries, climatology)

- Timeseries: (mid-point of each “year”)
  - 1994-07-01 00:00:00, 1995-07-01 00:00:00, …
- Climatology: (mid-point of first “year” or “period” in climatology)
  - 1991-07-01 00:00:00 (for climatology 1991-2020)

### Seasonal (timeseries, climatology)

- Timeseries: (mid-point of each “season” DJF/MAM/JJA/SON)
  - 1994-01-16 00:00:00, 1994-04-16 00:00:00, 1994-07-16 00:00:00, 1994-10-16 00:00:00
  - 1995-01-16 00:00:00, …
- Climatology: (first year of climatology at mid-point of seasons)
  - 1991-01-16 00:00:00, 1991-04-16 00:00:00, 1991-07-16 00:00:00, 1991-10-16 00:00:00

### Monthly (timeseries, climatology, heatplot)

- Timeseries: (mid-point of months)
  - 1994-01-16 00:00:00, 1994-02-16 00:00:00, 1994-03-16 00:00:00, 1994-04-16 00:00:00, …
- Climatology 1991-2020: (first year of climatology at mid-point of month)
  - 1991-01-16 00:00:00, 1991-02-16 00:00:00, 1991-03-16 00:00:00, 1991-04-16 00:00:00, …
- Heatplot: (first year of each decade at mid-points of months)
  - 1901-01-16 00:00:00, 1901-02-16 00:00:00, 1901-03-16 00:00:00, 1901-04-16 00:00:00, …
  - 1911-01-16 00:00:00, 1911-02-16 00:00:00, 1911-03-16 00:00:00, 1911-04-16 00:00:00, …
