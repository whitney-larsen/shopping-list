shopping_list = ["bananas","milk","eggs","sugar","butter"]

def add_shopping_list(shopping_list):
	new_item=raw_input("What do you want to add?").lower()

	if shopping_list.count(new_item) == 0:
		shopping_list = shopping_list + [new_item]
	else:
		print "That item is already on your list."

	alphabetical_order(shopping_list)

def alphabetical_order(shopping_list):
	shopping_list.sort()
	print shopping_list

def remove_from_list(shopping_list): 
	remove_item = raw_input("what do you want to remove?").lower() 

	if shopping_list.count(remove_item) == 0: 
		print "This item is not in your list"
	else: 
		shopping_list.remove(remove_item)   
		
	alphabetical_order(shopping_list)

def main():
	add_shopping_list(shopping_list)
	add_shopping_list(shopping_list)	
	remove_from_list(shopping_list)
	remove_from_list(shopping_list)

if __name__ == '__main__':
	main()
