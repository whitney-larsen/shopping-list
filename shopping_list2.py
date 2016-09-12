shopping_list = {}

def menu():
 #display menu and get choice using raw_input
	choice = int(raw_input("\n0 - Main Menu.\n1 - Show all lists.\n" \
		"2 - Show a specific list.\n3 - Add a new shopping list.\n" \
		"4 - Add an item to a shopping list.\n5 - Remove an item from a shopping list.\n" \
		"6 - Remove a list by nickname.\n7 - Open a shopping list from file.\n"
		"8 - Exit when you are done and save to file.\n"))
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

def add_item_to_list(key,items_list):
#prompt for existing list and then add item to that list
	if key in shopping_list:
		shopping_list[key].extend(items_list)
	else:
		print "That list does not exist."

def parse_string(items_string):
	items_list = items_string.split(",")
	return items_list

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
	
def write_to_file(my_file):
	with open(my_file, mode = "w") as my_file:
		shopping_list_string = str(shopping_list)
		my_file.write(shopping_list_string)


def read_file(my_file):
	with open(my_file, mode='r') as my_file:
		new_string = my_file.read()
		global shopping_list
		shopping_list = eval(new_string)

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
			items_string=(str(raw_input("What item do you want to add to the list?"))).lower()
			items_list=parse_string(items_string)
			add_item_to_list(key,items_list)
		elif choice ==5:
			key=(raw_input("What list do you want to remove an item from?")).lower()
			item=(str(raw_input("What item do you want to remove from the list?"))).lower()
			remove_item_from_list(key,item)
		elif choice==6:
			key=(raw_input("What list do you want to remove?")).lower()
			remove_list(key)
		elif choice ==7:
			my_file=(raw_input("What file do you want to open?"))
			read_file(my_file)
		elif choice==8:
			write_to_file("shopping_list.txt")
			break
		else:
			print "That is not a valid input."


if __name__ == '__main__':
	main()
