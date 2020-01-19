import requests
import http.client
import json


connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': '01372015b43e4930a66e2a7ddb9640db' }
connection.request('GET', '/v2/competitions/CL/matches', None, headers )
response = json.loads(connection.getresponse().read().decode())

print (response)
