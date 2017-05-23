name = 'Zed A. Shaw'
age = 35
height = 74 * 2.54
weight = 180
weight_in_kilos = weight * (1 / 2.2)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'


print "Let's talk about %s." % name
print "He's %d centimeters tall." % height
print "He's %d kilos heavy." % weight_in_kilos
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d" % (age, height, weight_in_kilos, age + height + weight_in_kilos)
