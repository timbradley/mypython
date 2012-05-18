from sys import argv

script, filename = argv

print "We are going to erase %r." % filename
print "If you dont want to do that hit CTRL-C (^C)."
print "If you do want to do that, hit RETURN."

raw_input("Press ENTER to continue ")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I am going to ask you for three lines."

line1 = raw_input("Line 1 >")
line2 = raw_input("Line 2 >")
line3 = raw_input("Line 3 >")

print "I am goin to write these to the file"

#These statements do the same thing
#target.write("%s\n%s\n%s\n" % (line1, line2, line3))
#target.write(line1+"\n"+line2+"\n"+line3+"\n")
my_variable = line1+"\n"+line2+"\n"+line3+"\n"
target.write(my_variable)


print "And finally, we close the file."
target.close()

#pydoc open
#q
