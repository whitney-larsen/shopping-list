shopping_list = ["bananas","milk","eggs","sugar","butter"]

def current_shopping_list():
	for item in shopping_list:
		print item

def add_shopping_list():
	new_item=raw_input("What do you want to add?").lower()

	global shopping_list
	if shopping_list.count(new_item) == 0:
		shopping_list = shopping_list + [new_item]
	else:
		print "That item is already on your list."

	alphabetical_order()

def alphabetical_order():
	global shopping_list
	shopping_list.sort()
	current_shopping_list()

def remove_from_list(): 
	remove_item = raw_input("what do you want to remove?").lower() 

	if shopping_list.count(remove_item) == 0: 
		print "This item is not in your list"
	else: 
		shopping_list.remove(remove_item)   
		
	alphabetical_order()

def menu():
	choice = int(raw_input("0 - Exit the program, 1 - Show current list, 2 - Add an item to your list, 3 - Remove an item from your list"))
	return choice

def main():
	while(True):
		choice=menu()
		if choice==1:
			current_shopping_list()
		elif choice==2:
			add_shopping_list()
		elif choice==3:
			remove_from_list()
		elif choice==0:
			break


if __name__ == '__main__':
	main()
