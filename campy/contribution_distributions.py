from bs4 import BeautifulSoup

import numpy as np
import pandas as pd
import time
import re
import requests

def get_source_html_table_from_url(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "lxml")
        body = soup.findAll("body")[0]
        main_div = body.findAll("div", {"class": "Main", "id": "main", "role": "main"})[0]
        main_wrap_div = main_div.findAll("div", {"class": "Main-wrap l-padding u-mt2"})[0]
        l_wrap_div = main_wrap_div.findAll("div", {"class": "l-wrap"})[0]
        l_primary_secondary_div = l_wrap_div.findAll("div", {"class": "l-primary-secondary"})[0]
        l_primary_div = l_primary_secondary_div.findAll("div", {"class": "l-primary"})[0]
        graphic_div = l_primary_div.findAll("div", {"class": "HorizontalStackedBar"})[0]
        stacked_bar_div = graphic_div.findAll("div", {"class": "HorizontalStackedBar--legend u-richtext u-mt4 u-mb4", "style": ""})[0]
        html_table = stacked_bar_div.findAll("table")[0]
        time.sleep(1)
        return html_table
    except:
        return None

def get_pac_html_table_from_url(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "lxml")
        body = soup.findAll("body")[0]
        main_div = body.findAll("div", {"class": "Main", "id": "main", "role": "main"})[0]
        main_wrap_div = main_div.findAll("div", {"class": "Main-wrap l-padding u-mt2"})[0]
        l_wrap_div = main_wrap_div.findAll("div", {"class": "l-wrap"})[0]
        l_primary_secondary_div = l_wrap_div.findAll("div", {"class": "l-secondary-primary"})[0]
        l_primary_div = l_primary_secondary_div.findAll("div", {"class": "l-primary"})[0]
        column_div = l_primary_div.findAll("div", {"class": "u-richtext u-mt4 u-mb4"})[0]
        graphic_div = column_div.findAll("div", {"class": "HorizontalStackedBar"})[0]
        stacked_bar_div = graphic_div.findAll("div", {"class": "HorizontalStackedBar--legend u-richtext u-mt4 u-mb4", "style": ""})[0]
        html_table = stacked_bar_div.findAll("table")[0]
        time.sleep(1)
        return html_table
    except:
        return None

def convert_row(row):
    columns = row.findAll("td")
    row = [None] * 3

    for i in range(len(list(columns))):
        attribute = str(columns[i])
        attribute = re.sub(r'<td(.|\n)*?>', '', attribute)
        attribute = re.sub(r'<\/td>', '', attribute)
        attribute = attribute.strip()
        attribute = attribute.replace("&lt;", "<")
        attribute = attribute.replace("*", "")
        row[i] = attribute

    return row

def source_of_funds_distribution(ids, cycle):
    index = ['Large Individual Contributions', 'Small Individual Contributions (< $200)', 'PAC Contributions', 'Other', 'Candidate self-financing']
    df = pd.DataFrame(index=index, columns=ids.values())
    for id in ids.keys():
        url = "https://www.opensecrets.org/members-of-congress/summary?cid={}&cycle={}".format(id, cycle)
        html_table = get_source_html_table_from_url(url)
        if html_table is None:
            continue
        tbody = html_table.findAll("tbody")[0]
        rows_scrape = html_table.findAll("tr")
        rows_for_id = [convert_row(row) for row in rows_scrape]
        for row in rows_for_id:
            df.at[row[0], ids[id]] = row[1]

    return df

def pac_contribution_distribution(ids, cycle):
    index = ['Labor', 'Business', 'Ideological']
    df = pd.DataFrame(index = index, columns = ids.values())
    for id in ids.keys():
        url = "https://www.opensecrets.org/members-of-congress/pacs?cid={}&cycle={}".format(id, cycle)
        html_table = get_pac_html_table_from_url(url)
        if html_table is None:
            continue
        tbody = html_table.findAll("tbody")[0]
        rows_scrape = html_table.findAll("tr")
        rows_for_id = [convert_row(row) for row in rows_scrape]
        for row in rows_for_id:
            df.at[row[0], ids[id]] = row[1]

    return df
