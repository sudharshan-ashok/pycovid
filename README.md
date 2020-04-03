# PyCOVID Package

The PyCOVID package provides a Pandas Dataframe of the 2019 Novel Coronavirus COVID-19 (2019-nCoV) epidemic based on Rami Krispin's 'coronavirus' package in R. The raw data pulled from the Johns Hopkins University Center for Systems Science and Engineering (JHU CCSE) Coronavirus

<img src="img/covid.jfif" width="100%" align="center"/></a>

## Try in a collaboratory iPython notebook
<a href="https://colab.research.google.com/github/kylemath/pycovid/blob/master/notebooks/PyCovid_Example_Notebook.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg"></a>

### Quick Installation

```py
pip install pycovid
```
### Importing

```py
from pycovid import pycovid
pycovid.getCovidCases()
```

## Value Addition

The 'coronavirus' R package gets access to data, but the 'pyCOVID' package builts some additional functionality over it.

1. Wide Format for quicker analysis (Wide by case type - Confirmed/Death/Recovered)
2. Filtering options - By country, timeline, casetype
3. Cumulative Aggregating options - cumsum parameter to look at the cumulative totals of how the Coronavirus has grown over time
4. Time Resampling: Converts dataframe to time-indexed, and resamples at required time level (weekly, monthly, etc)
5. Quick visualization using Plotly: Use the plotCountries() function


Usage
-----

**getCovidCasesWide()** : Get the wide version of the Coronavirus Dataset
Parameters: 
1. Countries: List of Countries (Default: All Countries)
2. start_date and end_date: Use these to set the time window you wish to access
3. casetype: Python List of Case Types ('confirmed', 'death' and 'recovered' and Default is all) 
4. cumsum: Gets cumulative sums of cases for each country in list (Default: False)

<img src="img/cumsumwide.PNG" width="100%" align="center"/></a>

**getCovidCases()** : Get the Rami Krispin Coronavirus Dataset in the original format
Parameters: 
1. Countries: List of Countries (Default: All Countries)
2. Provinces: List of Provinces and States (Default: All)
3. start_date and end_date: Use these to set the time window you wish to access
4. casetype: Python List of Case Types ('confirmed', 'death' and 'recovered' and Default is all) 
5. cumsum: gets cummulative sum for each country or province
5. plotprovinces: default is false, if True it cumsums over provinces instead of countries

<img src="img/long.PNG" width="100%" align="center"/></a>

**plotCountries()**: Plot the country aggregates on world map using Plotly
Parameters:
1. df: Pass a wide dataframe to the function with country-wise aggregates on confirmed, death and recovered cases
2. grouped_date: Boolean to indicate whether dataset has been aggregated at country level or not
3. metric: Can be 'confirmed' or 'death' or 'recovered'

<img src="img/world.PNG" width="100%" align="center"/></a>

**plot_countries_trend()**: Plot the cummultive trends over time for countries. Currently doesn't work for any countries with provinces/states (US, Canada, Australia, France).
1. countries - list of country names
2. start_date
3. end_date 
4. casetype as above,
5. plottype - linear or log

```py
from pycovid import pycovid

pycovid.plot_countries_trend(countries=['Iran', 'Italy', 'Spain', 'Portugal', 'Japan', 'Germany', 'Mexico'],
			casetype=['confirmed'], start_date="2020-01-01", plottype="linear")
```

**plotProvinces()**: Plot the values from provinces within a country (tested for australia, US, Canada) over time
1. countries - just include one
2. provinces - optional, include names of any states or provinces, otherwise plots all
3. start_date and end_date: as above
4. casetype: as above
5. proportion: default: False, boolean if you want data divided by population
6. cumulative: default: True, if you want data summed over days
7. plottype: "log" or "linear"

```py
from pycovid import pycovid

pycovid.plot_provinces(contries=['Canada'], 
			provinces=['Alberta', 'Ontario', 'Quebec', 
				'Manitoba', 'British Columbia', 
				'New Brunswick', 'Saskatchewan'], 
			casetype=['confirmed'], start_date="2020-02-20", plottype="linear")
```

<img src="img/province.png" width="100%" align="center"/></a>

**getIntervalData()**: Get resampled dataset of the Coronavirus based on the date (by default Monthly level)
1. df: Pass a wide dataframe to the function
2. interval: The time interval you wish to resample the dataset to: 1D = Daily, 1W: Weekly, 1M: Monthly

<img src="img/timeinterval.PNG" width="100%" align="center"/></a>

Installation
------------
```py
pip install pycovid
```
```py
from pycovid import pycovid
pycovid.getCovidCases()
```
or with virtual environment

```bash
# Configure a virtual environment in project directory
python3 -m venv venv 
# Activate the environment (assign paths)
source venv/bin/activate 
# Upgrade Pip and install requirements
pip install --upgrade pip 
pip install pycovid
```

Requirements
------------
Pandas, Numpy and Plotly

Authors
-------
PyCOVID was written by Sudharshan Ashok <sudharshan93@gmail.com>

Licence
-------
MIT License


