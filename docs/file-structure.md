
# Climate Change Knowledge Portal File Structure

The collections of WB-CCKP raster data stored under the root AWS S3 bucket `<AWS CLI link TBD>`.  The different collections, their variables and datasets with individual raster products (netCDF files) are organized by a hierarchy of facets that follow this structure:

### Example file: (with ‘..’ representing the root of the CCKP S3 bucket)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ../<font color='#FF0000'>Sub-Level 1</font>/<font color='#ED7D31'>Sub-Level 2</font>/<font color='#FFD966'>Sub-Level 3</font>/Sub-Level 4 (data)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ../<font color='#FF0000'>collection</font>/<font color='#ED7D31'>variable</font>/<font color='#FFD966'>Model</font>-<font color='#C45911'>scenario</font>/filename.nc<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; with filename.nc being:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <font color='#A8D08D'>product</font>-<font color='#ED7D31'>variable</font>-<font color='#B4C6E7'>aggregationperiod</font>-<font color='#4472C4'>statistic</font>\_<font color='#FF0000'>collection</font>\_<font color='#FFC000'>modelwithscenario</font>\_<font color='#538135'>category</font>\_<font color='#404040'>percentile</font>\_<font color='#AEAAAA'>timeperiod</font>.nc

### Sub-Level 1 - Collection

Under the CCKP root, the first level is the level of “Collection” (*cmip6-x0.25*, *era5*, *cru*, …). This represents the fundamental dataset collection. Inside each of these collections, the same structure is offered, albeit with potentially different entries.

### Sub-Level 2 – Variable

The first sub-level is the level of the variable. These are basic climate variables (*tas*, *pr*, …) as well as climate indicators derived from basic variables (*txx*, *rx1day*, *cdd*, *hi35*, …).

### Sub-Level 3 – Dataset

Below each of these “variables” (or indicators), there is the “Dataset”, which represents the source itself. This facet is more granular than the collection, because at this level the different versions and individual simulations are being distinguished. For example, the model *access-cm2* with model simulation variant *r1i1p1f1* for the simulation covering the historical period is an exactly defined, single simulation (one model run). This allows to distinguish this dataset from an entry of *“access-cm2-r2i1p1f1-historical”* (note difference in variant label *r2* vs *r1*). For observational data with evolving versions, the dataset level distinguishes these entries: *cru-ts4.07-historical* is different from *cru-ts4.07-historical*.

### Sub-Level 4 – Data

The final level stores the actual data files where the content is being distinguished in the file naming convention.:

### File Naming Convention

The file names are designed to be self-explanatory, meaning they can be copied somewhere and still retain the full information of the collection, variable and dataset source in addition to the actual content. The facets in the file name are as follows:

### File Naming Convention

The file names are designed to be self-explanatory, meaning they can be copied somewhere and still retain the full information of the collection, variable and dataset source in addition to the actual content. The facets in the file name are as follows:

### Example

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
