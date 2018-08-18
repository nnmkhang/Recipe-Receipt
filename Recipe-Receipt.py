import bs4 # parser  
import urllib # downloader 
import requests
import selenium # used to "click" on the print button to open the print page

#find the "print" button on the webpage and open it. the text is now easier 
# to interpt since all of the gibberish is gone.
# download the text as a string and then modify it so that it can be easily 
# printed. 


def getRecipe(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    elems = soup.select("#recipe-notes > span.recipe-directions--print > a")#css selector 
    print(soup.title)
    
url = input("imput url")
print(url)
getRecipe(url)
