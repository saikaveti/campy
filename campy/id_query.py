import json
import requests

def get_api_key(file_name):
    f = open(file_name,"r")
    API_KEY = f.readlines()[0][:-1]
    f.close()

    return API_KEY

# Retrieves the legislators for the given states in the 115th Congress
def get_ids_for_states(states):
    ids = {}
    API_KEY = get_api_key("./../API_KEY.txt")
    for state in states:
        API_CALL = "http://www.opensecrets.org/api/?method=getLegislators&id={}&apikey={}&output=json".format(state, API_KEY)
        page = requests.get(API_CALL)
        content = page.content
        parsed = json.loads(content)
        legislators = parsed["response"]["legislator"]
        for legislator in legislators:
            attributes = legislator["@attributes"]
            ids[attributes["cid"]] = attributes["firstlast"]

    return ids
