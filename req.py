import requests
import json

URL = 'https://spreadsheets.google.com/feeds/cells/1jD5LHkq_ofs34ovDHxF19aZ8r6ezKri6ms4JjG1zmkg/1/public/full?alt=json'
res = requests.get(URL)
data = res.json()['feed']['entry']
for i in range(0, len(data)):
    title = data[i]['title']['$t']
    content = data[i]['content']['$t']
    print(title, content)
