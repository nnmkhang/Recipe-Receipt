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

if(website == "www.budgetbytes.com"): #budget bytes has very nice HTML making the parsing process very straight foward
    #ingredients = soup.find_all("ul",{"class:","wprm-recipe-ingredients"}) # stored as an array
    #elems = soup.select("#wprm-recipe-container > div > div.wprm-recipe-ingredients-container > div > ul") 
    #print(ingredients) # will print all of the ingredients sub divided into its seperate  <li> components 


    # finds the ul tag containing the ingredients and then cylcecs trough all of the children belongning to the parent tag.
    # in each li tag, the span corrisponding to the name, amount and unit of each ingredient is appended to an array that 
    # stores each respectivly.

    table = soup.find("ul",{"class:","wprm-recipe-ingredients"})
    
    foods = []
    quantity = []
    unit = []   

    for li in table.findChildren("li"):

        amount = li.find("span",{"class:","wprm-recipe-ingredient-amount"})
        if(amount is None):
            quanitiy.append("")
        else:
            quantity.append(amount.text)

        u = li.find("span",{"class:","wprm-recipe-ingredient-unit"}) # u representing unit
        if(u is None):
            unit.append("")
        else:
            unit.append(u.text)


        name = li.find("span",{"class:","wprm-recipe-ingredient-name"})
        if(name is None):
            foods.append("")
        else:
            foods.append(name.text)

   



    print("\n"+soup.title.text+"\n")
    print("Ingredients:")
    
   
   
    for x in range(len(foods)): # puts all of the ingredients into a string
        ingredients = ingredients + quantity[x] + " " + unit[x] + " " + foods[x] + " \n"

    instruction_list = soup.find_all("div",{"class:","wprm-recipe-instruction-text"}) # puts the instructions into a string 
    for x in range(len(instruction_list)): 
        instructions = instructions + str(x + 1) + ": " + instruction_list[x].text + "\n"


elif(website == "www.thecookingguy.com"): # unable to do calories for these dishes becasue the format changes from each recipe
    recipe_div = soup.find("div",{"class:","sqs-block html-block sqs-block-html"})
    #print(recipe_div)

    #finds the ul tag within the larger div tag
    for ingredients_list in recipe_div:
        ingredients_list = recipe_div.find("ul")
        for ingredients_list_entry in ingredients_list:
            ingredients_list_entry = ingredients_list.find_all("li")
        instructions_list = recipe_div.find("ol")
        for instructions_list_entry in instructions_list:
            instructions_list_entry = instructions_list.find_all("li")
    



    unit = []
    foods = []
    quantity = []
    print (soup.title.text)
    for x in range(len(ingredients_list_entry)):
        #print(ingredients_list_entry[x].text)

        quantity.append(ingredients_list_entry[x].text.split(" ",2)[0])
        unit.append(ingredients_list_entry[x].text.split(" ",2)[1])
        foods.append(ingredients_list_entry[x].text.split(" ",2)[2])

    for x in range(len(foods)):
        ingredients = ingredients + quantity[x] + " " + unit[x] + " " + foods[x] + "\n"
    
  
    


    for x in range(len(instructions_list_entry)):
        instructions = instructions + str( x + 1 ) + ": " + instructions_list_entry[x].text + "\n"
    

    

elif(website == "www.allrecipes.com"): # all recipes is nice enough to include the nutritional facts for their recipes '

    nutrition_summary = soup.find("div",{"class:","nutrition-summary-facts"})
    nutrition_entries = nutrition_summary.find_all("span")
    nutrition = ""
    for x in range(len(nutrition_entries)):
        nutrition = nutrition  + nutrition_entries[x].text + " " 
    
    ingredients_list = soup.find_all("li",{"class:","checkList__line"})


    print(nutrition)
    for x in range(len(ingredients_list)-3):
        s = ingredients_list[x].text
        s.replace("\n","")
        ingredients = ingredients + " " + s
    
    instruction_list = soup.find_all("li",{"class:","step"})
    for x in range(len(instruction_list)):
        print(instruction_list[x].text)


print(ingredients)    
print(instructions)

# USDA API KEY GFmojzmt8TKjAQNurSRBZTi1GTkAD2FCkDbliAXY
# EXAMPLE GIVEN: https://developer.nrel.gov/api/alt-fuel-stations/v1/nearest.json?api_key=GFmojzmt8TKjAQNurSRBZTi1GTkAD2FCkDbliAXY&location=Denver+CO
# maybe use an online python library to parse all of the nutrition data from USDA website 
# or u can parse it yourself and learn about JSON files s






# need to make a dictonary that stores all of the foods and the ingredeints in a list.
# dictonary will hold the ingredient name and its quantity. This will make finding the calories later easier as well

#print(len(ingredients))

