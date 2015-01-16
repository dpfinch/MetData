##===========================================================================##
## This module will return Met Office data for a specific site input. 
##===========================================================================##
## Import Relevant Modules:
import requests
import json
##===========================================================================##
def forecast_daily(loc):
    '''
    This function pulls down data from the Met Office Datapoints website for daily forecasts. It uses
    an API key and the json function to get the data into a Python Dictionary. The returned data from this
    function will be an array of Met variables (temp etc) by 40 forecasts (8 forecasts per day, 5 days).
    '''
    ## Set the Datapoints web address:
    url='http://datapoint.metoffice.gov.uk/public/data/'
    ## Pesonal API key to access the data (I have previously applied for this API key from the Met Office
    api_key='&key=8c446f65-ea6a-4e75-afc1-659ca07d99bc'
    
    ## Get the location ID for the chosen location. This uses the function 'get_loc_id' to get the 
    
   # loc_id=get_loc_id(loc)
   
    # Test location (Edinburgh)
    edi_id='351351'

    ## Other resourses:
    cap = 'val/wxfcs/all/json/capabilities?res=daily' ## Returns time steps availble
    forecast_url = 'val/wxfcs/all/json/'+edi_id+'?res=daily' ## Returns forecast


    forecast_full = url+forecast_url+api_key
    forecast=requests.get(forecast_full)

    print'Status code: ', forecast.status_code

    forecast=json.loads(forecast.content)
    SiteRep = forecast['SiteRep']

    # We have to go through levels of dictionaries and lists within the pulled data 
    DV=SiteRep['DV']
    #Location specific
    data1 = DV['Location']
    #Forecast for period
    data2 = data1['Period']
    #
    data3= data2['']

    return SiteRep

param = forecast_daily(1)

def get_loc_id(loc):
    '''
    This function will return a Met Office site ID for a given location. This is needed to get the correct 
    '''
    
    ## To find location id - use following:
    ##locs='val/wxfcs/all/json/sitelist'

    return None
##===========================================================================##
## END
##===========================================================================##
