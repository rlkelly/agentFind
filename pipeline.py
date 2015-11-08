from urllib2 import urlopen
import json
import pandas as pd

def estateDf(db,address):
	print address
	temp = decodeAddressToCoordinates(address)
	llat, llong = temp['lat'], temp['lng']

	agent_list = []
	print 'part1'

	near_sales = "https://rets.io/api/v1/%s/listings?access_token=c4a90ed28f75dad9d89abb14a51929b9&near=%f,%f&radius=3mi&limit=100" %(db, llat, llong)
	print near_sales

	for each in json.loads(urlopen(near_sales).read())['bundle']:
	    agent_list.append(each['mlsAgentID'])

	print agent_list

	agent_listings = []

	for each in agent_list:
		if db == 'omreb':
			query = "https://rets.io/api/v1/omreb/agents/%s/listings?access_token=c4a90ed28f75dad9d89abb14a51929b9&limit=100" %(each)
		else:
			query = "https://rets.io/api/v1/%s/agents/%s/listings?access_token=c4a90ed28f75dad9d89abb14a51929b9&limit=100" %(db, each)
		try:
			agent_listings.append(json.loads(urlopen(query).read())['bundle'])
		except:
			pass

	print agent_listings

	columns = [u'zipCode', u'roomsTotal', u'bedrooms', u'taxAssessedValue', u'originalPrice', 'closePrice', 'daysOnMarket',  u'baths',  u'price', 'agent', u'squareFootage']
	keys = [u'zipCode', u'roomsTotal', u'squareFootage', u'bedrooms', u'taxAssessedValue', u'originalPrice', 'closePrice', 'daysOnMarket',  u'baths',  u'price']

	print 'part2'

	df = pd.DataFrame(columns = columns)

	for listing in agent_listings:
	    for sale in listing['listings']:
	        new_dict = {"agent":listing['mlsAgentID']}
	        for key in keys:
	            try:
	                new_dict[key] = sale[key]
	            except:
	                print 'fail', key
	                new_dict[key] = None
	        df.loc[len(df)] = pd.Series(new_dict)

	df['percent_over_orig'] = df['closePrice']/df['originalPrice']
	df.percent_over_orig = df.percent_over_orig.astype('float')
	df = df.groupby('agent').mean()
	
	return df.reset_index().to_json(orient='records')

	# df.groupby('agent').mean()

import urllib
import urllib2
import StringIO

def decodeAddressToCoordinates( address ):
        urlParams = {
                'address': address,
                'sensor': 'false',
        }  
        url = 'http://maps.google.com/maps/api/geocode/json?' + urllib.urlencode( urlParams )
        response = urllib2.urlopen( url )
        responseBody = response.read()

        body = StringIO.StringIO( responseBody )
        result = json.load( body )
        if 'status' not in result or result['status'] != 'OK':
                return None
        else:
                return {
                        'lat': result['results'][0]['geometry']['location']['lat'],
                        'lng': result['results'][0]['geometry']['location']['lng']
                }  

def agent_info(number):
	url = "https://rets.io//api/v1/test_sf/agents/%s?access_token=c4a90ed28f75dad9d89abb14a51929b9" %(number)
	url2 = "https://rets.io/api/v1/test_sf/agents/%s/listings?access_token=c4a90ed28f75dad9d89abb14a51929b9&limit=100" %number
	print urlopen(url2)





