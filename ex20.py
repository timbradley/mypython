from sys import argv

script, input_file = argv

def print_all(my_file):
	print my_file.read()
	print "\n"

def rewind(my_file):
	my_file.seek(0)

def print_a_line(line_count, my_file):
	print line_count, my_file.readline()
	
current_file = open(input_file)

print "First, let print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:\n\n"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)



