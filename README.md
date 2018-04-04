#Description:
  It uses multiple libraries to pull down the html file of whatever url is passed within the webScrape function. The code within webscaper.py is retrieving the bitcoin market price from the stock market. 
 
#How it works:
  Inside of webscrape.py, there is a function called webScrape with a parameter called url. The html file of any website that is passed within this parameter, which is to be in a string, will be retrieved and made interactible through the soup variable. As can be seen within webscraper.py, I had used soup to get the current market price of bitcoin along with the exact date and time when it was checked.
  
  EX. webScrape("google.com")
  
#Libraries Used:
  BeautifulSoup
  urllib2
  datetime
