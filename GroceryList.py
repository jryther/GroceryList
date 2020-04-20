#Grocery List
#Project 2
#1/29/20

#Bi: Creating dictionaries
grocery_item = {}
#Ai: Creating a list
grocery_history = []

#Looping input to add items to the dictionary
stop = 'c'
#Ciii: While Loop
while stop == 'c':
	#Bii:Adding key-value pairs
	grocery_item = {
	'item_name':input('Item Name:\n'),
	'quantity':input('Quantity purchased:\n'),
	'cost':input('Price per item:\n')
	#Aii: Adding data to a list
	}
	grocery_history.append(grocery_item)
	stop = input(
	'Would you like to enter another item?\n'
	'Type \'c\' for continue or \'q\' to quit:\n'
	)
#Calculate cost of the items purchased and add to grand total
grand_total = 0.00
#Aiii: Accessing values in a list
#Ci: Item-based for loop
for grocery_item in grocery_history:
	item_total = 0
	#Aiv: Modifying values in a list
	#Biii: Accessing values using keys
	#Cii: Index-based for loops
	grocery_name = grocery_item['item_name']
	#Biv: Modifying values
	grocery_price = float(grocery_item['cost'])
	grocery_quantity = int(grocery_item['quantity'])
	item_total = float(grocery_price * grocery_quantity)
	grand_total += float(item_total)
	print('%d %s @ $%.2f ea $%.2f'
	% (grocery_quantity, str(grocery_name), grocery_price, item_total)
	)
print('Grand total: $%.2F' % grand_total)