#this one is like your scripts with argv
#just like argv we've learnt before, *argv packs the arguments.
#it takes all the  arguments to the function and then 
#put them in args as a list
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, args: %r" % (arg1, arg2)

#this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

#this one takes no arguments
def print_none():
    print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

#Functions do three things:
#1. They name pieces of code the way variables name strings and numbers.
#2. They take arguments the way your scripts take argv.
#3. using #1 & #2, they let u make ur own "mini-scripts" or "tiny commands."
