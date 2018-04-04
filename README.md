# Description:
webscrape.py uses multiple libraries to acquire the html of any website provided.

# How to use it:
Inside of webscrape.py, there is a function called webScrape with a parameter called url. 

```
def webScrape(url) :
```

The html file of any website that is passed within this parameter, which is to be in a string, will be retrieved and made interactible through the soup variable. The urlopen method of urllib will first be used to 'open' the website. After this, it takes the result of that and makes it human readable through the read() method. The html file is now readable, but it can't be interacted with due to it being just text. Using BeautifulSoup's html parser, it can convert into something that can be manipulated through python.

```
webInf = urllib2.urlopen(url)
resultInf = webInf.read()
BeautifulSoup(resultInf, "html.parser")
```

For example, I had use the url of the bitcoin market price. Because BeautifulSoup converted it into html, I could find the current price of Bitcoin and write it into a txt file. With the help of the datetime module, I had also added the exact date and time the info was pulled.

```
bitCoinPrice = "$" + soup.find(attrs={"class" : "text-large2"}).get_text()
currTime = datetime.datetime.now()
with open("bitcoinprice.txt", "ab") as newFile:
        newFile.write(bitCoinPrice + ", " + str(currTime) + "\n")
```

# Libraries Used:
- BeautifulSoup
- urllib2
- datetime
