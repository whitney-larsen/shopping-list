def add(num1, num2):
	return num1+num2

def subtract(num1, num2):
	return num2-num1 

def multiply(num1, num2):
	return num1*num2

def divide (num1, num2):
	return num1/num2

def modulo(num1, num2):
	return num1%num2 

def power(base, exponent): 
	return base**exponent

def square(num):
	return num**2

print add(add(4,5),subtract (6,9))
print subtract(60,divide(12,2))
print add(add(1,2), add(3,0)) 
print square(add(1,2))
print divide(modulo(3.0,4),multiply(9.0,9))
print multiply(add(3,8), 7)
print subtract(multiply(add(4,5), 3), add(1,2))
print power(3,add(2,3))



