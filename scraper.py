import requests
from bs4 import BeautifulSoup
import pandas as pd

# baseurl = "https://www.thewhiskyexchange.com"
# headers = {'User-Agent': 'Chrome/89.0.4389.82'}
# productlinks = []
# for x in range(1, 6):
#     k = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={}&psize=24&sort=pasc'.format(x)).text
#     soup = BeautifulSoup(k, 'html.parser')
#     productlist = soup.find_all("li", {"class": "product-grid__item"})
#     # print(productlist)
#
#     for product in productlist:
#         link = product.find("a", {"class": "product-card"}).get('href')
#         productlinks.append(baseurl + link)
#
# print(productlinks)
# print(len(productlinks))

baseurl = "https://www.flipkart.com"
headers = {'User-Agent': 'Chrome/89.0.4389.82'}  # fake user-agent will be used to access the website
product_links = []
data = []
for x in range(1, 3):
    k = requests.get(
        f'https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=laptop%7CLaptops&requestId=2fe5fb4e-cd11-4786-a6a8-1a48b35cac60&as-backfill=on&page=1').text
    soup = BeautifulSoup(k, 'html.parser')
    for product_list in soup.find_all('div', class_='_13oc-S'):
        product_link = product_list.find('a', class_='_1fQZEK')['href']
        product_links.append(baseurl + product_link)

for link in product_links:
    l = requests.get(link, headers=headers).text
    product_page = BeautifulSoup(l, 'lxml')
    try:
        product_title = product_page.find('h1', class_='yhB1nd').text
        # print(product_title)
    except:
        product_title = None
    try:
        product_price_discounted = product_page.find('div', class_='_30jeq3 _16Jk6d').text
        # print(product_price_discounted)
    except:
        product_price_discounted = None
    product_rating = product_page.find('div', class_='_3LWZlK').text
    try:
        product_price_original = product_page.find('div', class_='_3I9_wc _2p61qe')
        # print(product_price_original)
    except:
        product_price_original = None
    try:
        product_price_discount = product_page.find('div', class_='_3Ay6Sb _31Dcoz').text
        # print(product_price_discount)
    except:
        product_price_discount = None
    product = {"Product Title": product_title, "Product Price": product_price_discounted, "Original Product Price": product_price_original,
               "Discount": product_price_discount, "Product Rating": product_rating, "Product Link": link}
    data.append(product)

df = pd.DataFrame(data)
print(df)
df.to_csv(r'C:\Users\S3883\Desktop\product_lists.csv')
