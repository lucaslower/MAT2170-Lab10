"""
Introduction to L-systems: Koch curve

Submitted by:
"""

import LSysFns
import turtle

# Obtain the L-system
system = LSysFns.readLSystem('kochVariant.txt')
axiom = system[0]
rules = system[1]

# Display the L-system in human-readable format
LSysFns.displayLSystem('L-system for the Koch-variant curve', axiom, rules)

# Generate and display the first few string produced by this system
print('  ')
howMany = 4
print('First %d strings produced by this system...' % howMany)
y = LSysFns.productionYields(axiom, rules, howMany)
for i in range(howMany):
    print('%s' % y[i])

# Interpret the strings as turtle commands
bob = turtle.Turtle()
bob.getscreen().tracer(0)

# Drawing parameters
length = 600
angle = 90

# Where should drawing begin?
origin = (-300, 0)

# Move to origin
bob.penup()
bob.goto(origin)
bob.pendown()

# interpret the string produced by the L-system
LSysFns.interpret(bob, y[howMany-1], length/3**(howMany-1), angle)

# update
bob.getscreen().update()

# Wait for mouse click within the graphics window
bob.getscreen().exitonclick()


    
