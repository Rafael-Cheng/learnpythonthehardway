from sys import argv

script, filename = argv

#returns a file subject
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()

#study drill 7
#do this in the prompt:
#txt = open("ex15_sample.txt") or
#txt = open('ex15_sample.txt')
#txt.read()
#txt.close()
