# this one is like your scripts with argv

def print_two(*args):
	arg1, arg2 = args
	print("arg1: {}, arg2: {}".format(arg1, arg2))
	
# ok that argument is just pointless, we can just do this
def print_two_again(arg1, arg2):
	print("arg1: {}, arg2: {}".format(arg1, arg2))

# this is just one argument
def print_one(arg1):
	print("arg1: {}".format(arg1))
	
# this takes no arguments
def print_none():
	print("I got nothing")
	
print_two("Rahul", "Prikshit")
print_two_again("Pankhuri","Nidhi")
print_one("This is just one argument")
print_none()