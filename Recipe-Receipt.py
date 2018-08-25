import bs4 # parser  
import urllib # downloader 
import requests
import selenium # used to "click" on the print button to open the print page

#find the "print" button on the webpage and open it. the text is now easier 
# to interpt since all of the gibberish is gone.
# download the text as a string and then modify it so that it can be easily 
# printed. 


# will start with budget bytes since it is the recipe website i use the most. 
# unsure how to parse multiple kinds of websites 

def getRecipe(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    elems = soup.select("#recipe-notes > span.recipe-directions--print > a")#css selector 
    print(soup.title)

#def clean(str): # removes all the beginning tags 

    
url = input("imput url")

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
#ingredients = soup.find_all("ul",{"class:","wprm-recipe-ingredients"}) # stored as an array
#elems = soup.select("#wprm-recipe-container > div > div.wprm-recipe-ingredients-container > div > ul") 
#print(ingredients) # will print all of the ingredients sub divided into its seperate  <li> components 
foods = soup.find_all("span",{"class:", "wprm-recipe-ingredient-name"}) #gets the ingredient names 
quantity = soup.find_all("span",{"class:","wprm-recipe-ingredient-amount"})
unit = soup.find_all("span",{"class","wprm-recipe-ingredient-unit"})

print("\n"+soup.title.text+"\n")
print("Ingredients:")



ingredients = ""
for x in range(len(unit)):
    #print(quantity[x].text,unit[x].text,foods[x].text)
    ingredients = ingredients + quantity[x].text +" " +unit[x].text + " " + foods[x].text + "\n"


instruction_list = soup.find_all("div",{"class:","wprm-recipe-instruction-text"})

instructions = ""
for x in range(len(instruction_list)):
    instructions = instructions + str(x + 1) + ": " + instruction_list[x].text + "\n"

print(ingredients)    
print(instructions)






# need to make a dictonary that stores all of the foods and the ingredeints in a list.
# dictonary will hold the ingredient name and its quantity. This will make finding the calories later easier as well

#print(len(ingredients))

