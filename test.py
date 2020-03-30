from pycovid import pycovid


# pycovid.plot_countries_trend(countries=['United Kingdom', 'Germany', 'Portugal', 'Bulgaria', 'France', 'Netherlands'],
# 			casetype=['confirmed'], start_date="2020-01-01", plottype="linear")

# pycovid.plot_provinces(country=['China'],  
# 			casetype=['confirmed'], start_date="2019-10-01", plottype="linear",
# 			proportion=True, cumulative=True)
# pycovid.plot_provinces(country=['Australia'],  
# 			casetype=['confirmed'], start_date="2019-12-01", plottype="linear",
# 			proportion=True, cumulative=True)
# pycovid.plot_provinces(country=['US'],  
# 			casetype=['confirmed'], start_date="2019-12-01", plottype="linear",
# 			proportion=True, cumulative=True)
pycovid.plot_provinces(country=['Canada'],  
			casetype=['confirmed'], start_date="2019-12-01", plottype="linear",
			proportion=False, cumulative=True)

pycovid.plot_countries()


