bill_amt = 0
tip_percent = 0
tip_amount = 0
total_bill = 0
num_people = 0
split_bill = 0


def CalcTip():
	global tip_amount
	tip_amount = bill_amt*tip_percent
	return tip_amount

# print CalcTip(bill_amt)

def bill():
	global total_bill
	total_bill = bill_amt + tip_amount
	return total_bill

#print bill()

def split():
	global split_bill
	split_bill = total_bill/num_people
	return split_bill

# bill ()
# print split()
# 		
def main():
	num = int(raw_input("enter 1 to calculate tip, enter 2 to split the bill: "))
	if num == 1:
		global bill_amt
		bill_amt = float(raw_input("enter original bill amount: "))
		global tip_percent
		tip_percent = float(raw_input("enter tip percentage: "))
		CalcTip()
		bill()
		print "your tip amount is %f, and your total bill is %f." % (tip_amount,total_bill)
		split_prompt = raw_input("do you want to split the bill? (y/n) ")
		if split_prompt == "y":
			global num_people 
			num_people = int(raw_input("how many ways are you splitting the bill? "))
			split()
			print "Each person should pay %f. Show me the money!" % (split_bill)
		else: 
			print "hope you enjoyed your dinner."
	# elif num == 2:
	# 		global total_bill
	# 		total_bill = float(raw_input("how much was your total bill for dinner? "))
	# 		num_people = int(raw_input("how many ways are you splitting the bill? "))
	# 		split()
	# 		print "Each person owes %f "  %  (split_bill)

if __name__ == '__main__':
	main()