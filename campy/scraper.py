from bs4 import BeautifulSoup

import numpy as np
import pandas as pd
import re
import requests

id = "H0MA04192"
cycle = 2020

url = "https://www.fec.gov/data/candidate/{}/?cycle={}&election_full=true".format(id, cycle)

print(url)
print("------------------------------------------------------------------------")

def get_slab_div(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    body = soup.findAll("body")[0]
    main = soup.findAll("main", {"id": "main"})[0]
    page_div = main.findAll("div", {"class": "u-padding--left u-padding--right tab-interface"})[0]
    data_div = page_div.findAll("div", {"class": "data-container__wrapper"})[0]
    main_content_div = data_div.findAll("div", {"class": "main__content--right-full"})[0]
    section = main_content_div.findAll("section", {"id": "section-1", "role": "tabpanel", "aria-labelledby": "section-1-heading"})[0]
    slab_div = section.findAll("div", {"class": "slab slab--inline slab--neutral u-padding--left u-padding--right"})[0]

    return slab_div

def get_total_reciepts_table(slab_div):
    entity_div = slab_div.findAll("div", {"class": "entity__figure entity__figure--narrow", "id": "total-raised"})[0]
    figure = entity_div.findAll("figure")[0]
    html_table = figure.findAll("table", {"class": "simple-table"})[0]

    return html_table

def get_total_spent_table(slab_div):
    entity_div = slab_div.findAll("div", {"class": "entity__figure entity__figure--narrow", "id": "total-spent"})[0]
    figure = entity_div.findAll("figure")[0]
    html_table = figure.findAll("table", {"class": "simple-table"})[0]

    return html_table

def get_cash_summary_table(slab_div):
    entity_div = slab_div.findAll("div", {"class": "entity__figure entity__figure--narrow", "id": "cash-summary"})[0]
    figure = entity_div.findAll("figure")[0]
    html_table = figure.findAll("table", {"class": "simple-table"})[0]

    return html_table

slab_div = get_slab_div(url)
print(get_cash_summary_table(slab_div))
