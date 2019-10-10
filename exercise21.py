def add(a, b):
	print("Adding : {} + {}".format(a, b))
	return(a + b)
	
def sub(a, b):
	print("Subtracting : {} - {}".format(a, b))
	return(a-b)
	
def multiply(a, b):
	print("Multiplying : {} * {}".format(a, b))
	return(a*b)
	
def divide(a, b):
	print("Dividing : {} / {}".format(a, b))
	return(a/b)
	
print("Let us do maths with just some functions")

age = add(30, 5)
height = sub(78, 4)
weight = multiply(90, 2)
IQ = divide(100,2)

print("Age : {}, Height : {}, Weight : {}, IQ : {}".format(age, height, weight, IQ))

#A puzzle ofr extra credits
print("Here is a puzzle")
what = add(age, sub(height, multiply(weight, divide(IQ, 2))))
print("Thtas becomes: ", what, "Can you do it by hand?")