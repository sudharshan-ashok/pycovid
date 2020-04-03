import pandas as pd
import numpy as np
import plotly.express as px

def getCovidCases(countries=None, provinces=None, start_date=None, end_date=None, casetype=['confirmed', 'death', 'recovered'], cumsum=False, plotprovinces=False):
    df = pd.read_csv('https://raw.githubusercontent.com/RamiKrispin/coronavirus-csv/master/coronavirus_dataset.csv',
            names=["province_state", 'country_region', 'lat', 'long', 'date', 'cases', 'type'], skiprows=1, parse_dates=['date'])
    
    df = df[df.type.isin(casetype)]
    
    if start_date is not None:
        df = df[df.date >= start_date]
    if end_date is not None:
        df = df[df.date <= end_date]

    if countries is not None:
        for country in countries:
            if country not in df.country_region.values:
                print("Country: {0} not found in database. Check spelling!".format(country))
            df =  df[(df.country_region.isin(countries))]
       
    if cumsum is True:
        if plotprovinces:
            df.cases = df.groupby('province_state')['cases'].transform(pd.Series.cumsum)   
        else: 
            df.cases = df.groupby('country_region')['cases'].transform(pd.Series.cumsum)

    iso_df = getIsoDf()           
    df = pd.merge(df, iso_df, left_on="country_region", right_on='name')
    print(df)
    return df

def getIsoDf():
    iso_df = pd.read_csv('https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/slim-3/slim-3.csv')
    iso_df = iso_df[['name', 'alpha-3']]
    
    iso_df.loc[iso_df.name=="United States of America", 'name'] = 'US'
    iso_df.loc[iso_df.name=="United Kingdom", 'name'] = 'UK'
    iso_df.loc[iso_df.name=="Korea, South", 'name'] = 'South Korea'
    iso_df.loc[iso_df.name=="United Kingdom of Great Britain and Northern Ireland", 'name'] = 'United Kingdom'
    iso_df.loc[iso_df.name=="Russian Federation", 'name'] = 'Russia'
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

    return iso_df    

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
        
    iso_df = getIsoDf()  
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
    
    df['log_confirmed'] = np.log10(df.confirmed)
    fig = px.choropleth(df, locations="alpha-3",
                    color=metric, # lifeExp is a column of gapminder
                    hover_name="country_region", # column to add to hover information
                    color_continuous_scale="OrRd")
    
    fig.update_layout(
        coloraxis_colorbar=dict(
        title='log confirmed',
        exponentformat='none'
        )
    )
    
    fig.show()
    

def plot_countries_trend(countries=None, start_date=None, end_date=None, casetype=['confirmed', 'death', 'recovered'], plottype="linear", cumulative=True):
    
  # load in populations 

    df = getCovidCases(countries=countries,  casetype = casetype, start_date=start_date, end_date=end_date, cumsum=cumulative)

    fig = px.line(df, x="date", y="cases", color='name', title="Number of confirmed COVID-19 cases over time")

    fig.update_layout(
        yaxis_title="cases",
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



def plot_provinces(country=None, provinces=None, start_date=None, end_date=None, casetype=['confirmed', 'death', 'recovered'], proportion=False, cumulative=True, plottype="linear"):
    ylabel = "Cases "
    title = "Number of confirmed COVID-19 cases over time in " + country[0] 

    if plottype == 'linear':
        thisRange = [100, 10000]
    else:
        thisRange = [2, 4]

    df = getCovidCases(countries=country, provinces = provinces, casetype = casetype, start_date=start_date, end_date=end_date, cumsum=cumulative, plotprovinces=True)
    df = df[df.cases > 100]
    df['daysFrom100'] = df['date']

    if provinces is None:
        provinces = np.unique(df.province_state)

    for province in provinces:
        temp =  df.loc[df.province_state == province, 'date'] - df.loc[df.province_state == province, 'date'].iloc[0]    
        temp = temp.astype(int) / 10**9 / 60 / 60 / 24
        df.loc[df.province_state == province, 'daysFrom100'] = temp

    print(df)

    if proportion:
        df_pop = pd.read_csv(country[0] + '_StatePop_19.csv', names=["state", 'population'], skiprows=0)
        province_populations = df_pop.set_index('state').T.to_dict('records')[0]
        ylabel = ylabel + "per 100,000 people"
        title = title + " per 100,000 Citizens"
        for province in provinces:
            df.loc[df.province_state == province, 'cases'] = (df.loc[df.province_state == province, 'cases'] / province_populations[province]) * 100000

    fig = px.line(df, x="daysFrom100", y="cases", color='province_state', title=title)

    for multiple in [1, 2, 3, 5, 7]:
        fig.add_shape(
            type="line",
            x0=0,
            y0=100,
            x1=7*(multiple),
            y1=12800,
            line=dict(
                color="Gray",
                width=2,
                dash="dot",
            )
        )
 
    fig.update_layout(
        yaxis_title=ylabel,
        yaxis = dict(
            showexponent = 'all',
            exponentformat = 'none',
            type = plottype,
            range = thisRange
        ),
        xaxis = {
            'tickmode': 'auto',
            'nticks': 30,
            'range': [0, 20]
        }
    )

    fig.update_shapes(dict(xref='x', yref='y'))
    fig.show()

    