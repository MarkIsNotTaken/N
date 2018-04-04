from bs4 import BeautifulSoup
import urllib2
import datetime

def webScrape(url) :
  webInf = urllib2.urlopen(url)
  resultInf = webInf.read()
  soup = BeautifulSoup(resultInf, "html.parser")
  bitCoinPrice = "$" + soup.find(attrs={"class" : "text-large2"}).get_text()
  currTime = datetime.datetime.now()
  with open("bitcoinprice.txt", "ab") as newFile:
        newFile.write(bitCoinPrice + ", " + str(currTime) + "\n")

webScrape('https://coinmarketcap.com/currencies/bitcoin/')
