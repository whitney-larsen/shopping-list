today = raw_input("What day is it?")

if today == "Monday":
	print "Yay class day"
elif today == "Tuesday":
	print "sigh, it's only tuesday"
elif today=="Wednesday":
	print "Humpday!"
elif today== "Thursday":
	print "#tbt"
elif today== "Friday":
	print "TGIF"
else:
	print "Yeah, it's the weekend!"

age = int(raw_input("what is your age?"))
if age >= 18 :
	print "yay I can vote!"
else:
	print "aww I cannot vote"

if age >= 18 and age >= 21:
	print "I can vote and go to the bar!"

age = int(raw_input("What is your age?"))
if age >= 21:
	print "I can go to the bar!"
elif age >= 18:
	print "I can vote but I can't go to the bar!"
else:
	print "I cannot vote or go to the bar!"

num = 8
if 8%2 == 0:
	print "the number 8 is even"
else:
	print "the number 8 is odd"

if num%2 == 1:
	print "the number 8 is odd"
else:
	print "the number 8 is even"
