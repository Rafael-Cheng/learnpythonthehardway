from sys import argv

script, name = argv

def Gold_Room():
    print "You see many golds in front of you!"

def Dragon_Home():
    print "There are many dragon here!"
    print "What you wanna do? flee or fight?"
    decision = raw_input(">")
    if decision == "flee":
        print "There is a dragon behind you!"
        dead("Coward, you're eaten.")
    elif decision == "fight":
        print "You're brave and you kill it!"
        Gold_Room()
    else: 
        dead("You're eaten.")

def Snake_Home():
    print "There are snakes all around!!!"
    print "flee or fight?"
    decision = raw_input(">")
    if decision == "flee":
        dead("Coward, you're eaten.")
    elif decision == "fight":
        dead("Cruel world, you're eaten.")
    else:
        print "Snakes thought you're dead and they are gone!!!"
        Gold_Room()

def dead(why):
    print why, "Well done!"

def start():
    print "Hello", name
    print "You are in the forest, there are three way in front of you."
    print "choose one, two or three."
    decision = raw_input(">")
    if decision == "one":
        Dragon_Home()
    elif decision == "two":
        Gold_Room()
    elif decision == "three":
        Snake_Home()
    else:
        dead("You're lost")

start()
