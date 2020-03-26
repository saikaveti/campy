import sys
sys.path.append("..")

from itertools import islice

from campy.id_query import get_ids_for_states
from campy.contribution_distributions import source_of_funds_distribution, pac_contribution_distribution

import numpy as np
import pandas as pd

import json
import requests

house_ideology_df = pd.read_csv("./csv-files/govtrack-stats-2018-house-ideology.csv")
senate_ideology_df = pd.read_csv("./csv-files/govtrack-stats-2018-senate-ideology.csv")

f = open('result.json')
ids = json.load(f)

n_items = take(3, ids.iteritems())
print(n_items)
print(source_of_funds_distribution(ids, 2018))


#source_of_funds_df = source_of_funds_distribution(ids, 2018)
