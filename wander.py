"""
Demonstration of saving/restoring the state of the turtle

Submitted by:
"""
import turtle
import random
import LSysFns

def displayStack(myStack):
    """
    Display the contents of a stack of crumbs
    """
    stackCopy = myStack[:]
    while len(stackCopy) > 0:
        # get the value from the top of the stack...
        crumb = stackCopy.pop()

        # ...and display it
        print(crumb)

        
def retraceSteps(myTurtle, myStack):
    """
    Use the bread crumbs in a given stack to retrace steps taken in a random walk
    """
    while len(myStack) != 0:
        crumb = myStack.pop()
        myTurtle.pencolor(crumb[0])
        myTurtle.goto(crumb[1])

        
def wanderAround():
    # create a turtle object
    bob = turtle.Turtle()

    # Adjust pen size and speed
    bob.pensize(3)
    bob.speed(2)

    # create a stack to save turtle "bread crumbs"
    breadCrumbs = []

    # palette of colors to choose from
    colors = ["midnight blue", "lawn green", "magenta", "slate gray", "hot pink", "black", "red"]

    # number of steps to take?
    steps = random.randint(10, 50)

    # take a random walk
    for i in range(steps):
        # choose a color
        myColor = random.choice(colors)

        # choose a turning angle
        myAngle = random.randint(0, 359)

        # choose a distance
        myDistance = random.randint(25, 75)

        # change the color and get ready to move
        bob.pencolor(myColor)
        bob.left(myAngle)

        # drop a bread crumb
        crumb = LSysFns.getTurtleState(bob)
        breadCrumbs.append(crumb)

        # move!
        bob.forward(myDistance)

    # show the stack of bread crumbs
    displayStack(breadCrumbs)

    # retrace all steps taken
    retraceSteps(bob, breadCrumbs)

    # wait for a mouse click
    bob.getscreen().exitonclick()

        
if __name__ == "__main__":
    # take a random walk!
    wanderAround()


    
