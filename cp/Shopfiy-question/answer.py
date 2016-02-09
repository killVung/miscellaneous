from functools import reduce
import pprint
import json

with open('products.json') as data_file:    
    data = json.load(data_file)
    products = data['products']

selects = []
for i in range(len(data['products'])):
    #7 selects suppose
    if ("Wallet" in products[i]['product_type']) or ("Lamp" in products[i]['product_type']):    	    	
        selects.append((data['products'][i]['variants']))
    #dealing with the issues of whether tags don't have the corresponding selects 
    elif ("wallet" in products[i]['title'].lower()) or ("lamp" in products[i]['title'].lower()): 
        selects.append((data['products'][i]['variants']))

#Using reduce to reduce all the list with multiple lists into one big list
final_list = reduce(lambda x,y:x+y,selects) 
prices = [float(final_list[i]["price"]) for i in range(len(final_list)) if final_list[i]["available"] ]

#Using reduce again to summarise the price of the available wallet and lamps items
print(reduce(lambda x,y:x+y,prices))