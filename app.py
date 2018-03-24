__author__='joseph'


# import two packages
import requests
from bs4 import BeautifulSoup

request=requests.get("https://www.johnlewis.com/house-by-john-lewis-curve-dining-chair-white/p231441579#tabinfo-spcl-offr")
content=request.content

soup=BeautifulSoup(content,"html.parser")
# find the right parsed html
element=soup.find("span",{"itemprop":"price","class":"now-price"})

string_price=element.text.strip() #$15.20

# price_without_symbol
price_without_symbol=string_price[1:]





