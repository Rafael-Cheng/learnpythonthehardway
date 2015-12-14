print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n new lines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print "____________"
print poem
print "____________"

five = 10 -2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
#Functions in python can return more than one variables?

start_point = 10000
beans, jars, crates = secret_formula(start_point)
#Attention!

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
