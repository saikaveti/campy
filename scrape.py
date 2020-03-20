# Scrape together total raised and spent for cycle
from bs4 import BeautifulSoup

import numpy as np
import pandas as pd
import re
import requests

def get_html_table_from_url(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    main_div = soup.findAll("div", {"class": "Main", "id": "main"})[0]
    main_wrap_div = main_div.findAll("div", {"class": "Main-wrap l-padding u-mt2"})[0]
    l_wrap_div = main_wrap_div.findAll("div", {"class": "l-wrap"})[0]
    l_secondary_primary_div = l_wrap_div.findAll("div", {"class": "l-secondary-primary"})[0]
    l_primary_div = l_secondary_primary_div.findAll("div", {"class": "l-primary"})[0]
    l_rich_text_div = l_primary_div.findAll("div", {"class", "u-richtext u-mt4 u-mb4"})[0]
    html_table = l_rich_text_div.findAll("table", {"class", "DataTable"})[0]

    return html_table

def get_df_from_html_table(html_table):
    tbody = html_table.findAll("tbody")[0]
    tr = html_table.findAll("tr")

    column_names = ['Candidate', 'Raised', 'Spent', 'Cash on Hand', 'Last Report']
    df = pd.DataFrame(columns = column_names)

    for i in range(len(list(tr))):
        row = list(tr)[i]
        columns = row.findAll("td")
        for j in range(len(list(columns))):
            item = str(list(columns)[j])
            item = re.sub(r'<td>', '', item)
            item = re.sub(r'<td(.|\n)*?>', '', item)
            item = re.sub(r'<\/td>', '', item)
            item = item.strip()
            df.at[i-1, column_names[j]] = item

    return df

state = "GA"
district = "07"
cycle = 2020

url = "https://www.opensecrets.org/races/summary?cycle={}&id={}{}".format(cycle, state, district)
print(url)
html_table = get_html_table_from_url(url)
df = get_df_from_html_table(html_table)

print(df)
