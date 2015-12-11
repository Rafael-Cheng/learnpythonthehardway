my_name = 'Zed A.Shaw'
my_age = 35 #lie
my_height = 74 #inches
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(
    my_age, my_height, my_weight, my_age + my_height + my_weight)

#study drill

his_height_inches = 74
his_weight_lbs = 180
his_height_centimeters = 2.54 * 74
his_weight_kilo = 180 * 0.45

print "He's %r centimeters tall." % his_height_centimeters
print "He's %r kilos heavy." % his_weight_kilo
print "He's not fat at all in terms of his weight."
