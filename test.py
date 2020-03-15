from pycovid import pycovid


# pycovid.plot_countries_trend(countries=['Iran', 'Italy', 'Spain', 'Portugal', 'Japan', 'Germany', 'Mexico'],
# 			casetype=['confirmed'], start_date="2020-01-01", plottype="linear")

#######crashes 

# pycovid.plot_provinces(country=['Australia'],  
# 			casetype=['confirmed'], start_date="2019-12-01", plottype="log")
# pycovid.plot_provinces(country=['US'],  
# 			casetype=['confirmed'], start_date="2019-12-01", plottype="log")

# ####### dont start at zero

# pycovid.plot_provinces(country=['Canada'],  
# 			casetype=['confirmed'], start_date="2019-12-01", plottype="log")

# pycovid.plot_countries()


# pycovid.plot_provinces(country=['US'], provinces=['Arkansas','Arizona',
# 	'California','Colorado','Connecticut','District of Columbia','Delaware',
# 	'Florida','Georgia','Hawaii','Iowa','Idaho','Illinois','Indiana','Kansas',
# 	'Kentucky','Louisiana','Massachusetts','Maryland','Maine','Michigan','Minnesota',
# 	'Missouri','Mississippi','Montana','North Carolina','North Dakota','Nebraska',
# 	'New Hampshire','New Jersey','New Mexico','Nevada','New York','Ohio','Oklahoma',
# 	'Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota',
# 	'Tennessee','Texas','Utah','Virginia','Vermont','Washington','Wisconsin',
# 	'West Virginia','Wyoming'],
# 			casetype=['confirmed'], start_date="2020-2-26", plottype="linear")

pycovid.plot_provinces(country=['Canada'], 
			provinces=['Alberta', 'Ontario', 'Quebec', 
				'Manitoba', 'British Columbia', 
				'New Brunswick', 'Saskatchewan', 'Nova Scotia'], 
			casetype=['confirmed'], start_date="2020-01-01", plottype="linear")



