def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
	
print "Let's do some maths by using functions!!\n"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "\nAge: %d, Height: %d, Weight: %d, IQ: %d\n" % (age, height, weight, iq)

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand"

#My own way of returning the value of one function, and using it as the argument of another function
print "Here is a puzzle I created."
mypuz = add(age, subtract(iq, 10))
print "That becomes: ", mypuz, "i.e iq = 50 - 10 = 40\nthen age = 35 plus returned value (40) = 75"


# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# what = add(35, subtract(74, multiply(180, divide(50, 2))))
# what = add(35, subtract(74, multiply(180 x 25))))
#
# 50/2 = 25
# 180x25 = 4500
# 74-4500 = -4426
# -4426+35 = -4391