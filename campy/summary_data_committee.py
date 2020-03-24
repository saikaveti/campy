from bs4 import BeautifulSoup

import numpy as np
import pandas as pd
import re
import requests

def get_slab_div(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    body = soup.findAll("body")[0]
    main = soup.findAll("main", {"id": "main"})[0]
    page_div = main.findAll("div", {"class": "u-padding--left u-padding--right tab-interface"})[0]
    data_div = page_div.findAll("div", {"class": "data-container__wrapper"})[0]
    section = data_div.findAll("section", {"id": "section-1", "role": "tabpanel", "aria-labelledby": "section-1-heading"})[0]
    slab_div = section.findAll("div", {"class": "slab slab--inline slab--neutral u-padding--left u-padding--right"})[0]

    return slab_div

def get_total_reciepts_html_table(slab_div):
    entity_div = slab_div.findAll("div", {"class": "entity__figure entity__figure--narrow", "id": "total-raised"})[0]
    figure = entity_div.findAll("figure")[0]
    html_table = figure.findAll("table", {"class": "simple-table"})[0]

    return html_table

def get_total_spent_html_table(slab_div):
    entity_div = slab_div.findAll("div", {"class": "entity__figure entity__figure--narrow", "id": "total-spent"})[0]
    figure = entity_div.findAll("figure")[0]
    html_table = figure.findAll("table", {"class": "simple-table"})[0]

    return html_table

def get_cash_summary_html_table(slab_div):
    entity_div = slab_div.findAll("div", {"class": "entity__figure entity__figure--narrow", "id": "cash-summary"})[0]
    figure = entity_div.findAll("figure")[0]
    html_table = figure.findAll("table", {"class": "simple-table"})[0]

    return html_table

def convert_row(row):
    columns = row.findAll("td")
    row = [None] * 2

    for i in range(len(list(columns))):
        attribute = str(columns[i])
        attribute = re.sub(r'<td(.|\n)*?>', '', attribute)
        attribute = re.sub(r'<\/td>', '', attribute)
        attribute = attribute.strip()
        attribute = re.sub(r'<a(.|\n)*?>', '', attribute)
        attribute = re.sub(r'<\/a>', '', attribute)
        attribute = attribute.strip()
        attribute = re.sub(r'<span(.|\n)*?>', '', attribute)
        attribute = re.sub(r'<\/span>', '', attribute)
        attribute = attribute.strip()
        row[i] = attribute

    return row

def total_reciepts_table(ids, cycle):
    index = ['Total receipts', 'Total contributions', 'Total individual contributions', 'Itemized individual contributions', 'Unitemized individual contributions', 'Party committee contributions', 'Other committee contributions', 'Candidate contributions', 'Transfers from other authorized committees', 'Total loans received', 'Loans made by candidate', 'Other loans', 'Offsets to operating expenditures', 'Other receipts']
    df = pd.DataFrame(index=index, columns=ids)
    for id in ids:
        url = "https://www.fec.gov/data/committee/{}/?cycle={}&election_full=true".format(id, cycle)
        slab_div = get_slab_div(url)
        html_table = get_total_reciepts_html_table(slab_div)
        rows_scrape = html_table.findAll("tr")
        rows_for_id = [convert_row(row) for row in rows_scrape]
        for row in rows_for_id:
            df.at[row[0], id] = row[1]

    return df

def total_spent_table(ids, cycle):
    index = ['Total disbursements', 'Operating expenditures', 'Transfers to other authorized committees', 'Total contribution refunds', 'Individual refunds', 'Political party refunds', 'Other committee refunds', 'Total loan repayments', 'Candidate loan repayments', 'Other loan repayments', 'Other disbursements']
    df = pd.DataFrame(index=index, columns=ids)
    for id in ids:
        url = "https://www.fec.gov/data/committee/{}/?cycle={}&election_full=true".format(id, cycle)
        slab_div = get_slab_div(url)
        html_table = get_total_spent_html_table(slab_div)
        rows_scrape = html_table.findAll("tr")
        rows_for_id = [convert_row(row) for row in rows_scrape]
        for row in rows_for_id:
            df.at[row[0], id] = row[1]

    return df

def cash_summary_table(ids, cycle):
    index = ['Beginning cash on hand', 'Ending cash on hand', 'Debts/loans owed to committee', 'Debts/loans owed by committee']
    df = pd.DataFrame(index=index, columns=ids)
    for id in ids:
        url = "https://www.fec.gov/data/committee/{}/?cycle={}&election_full=true".format(id, cycle)
        slab_div = get_slab_div(url)
        html_table = get_cash_summary_html_table(slab_div)
        rows_scrape = html_table.findAll("tr")
        rows_for_id = [convert_row(row) for row in rows_scrape]
        for row in rows_for_id:
            df.at[row[0], id] = row[1]

    return df
