my_name = "Tim Bradley"
my_age = 38 #mental age 23
my_height = 74
my_weight = 250
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He is %d inches tall" % my_height
print "He is %d pounds heavy" % my_weight
print "He has %s eyes and %s hair" % (my_eyes, my_hair)

print "If I add %d, %d and %d I get %d" % (my_age, my_height, my_weight, my_age + my_height + my_weight)

#One way to do a conversion
mile_in_km = 1.609344
number_of_km = 10.00

print "If you have run ", number_of_km, "km, then you have run %f miles" % (number_of_km / mile_in_km)

#And another way to do a conversion
mile_in_km = 1.609344
number_of_miles = 13.1
result = number_of_miles * mile_in_km

print "If you have run ", number_of_miles, "miles, then you have run %f km" % result