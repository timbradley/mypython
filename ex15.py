from sys import argv

script, filename = argv

#open the file and assign to variable
txt = open(filename)

#print the file name
print "Here is your file %r:" % filename

#print the file contents
print txt.read()

#ask the user to input the file name again
print "Type the filename again:"

#assign the user's input to a variable
file_again = raw_input("> ")

#open the specified file
txt_again = open(file_again)

#print the content of the specified file
print txt_again.read()
