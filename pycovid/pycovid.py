import pandas as pd
import numpy as np
import plotly.express as px

def getCovidCases(countries=None, provinces=None, start_date=None, end_date=None, casetype=['confirmed', 'death', 'recovered'], cumsum=False):
    df = pd.read_csv('https://raw.githubusercontent.com/RamiKrispin/coronavirus-csv/master/coronavirus_dataset.csv',
            names=["province_state", 'country_region', 'lat', 'long', 'date', 'cases', 'type'], skiprows=1, parse_dates=['date'])
    
    df = df[df.type.isin(casetype)]
    
    if start_date is not None:
        df = df[df.date >= start_date]
    if end_date is not None:
        df = df[df.date <= end_date]

    if provinces is not None:
        for province in provinces:
            if province not in df.province_state.values:
                print("Province: {0} not found in database. Check spelling!".format(province))
            df = df[(df.province_state.isin(provinces))] 
            
    if countries is not None:
        for country in countries:
            if country not in df.country_region.values:
                print("Country: {0} not found in database. Check spelling!".format(country))
            df =  df[(df.country_region.isin(countries))]

    if cumsum is True:
        df.cases = df.groupby('province_state')['cases'].transform(pd.Series.cumsum)
            

            
    iso_df = pd.read_csv('https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/slim-3/slim-3.csv')
    iso_df = iso_df[['name', 'alpha-3']]
    iso_df.loc[iso_df.name=="United States of America", 'name'] = 'US'
    iso_df.loc[iso_df.name=="United Kingdom", 'name'] = 'UK'
    iso_df.loc[iso_df.name=="Russian Federation", 'name'] = 'Russia'
    iso_df.loc[iso_df.name=="Korea, Republic of", 'name'] = 'South Korea'
    iso_df.loc[iso_df.name=="Macao", 'name'] = 'Macau'
    iso_df.loc[iso_df.name=="Taiwan, Province of China", 'name'] = 'Taiwan'
    iso_df.loc[iso_df.name=="Viet Nam", 'name'] = 'Vietnam'
    iso_df.loc[iso_df.name=="Iran (Islamic Republic of)", 'name'] = 'Iran'
    iso_df.loc[iso_df.name=="Czechia", 'name'] = 'Czech Republic'
    iso_df.loc[iso_df.name=="Saint Barthélemy", 'name'] = 'Saint Barthelemy'
    iso_df.loc[iso_df.name=="Palestine, State of", 'name'] = 'Palestine'
    iso_df.loc[iso_df.name=="Moldova, Republic of", 'name'] = 'Moldova'
    iso_df.loc[iso_df.name=="Ireland", 'name'] = 'Republic of Ireland'
    iso_df.loc[iso_df.name=="Holy See", 'name'] = 'Vatican City'
               
    df = pd.merge(df, iso_df, left_on="country_region", right_on='name')
    
    return df

def getCovidCasesWide(countries=None, start_date=None, end_date=None, casetype=['confirmed', 'death', 'recovered'], cumsum=False):
    df = pd.read_csv('https://raw.githubusercontent.com/RamiKrispin/coronavirus-csv/master/coronavirus_dataset.csv',
            names=["province_state", 'country_region', 'lat', 'long', 'date', 'cases', 'type'], skiprows=1, parse_dates=['date'])
    
    df = df[df.type.isin(casetype)]
    
    if start_date is not None:
        df = df[df.date >= start_date]
    else:
        if end_date is not None:
            df = df[df.date <= end_date]
    
    if countries is not None:
        for country in countries:
            if country not in df.country_region.values:
                print("Country: {0} not found in database. Check spelling!".format(country))
            df =  df[(df.country_region.isin(countries))]
    
    df = df.pivot_table(index=["date", 'country_region'], columns='type', values='cases', \
                        aggfunc={'date':'first', 'country_region':'first', 'cases':np.sum})\
            .reset_index().fillna(0)
    
    if 'death' not in df.columns:
        df['death'] = 0
    
    if 'recovered' not in df.columns:
        df['recovered'] = 0
        
    df.sort_values(by=['country_region', 'date'], inplace=True)
    
    if cumsum is True:
        df.confirmed = df.groupby('country_region')['confirmed'].transform(pd.Series.cumsum)
        df.recovered = df.groupby('country_region')['recovered'].transform(pd.Series.cumsum)
        df.death = df.groupby('country_region')['death'].transform(pd.Series.cumsum)
        
        

    iso_df = pd.read_csv('https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/slim-3/slim-3.csv')
    iso_df = iso_df[['name', 'alpha-3']]
    iso_df.loc[iso_df.name=="United States of America", 'name'] = 'US'
    iso_df.loc[iso_df.name=="United Kingdom", 'name'] = 'UK'
    iso_df.loc[iso_df.name=="Russian Federation", 'name'] = 'Russia'
    iso_df.loc[iso_df.name=="Korea, Republic of", 'name'] = 'South Korea'
    iso_df.loc[iso_df.name=="Macao", 'name'] = 'Macau'
    iso_df.loc[iso_df.name=="Taiwan, Province of China", 'name'] = 'Taiwan'
    iso_df.loc[iso_df.name=="Viet Nam", 'name'] = 'Vietnam'
    iso_df.loc[iso_df.name=="Iran (Islamic Republic of)", 'name'] = 'Iran'
    iso_df.loc[iso_df.name=="Czechia", 'name'] = 'Czech Republic'
    iso_df.loc[iso_df.name=="Saint Barthélemy", 'name'] = 'Saint Barthelemy'
    iso_df.loc[iso_df.name=="Palestine, State of", 'name'] = 'Palestine'
    iso_df.loc[iso_df.name=="Moldova, Republic of", 'name'] = 'Moldova'
    iso_df.loc[iso_df.name=="Ireland", 'name'] = 'Republic of Ireland'
    iso_df.loc[iso_df.name=="Holy See", 'name'] = 'Vatican City'


    
    df = pd.merge(df, iso_df, left_on="country_region", right_on='name')

    return df

def getIntervalData(df, interval='30D'):
    
    df.index = df.date

    df = df.groupby([pd.Grouper(freq=interval), 'country_region']).sum().reset_index()
    
    return df.sort_values(by=['country_region', 'date'])

def plot_countries(df=None, grouped_data=False, metric="confirmed"):
    
    if df is None:
        df = getCovidCasesWide()
   
    if grouped_data == False:
        df = df.groupby(['country_region', 'alpha-3']).sum().reset_index()
        
    fig = px.choropleth(df, locations="alpha-3",
                    color=metric, # lifeExp is a column of gapminder
                    hover_name="country_region", # column to add to hover information
                    color_continuous_scale="OrRd")
    fig.show()
    

def plot_provinces(countries=None, provinces=None, start_date=None, end_date=None, casetype=['confirmed', 'death', 'recovered'], plottype="linear"):
    
    province_populations = { 'Ontario': 14446515,  
                    'Quebec': 8433301,   
                    'British Columbia': 5020302,   
                    'Alberta': 4345737,   
                    'Manitoba': 1360396,   
                    'Saskatchewan': 1168423,   
                    'Nova Scotia': 965382, 
                    'New Brunswick': 772094, 
                    'Newfoundland': 523790, 
                    'Prince Edward Island': 154748, 
                    'Northwest Territory': 44598,  
                    'Yukon': 40369,  
                    'Nunavut': 38787
                    };



    df = getCovidCases(countries=countries, provinces = provinces, casetype = casetype, start_date=start_date, end_date=end_date, cumsum=True)
    
    if provinces is not None:
        for province in provinces:
            print(province)
            df.loc[df.province_state == province, 'cases'] = (df.loc[df.province_state == province, 'cases'] / province_populations[province]) * 100000
             
    fig = px.line(df, x="date", y="cases", color='province_state', title="Number of confirmed COVID-19 cases over time per 100,000 Canadians")

    fig.update_layout(
        yaxis_title="cases per 100,000 people",
        yaxis = dict(
            showexponent = 'all',
            exponentformat = 'e',
            type = plottype
        ),
        xaxis = {
            'tickformat': '%m-%d',
            'tickmode': 'auto',
            'nticks': 30, 
            'tick0': start_date,
        }
    
    )

    fig.show()

    