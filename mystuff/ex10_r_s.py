x = "\'"
y = "\""

print "single-quotes with %%r %r" % x
print "double-quotes here %%r %r" % y
print "single-quotes with %%s %s" % x
print "souble-quotes with %%s %s" % y

#conclusion:
#\r will show exactly what your code is,
#if your code is a string,
#then output will be in quotes.
#however, if there's a single-quotes in 
#your string, the quotes in the output
#will be double-quotes, vice verse.
#On the other side, \s output your
#variable in an efficient way,
#it output a string without quotes.
