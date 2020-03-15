from pycovid import pycovid

pycovid.plot_provinces(countries=['Canada'], 
			provinces=['Alberta', 'Ontario', 'Quebec', 
				'Manitoba', 'British Columbia', 
				'New Brunswick', 'Saskatchewan', 'Nova Scotia'], 
			casetype=['confirmed'], start_date="2020-01-01", plottype="linear")

# pycovid.plot_countries()