import sys
sys.path.append("..")

from campy.id_query import get_ids_for_states
from campy.contribution_distributions import source_of_funds_distribution, pac_contribution_distribution

import numpy as np
import pandas as pd

import json
import requests

house_ideology_df = pd.read_csv("./csv-files/govtrack-stats-2018-house-ideology.csv")
senate_ideology_df = pd.read_csv("./csv-files/govtrack-stats-2018-senate-ideology.csv")

f = open('congress-115.json')
ids = json.load(f)

# source_of_funds_df = source_of_funds_distribution(ids, 2018)
# source_of_funds_df.to_csv("source-of-funds.csv")
# print("Complete Source of Funds")
pac_contribution_distribution_df = pac_contribution_distribution(ids, 2018)
pac_contribution_distribution_df.to_csv("pac-contribution-distributions.csv")
print(pac_contribution_distribution_df)
print("Complete PAC Contribution Distributions")

# source_of_funds_df = pd.read_csv("source-of-funds.csv")
# pac_contribution_distribution_df = pd.read_csv("pac-contribution-distributions.csv")
#
# source_of_funds_df = source_of_funds_df.dropna(axis=1, how='all')
# pac_contribution_distribution_df = pac_contribution_distribution_df.dropna(axis=1, how='all')
#
# print(source_of_funds_df)
# print(pac_contribution_distribution_df)
