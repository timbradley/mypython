# This is like one of the scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#The *args above is pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2 %r " % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
#this one takes no arguements
def print_none():
	print "I aint got nothin."
	
print_two("Tim", "Bradley")
print_two_again("Charming", "Funny")
print_one("First!")
print_none()

#Function Checklist
#
#Did you start your function definition with def?
#Does your function name have only characters and _ (underscore) characters?
#Did you put an open parenthesis ( right after the function name?
#Did you put your arguments after the parenthesis ( separated by commas?
#Did you make each argument unique (meaning no duplicated names).
#Did you put a close parenthesis and a colon ): after the arguments?
#Did you indent all lines of code you want in the function 4 spaces? No more, no less.
#Did you "end" your function by going back to writing with no indent (dedenting we call it)?
#
#When running (calling) the function:
#
#Did you call/use/run this function by typing its name?
#Did you put ( character after the name to run it?
#Did you put the values you want into the parenthesis separated by commas?
#Did you end the function call with a ) character.
