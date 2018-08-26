import bs4 # parser  
import urllib # downloader 
import requests
import selenium # used to "click" on the print button to open the print page

#find the "print" button on the webpage and open it. the text is now easier 
# to interpt since all of the gibberish is gone.
# download the text as a string and then modify it so that it can be easily 
# printed. 


# will start with budget bytes since it is the recipe website I use the most. 
# unsure how to parse multiple kinds of websites.
# will add allrecipes and sam the cooking guy to this list as well


    
url = input("imput url")
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")

website = url.split("/")[2] # website is the name of the website ex: www.budgetbytes.com
print(website)

ingredients = ""
instructions = ""

if(website == "www.budgetbytes.com"):
    #ingredients = soup.find_all("ul",{"class:","wprm-recipe-ingredients"}) # stored as an array
    #elems = soup.select("#wprm-recipe-container > div > div.wprm-recipe-ingredients-container > div > ul") 
    #print(ingredients) # will print all of the ingredients sub divided into its seperate  <li> components 
    foods = soup.find_all("span",{"class:", "wprm-recipe-ingredient-name"}) #gets the ingredient names 
    quantity = soup.find_all("span",{"class:","wprm-recipe-ingredient-amount"})
    unit = soup.find_all("span",{"class","wprm-recipe-ingredient-unit"})


    print("\n"+soup.title.text+"\n")
    print("Ingredients:")


    for x in range(len(unit)):
        ingredients = ingredients + quantity[x].text +" " +unit[x].text + " " + foods[x].text + "\n"

    instruction_list = soup.find_all("div",{"class:","wprm-recipe-instruction-text"})

    for x in range(len(instruction_list)):
        instructions = instructions + str(x + 1) + ": " + instruction_list[x].text + "\n"

elif(website == "www.thecookingguy.com"):
    recipe_div = soup.find("div",{"class:","sqs-block html-block sqs-block-html"})
    #print(recipe_div)
    for ingredients_list in recipe_div:
        ingredients_list = recipe_div.find("ul")
        for ingredients_list_entry in ingredients_list:
            ingredients_list_entry = ingredients_list.find_all("li")
    




    for x in range(len(ingredients_list_entry)):
        print(ingredients_list_entry[x].text)
        type(ingredients_list_entry[x].text)
        #print(ingredients_list[x].text.split("",2))
   # print(foods)
    #print(len(foods))


elif(website == "www.allrecipes.com"):
    print("test2")

print(ingredients)    
print(instructions)

# USDA API KEY GFmojzmt8TKjAQNurSRBZTi1GTkAD2FCkDbliAXY
# EXAMPLE GIVEN: https://developer.nrel.gov/api/alt-fuel-stations/v1/nearest.json?api_key=GFmojzmt8TKjAQNurSRBZTi1GTkAD2FCkDbliAXY&location=Denver+CO
# maybe use an online python library to parse all of the nutrition data from USDA website 
# or u can parse it yourself and learn about JSON files 






# need to make a dictonary that stores all of the foods and the ingredeints in a list.
# dictonary will hold the ingredient name and its quantity. This will make finding the calories later easier as well

#print(len(ingredients))

