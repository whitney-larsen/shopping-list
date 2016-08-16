shopping_list = {"target":["socks","soap","detergent","sponges"]}

def menu():
 #display menu and get choice using raw_input
	choice = int(raw_input("\n0 - Main Menu.\n1 - Show all lists.\n" \
		"2 - Show a specific list.\n3 - Add a new shopping list.\n" \
		"4 - Add an item to a shopping list.\n5 - Remove an item from a shopping list.\n" \
		"6 - Remove a list by nickname.\n7 - Exit when you are done.\n"))
	return choice

def show_all_lists():
#print dictionary with all shopping lists
	print shopping_list.keys()

def show_specific_list(key):
# prompt for nickname and return that list sorted
	print shopping_list[key]

def add_new_list(key):
#create a new key and collect shopping items for new list
	if key not in shopping_list:
		shopping_list[key]=[]
	else:
		print "That list already exists."

def add_item_to_list(key,item):
#prompt for existing list and then add item to that list
	if key in shopping_list:
		shopping_list[key]+= item
	else:
		print "That list does not exist."

def remove_item_from_list(key,item):
#prompt for existing list and exiting item, remove item from list
	if key in shopping_list and item in shopping_list[key]:
		shopping_list[key].remove(item)
	elif key not in shopping_list:
		print "That list does not exist."
	elif item not in shopping_list[key]:
		print "That item is not on that list."

def remove_list(key):
#prompt for existing list, remove list
	if key in shopping_list:
		del shopping_list[key]
	else:
		print "That list does not exist"
	

def main():
	while(True):
		choice=menu()
		if choice==1:
			show_all_lists()
		elif choice==2:
			key=(raw_input("what list do you want to show?")).lower()
			show_specific_list(key)
		elif choice==3:
			key=(raw_input("What is the name of the new list?")).lower()
			add_new_list(key)
		elif choice==4:
			key=(raw_input("What list do you want to add to?")).lower()
			item=(str(raw_input("What item do you want to add to the list?"))).lower()
			add_item_to_list(key,item)
		elif choice ==5:
			key=(raw_input("What list do you want to remove an item from?")).lower()
			item=(str(raw_input("What item do you want to remove from the list?"))).lower()
			remove_item_from_list(key,item)
		elif choice==6:
			key=(raw_input("What list do you want to remove?")).lower()
			remove_list(key)
		elif choice==7:
			break


if __name__ == '__main__':
	main()


# def current_shopping_list():
# 	for item in shopping_list:
# 		print item

# def add_shopping_list():
# 	new_item=raw_input("What do you want to add?").lower()

# 	global shopping_list
# 	if shopping_list.count(new_item) == 0:
# 		shopping_list = shopping_list + [new_item]
# 	else:
# 		print "That item is already on your list."

# 	alphabetical_order()

# def alphabetical_order():
# 	global shopping_list
# 	shopping_list.sort()
# 	current_shopping_list()

# def remove_from_list(): 
# 	remove_item = raw_input("what do you want to remove?").lower() 

# 	if shopping_list.count(remove_item) == 0: 
# 		print "This item is not in your list"
# 	else: 
# 		shopping_list.remove(remove_item)   
		
# 	alphabetical_order()