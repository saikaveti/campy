from bs4 import BeautifulSoup

import numpy as np
import pandas as pd
import re
import requests

def get_html_table_from_url(url):
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

    return html_table


id = "N00038858"
cycle = 2020

url = "https://www.opensecrets.org/members-of-congress/summary?cid={}&cycle={}".format(id, cycle)

html_table = get_html_table_from_url(url)
print(html_table.prettify())
