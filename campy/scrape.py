# Scrape together total raised and spent for cycle
from bs4 import BeautifulSoup

import numpy as np
import pandas as pd
import re
import requests

URL_ERROR = "This is an invalid congressional district or senate seat. Must use two letter state abbreviations as well as two digit congressional abbreviations. Senate seats are either S1 and S2."

def get_html_table_from_url(url):
    try:
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
    except:
        raise ValueError(URL_ERROR)

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
            item = strip_tags(i, j, item)
            df.at[i-1, column_names[j]] = item

    return df

def strip_tags(r, c, attribute):
    # Strip the td HTML tags
    attribute = re.sub(r'<td>', '', attribute)
    attribute = re.sub(r'<td(.|\n)*?>', '', attribute)
    attribute = re.sub(r'<\/td>', '', attribute)
    attribute = attribute.strip()

    # Remove information after the candidate name
    attribute = re.sub(r'<a(.|\n)*?>', '', attribute)
    if c == 0:
        attribute = attribute.split(")")[0] + ")"

    return attribute

def summary_data(state, district, cycle):
    url = "https://www.opensecrets.org/races/summary?cycle={}&id={}{}".format(cycle, state, district)
    html_table = get_html_table_from_url(url)
    df = get_df_from_html_table(html_table)

    return df
    
