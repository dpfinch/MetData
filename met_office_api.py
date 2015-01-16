##===========================================================================##
## A program to import Met Office forecast data for a specific location 
##===========================================================================##
## Import Relevant Modules:
import requests
from pprint import pprint
import json
##===========================================================================##
## Set the web address:
url='http://datapoint.metoffice.gov.uk/public/data/'
## Pesonal API key
api_key='&key=8c446f65-ea6a-4e75-afc1-659ca07d99bc'

## To find location id - use following:
##locs='val/wxfcs/all/json/sitelist'
## ID for Edinburgh:
edi_id='351351'


## Other resourses:
cap = 'val/wxfcs/all/json/capabilities?res=3hourly' ## Returns time steps availble
forecast_url = 'val/wxfcs/all/json/'+edi_id+'?res=3hourly' ## Returns forecast

##full_capabil = url+cap+api_key
##met_capabil = requests.get(full_capabil)
##print 'Status code: ', met_capabil.status_code
##
##met_capabil= json.loads(met_capabil.content)

forecast_full = url+forecast_url+api_key
forecast=requests.get(forecast_full)

print'Status code: ', forecast.status_code

forecast=json.loads(forecast.content)
SiteRep = forecast['SiteRep']

wx=SiteRep['Wx']
param = wx['Param']

##===========================================================================##
## END
##===========================================================================##
