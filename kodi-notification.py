#!/usr/bin/env python

import requests
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--message')
parser.add_argument('--title')
args = parser.parse_args()

# Kodi api settings
host = '10.10.10.10'
port = '8080'
user = 'user'
password = 'password'

url = 'http://%s:%s@%s:%s/jsonrpc' % (user, password, host, port)
payload = {"id":1,"jsonrpc":"2.0","method":"GUI.ShowNotification","params":{"title":args.title,"message":args.message}}

r = requests.post(url, data=json.dumps(payload))

