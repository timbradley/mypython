from sys import argv

script, user_name = argv
prompt = 'Here > '

print "Hello %s, I am the %s script" % (user_name, script)
print "I would like to ask you a few questions"
print "Do you like me %s ?" % user_name
likes = raw_input(prompt)

print "Where do you live %s ?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have ?"
computer = raw_input(prompt)

print"""
Alright, so you said %r about liking me.
You live in %r. I'm not sure where that is.
And you have a %r computer. Very Nice.
""" % (likes, lives, computer)
