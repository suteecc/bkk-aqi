#!/usr/local/bin/python2.7
import requests
from config import *

url="http://api.waqi.info/feed/" + city + "/?token=" + waqi_token
r = requests.get(url)
data = r.json()

def notify(message):
  url = "https://notify-api.line.me/api/notify"
  msg = {"message": message}
  line_headers = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+line_token}
  session = requests.Session()
  resp =session.post(url, headers=line_headers, data=msg)
  print resp.text

if data["data"]["aqi"] > 100:
  message = str(data["data"]["aqi"]) + " Updated on " + data["data"]["time"]["s"]
  print message
  notify(message)

