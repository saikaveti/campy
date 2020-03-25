import json
import requests

print("Hello World!")

API_KEY = "d3786a54758c0ad545088af11246d950"
state = "MA"

API_CALL = "http://www.opensecrets.org/api/?method=getLegislators&id={}&apikey={}&output=json".format(state, API_KEY)

page = requests.get(API_CALL)

content = page.content
parsed = json.loads(content)
print(json.dumps(parsed, indent=4, sort_keys=True))
#print(parsed)
