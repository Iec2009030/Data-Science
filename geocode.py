
# coding: utf-8


from urllib.request import urlopen
import json

def Revese_geocode_API_json(long,lat):
    address = urlopen("https://maps.googleapis.com/maps/api/geocode/json?latlng="+lat+","+long+ 
                      "&key=AIzaSyDQ8_wgKSuzlJ9Ut8zfC6Rp5HYD-Rg").read().decode('utf-8')
    return(address)
    


long = '-118.283834'
lat = '34.095475'
address = Revese_geocode_API_json(long,lat)
type(address)


json_handle = json.loads(address)
type(json_handle)


print (json_handle['results'][0]['formatted_address'])
print (json_handle['results'][1]['formatted_address'])
print (json_handle['results'][2]['formatted_address'])
print (json_handle['results'][3]['formatted_address'])
print (json_handle['results'][4]['formatted_address'])


address = (json_handle['results'][0]['formatted_address'])
print (address)
print ("Artist Name is: Elliot Smith")




