from sys import argv

script, filename = argv

print "We are going to read %r." % filename
print "If you dont want to do that hit CTRL-C (^C)."
print "If you do want to do that, hit RETURN."

raw_input("Press ENTER to continue ")

print "Opening the file..."
target = open(filename)

print "Displaying the file..."
print target.read()
