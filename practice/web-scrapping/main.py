from bs4 import BeautifulSoup
import requests
import lxml
from lxml import etree

with open('./nse.html', mode='r') as fp:
    soup = BeautifulSoup(fp,'html.parser')

print(soup.div)

url_path = "https://www.moneycontrol.com/techmvc/responsive/fiidii/getFiiDiiMonthly?classic=true&data=cash&mf=01&yf=2022&mt=12&yt=2022"
resp = requests.get(url_path)

#html_content = resp.raw.

# print(resp.content)

# with open('./fii-dii.html', mode='r') as fiidiif:
#     fiisoup = BeautifulSoup(fiidiif,"html.parser")


fiisoup = BeautifulSoup(resp.content,"html.parser")

fii_net_buy_sale_tds = fiisoup.select('tbody tr td:nth-child(4n)')
dii_net_buy_sale_tds = fiisoup.select('tbody tr td:nth-child(7n)')


fii_sum = 0

for item in fii_net_buy_sale_tds:
    amount = float(item.string.replace(',', ''))
    fii_sum = fii_sum + amount
    #print(float(item.string.replace(',', '')))

print(fii_sum)

dii_sum = 0

for item in dii_net_buy_sale_tds:
    amount = float(item.string.replace(',', ''))
    dii_sum = dii_sum + amount
    #print(float(item.string.replace(',', '')))

print(dii_sum)
