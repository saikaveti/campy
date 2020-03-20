# Scrape together total raised and spent for cycle
from bs4 import BeautifulSoup
import requests

state = "GA"
district = "07"
cycle = 2020

url = "https://www.opensecrets.org/races/summary?cycle={}&id={}{}".format(cycle, state, district)

print(url)

page = requests.get(url)
print(page)
print("------------------------------------------")

soup = BeautifulSoup(page.content, "html.parser")
#print(soup.prettify())
#for i in range(len(list(soup.children))):
#    print(i, "           ", list(soup.children)[i])

main = list(soup.children)[21]
#print(main.name, main.class)
#print(main.name == BeautifulSoup.element.Tag)
#for i in range(len(list(main.children))):
    #print(i, "           ", list(main.children)[i])

main_div = soup.findAll("div", {"class": "Main", "id": "main"})[0]
#print(len(main_div))
#for i in range(len(list(main_div))):
#    print(i, "         ", list(main_div)[i])

main_wrap_div = main_div.findAll("div", {"class": "Main-wrap l-padding u-mt2"})[0]
#print(main_wrap_div)
#for i in range(len(list(main_wrap_div))):
    #print(i, "         ", list(main_wrap_div)[i])
l_wrap_div = main_wrap_div.findAll("div", {"class": "l-wrap"})[0]
#print(l_wrap_div)
l_secondary_primary = l_wrap_div.findAll("div", {"class": "l-secondary-primary"})[0]
#for i in range(len(list(l_secondary_primary))):
    #print(i, "         ", list(l_secondary_primary)[i])
l_primary = l_secondary_primary.findAll("div", {"class": "l-primary"})[0]
#print(l_primary)
l_rich_text = l_primary.findAll("div", {"class", "u-richtext u-mt4 u-mb4"})[0]
#print(l_rich_text)
table = l_rich_text.findAll("table", {"class", "DataTable"})
print(table)
# for i in range(len(list(l_padding_div))):
#     print(i, "         ", list(l_padding_div)[i])
#l_wrap_div = l_padding_div.findAll("div", {"class": "l-wrap"})[0]
#print(l_wrap_div)
