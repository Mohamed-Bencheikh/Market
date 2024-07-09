import json

import requests

region = input("donnez la region >> ")
date = input("Donnez la date >> ")
url = f"https://public.opendatasoft.com/api/records/1.0/search/?dataset=donnees-synop-essentielles-omm&q={region}&q=date%3E%3D%22{date}T23%3A00%3A00Z%22&facet=date&facet=nom&facet=temps_present&facet=libgeo&facet=nom_epci&facet=nom_dept&facet=nom_reg"
data = requests.get(url=url)
meteo = json.loads(data.text)
print(meteo)
