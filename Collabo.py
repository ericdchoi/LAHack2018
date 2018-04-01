import json, requests, foursquare
from urllib.request import urlopen
url = 'https://api.foursquare.com/v2/venues/trending'

def location_lookup():
  try:
    return json.load(urlopen('http://ipinfo.io/json'))
  except urllib2.HTTPError:
    return False
location = location_lookup()

collective_venues = venue_request['venues']
for v in collective_venues:
	print(v['name'])
	print(v['location']['city'])
# print(json.dumps(venue_request, indent=4, sort_keys=True))

params = dict(
  client_id='PHPYTFG0OU3ALNMODYC1X432CCQVOCNGW2GMRQM4JP2WVRZD',
  client_secret='JTLINVTFX3WRRIGESGVNZLXO2GNJ1HLWZN4GOZR52RH5JVQX',
  v='20180323',
  ll = location['loc'],
  radius = '10000',
  section = 'coffee'
)
client = foursquare.Foursquare(client_id = 'PHPYTFG0OU3ALNMODYC1X432CCQVOCNGW2GMRQM4JP2WVRZD', client_secret = 'JTLINVTFX3WRRIGESGVNZLXO2GNJ1HLWZN4GOZR52RH5JVQX')
venue_request = client.venues.search(params={'section':'coffee', 'll':location['loc'],'v':'20180323'})
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
response = data['response']['groups'][0]['items']
# print(response)
# groups 
# print(json.dumps(data, indent=4, sort_keys=True))
# print(location['loc'])
