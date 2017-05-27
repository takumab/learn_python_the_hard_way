# Remember %r displays raw data of variables
formatter = "%r %r %r %r"

# Prints raw numbers 1,2,3,4
print formatter % (1,2,3,4)

# Prints strings as they are
print formatter % ("one", "two", "three", "four")

# Prints True and False in raw format
print formatter % (True, False, True, False)
# Prints the %r characters themselves
print formatter % (formatter, formatter, formatter, formatter)

# Prints raw strings on the same line
# "But it didn't sing." printed with double quotes
# and the others printed with single quotes
# the reason for that is the apostraphe in "didn't"
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
