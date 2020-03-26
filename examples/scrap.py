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

source_of_funds_df = pd.read_csv("./csv-files/source-of-funds.csv")
pac_contribution_distribution_df = pd.read_csv("./csv-files/pac-contribution-distributions.csv")

source_of_funds_df = source_of_funds_df.dropna(axis=1, how='all')
pac_contribution_distribution_df = pac_contribution_distribution_df.dropna(axis=1, how='all')

source_of_funds_df[source_of_funds_df.columns[1:]]  \
    = source_of_funds_df[source_of_funds_df.columns[1:]].replace('[\$,]', '', regex=True).astype(float)

pac_contribution_distribution_df[pac_contribution_distribution_df.columns[1:]]  \
    = pac_contribution_distribution_df[pac_contribution_distribution_df.columns[1:]].replace('[\$,]', '', regex=True).astype(float)

source_of_funds_df[source_of_funds_df.columns[1:]] \
    = source_of_funds_df[source_of_funds_df.columns[1:]].div(source_of_funds_df[source_of_funds_df.columns[1:]].sum(axis=0), axis=1)
pac_contribution_distribution_df[pac_contribution_distribution_df.columns[1:]] \
    = pac_contribution_distribution_df[pac_contribution_distribution_df.columns[1:]].div(pac_contribution_distribution_df[pac_contribution_distribution_df.columns[1:]].sum(axis=0), axis=1)

source_of_funds_df = source_of_funds_df.T
pac_contribution_distribution_df = pac_contribution_distribution_df.T

source_of_funds_df = source_of_funds_df[1:]
pac_contribution_distribution_df = pac_contribution_distribution_df[1:]

combined = pd.merge(source_of_funds_df, pac_contribution_distribution_df, left_index=True, right_index=True)
combined.columns = ['Large Individual Contributions', 'Small Individual Contributions (< $200)', 'PAC Contributions', 'Other', 'Candidate self-financing', 'Labor', 'Business', 'Ideological']

combined.to_csv("./csv-files/combined-contribution.csv")
