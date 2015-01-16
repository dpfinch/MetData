##===========================================================================##
## This module will return Met Office data for a specific site input. 
##===========================================================================##
## Import Relevant Modules:
import requests
import json
import numpy as np
import csv
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
    
    loc_id=get_loc_id(loc)
   
    ## Other resourses:
    forecast_url = 'val/wxfcs/all/json/'+loc_id+'?res=3hourly' ## Returns forecast
    
    forecast_full = url+forecast_url+api_key
    forecast=requests.get(forecast_full)

    #print'Status code: ', forecast.status_code

    forecast=json.loads(forecast.content)
    SiteRep = forecast['SiteRep']

    # We have to go through levels of dictionaries and lists within the pulled data 
    DV=SiteRep['DV']
    #Location specific
    data1 = DV['Location']
    #Forecast for period
    data2 = data1['Period']

    # Find variable names:

    wx = 4

    val_array = np.chararray([11,32],itemsize=4)
    val_array[:] = '-9999'

    count = 0
    var = ['Pp','D','G','F','H','S','U','T','W','V','$']
    for x in range(4):
        
        data3= data2[x]
        data4 = data3['Rep']

        if len(data4) < 8:
            diff = 8 - len(data4)
            count += diff-1
            for  y in range(diff,8):
                count+=1
                
                for v in range(len(data4[y-diff].keys())):
                    val_array[v,count]=str(data4[y-diff][var[v]])

        else:
            for yy in range(8):
                count +=1
                
                for vv in range(len(data4[yy].keys())):
                    val_array[vv,count]=str(data4[yy][var[vv]])
                
        
    return SiteRep
##===========================================================================##

def site_list():
    '''
    This function gets a list of all the ID sites
    '''
    ## Set the Datapoints web address:
    url='http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/sitelist?key='
    ## Pesonal API key to access the data (I have previously applied for this API key from the Met Office
    api_key='&key=8c446f65-ea6a-4e75-afc1-659ca07d99bc'

    full_url = url+api_key

    sitelist = requests.get(full_url)
    sitelist = json.loads(sitelist.content)

    loc = sitelist['Locations']
    sitelist = loc['Location']

    return sitelist

##===========================================================================##

def get_loc_id(location):
    '''
    This function will return a Met Office site ID for a given location. This is needed to get the correct 
    '''
    sitelist = site_list()

    for x in range(len(sitelist)):
        if location == sitelist[x]['name']:
            site_id = sitelist[x]['id']
    print site_id
    return site_id
##===========================================================================##

location_list=[]

in_file = 'location_data.txt'
for line in open(in_file):
                 col = line.split(" ")
                 location_list.append(col[0])

location_list = location_list[2:]

for location in location_list:
    
    data = forecast_daily(location)
    out_file = location+'_.csv'

    with open(out_file,'wb') as f:
        csv.writer(f).writerows(data)
    
##===========================================================================##
## END
##===========================================================================##
