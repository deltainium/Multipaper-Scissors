# getaddr() function gets the user's public ip address from ipinfo.io
# Code courtesy of pytutorial
# Address is only used internall and will NEVER be sendt to me or any other third party

import requests, json

def getaddr():
    endpoint = 'https://ipinfo.io/json'
    response = requests.get(endpoint, verify = True)
    # Error code handling
    if response.status_code != 200:
        return 'Status:', response.status_code, 'Problem with the request. Exiting.'
        exit()
    # Return ip address field of response.json
    return response.json()['ip']
