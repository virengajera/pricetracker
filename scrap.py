#import requests 
from bs4 import BeautifulSoup

def formatPrice(price):
    price = price[:-1]
    #price = price.replace('€','')
    price = price.replace('.','')
    price = price.replace(',','.')
    price = float(price)
    return price

def scrapping(link):

    HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

    webpage = requests.get(link, headers=HEADERS)  
    soup = BeautifulSoup(webpage.content)
    price = soup.find("span", attrs={"class":'a-offscreen'}).text
    print("++++++++",price,type(price))
    final_price = formatPrice(price)
    
    return final_price
