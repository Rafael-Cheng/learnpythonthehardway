formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

#study drill
#There's a ' (single-quotes) in "But it didn't sing."
#therefore the output use double-quotes
#%r print the raw programmer's version of variables.
#so it's reasonable if it's not very efficient.
