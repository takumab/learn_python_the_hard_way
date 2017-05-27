# Insers variable into string and then gives
# variable a number and assigns
# it to x
x = "There are %d types of people." % 10
# Assigns binary to binary
binary = "binary"
# Assigns don't to do_not variable
do_not = "don't"
# String interpolation
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# What does %r format character do?
# Displays the "raw" data of the variable
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False

joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
