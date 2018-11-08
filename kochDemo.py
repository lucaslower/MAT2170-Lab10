"""
Introduction to L-systems: Koch curve

Submitted by:
"""

import LSysFns
import turtle

# Obtain the L-system
system = LSysFns.readLSystem('koch.txt')
axiom = system[0]
rules = system[1]

# Display the L-system in human-readable format
LSysFns.displayLSystem('L-system for the Koch curve', axiom, rules)

# Generate and display the first few string produced by this system
print()
howMany = 3
print('First %d strings produced by this system...' % howMany)
y = LSysFns.productionYields(axiom, rules, howMany)
for i in range(howMany):
    print('%s' % y[i])

# Interpret the strings as turtle commands
bob = turtle.Turtle()
bob.speed(5)

# Drawing parameters
length = 600
angle = 60

# Where should drawing begin?
origin = (-300, 150)

# A few pen colors...
colors = ['cyan', 'red', 'blue', 'black']

for level in range(howMany):
    # Move to origin
    bob.penup()
    bob.goto(origin)
    bob.pendown()

    # choose a color
    bob.pencolor(colors[level])

    # interpret the string produced by the L-system
    LSysFns.interpret(bob, y[level], length/3**level, angle)

# Wait for mouse click within the graphics window
bob.getscreen().exitonclick()


    
