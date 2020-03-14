from pycovid import pycovid

pycovid.plot_provinces(contries=['Canada'], 
						provinces=['Alberta', 'Ontario', 'Quebec', 
								'Manitoba', 'British Columbia', 
								'New Brunswick', 'Saskatchewan'], 
						casetype=['confirmed'], start_date="2020-02-20")