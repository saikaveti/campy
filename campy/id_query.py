import json
import requests

f = open("./../API_KEY.txt","r")
API_KEY = f.readlines()[0][:-2]

# Retrieves the legislators for the given states in the 115th Congress
def get_ids_for_states(states):
    ids = {}
    for state in states:
        API_CALL = "http://www.opensecrets.org/api/?method=getLegislators&id={}&apikey={}&output=json".format(state, API_KEY)
        page = requests.get(API_CALL)
        content = page.content
        parsed = json.loads(content)
        legislators = parsed["response"]["legislator"]
        #print(legislators)
        for legislator in legislators:
            attributes = legislator["@attributes"]
            #print(json.dumps(attributes, indent=4, sort_keys=True))
            ids[attributes["cid"]] = attributes["firstlast"]

    return ids
