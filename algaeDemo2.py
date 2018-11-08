"""
Introduction to L-systems

Submitted by:
"""

import LSysFns

# Obtain the L-system
system = LSysFns.readLSystem('algae.txt')
axiom = system[0]
rules = system[1]

# Display the L-system in a human-readable format
LSysFns.displayLSystem('L-system to model algae growth', axiom, rules)

# Generate and display the first few strings produced by this system
print()
howMany = 10
print('First %d strings produced by this system...' % howMany)
y = LSysFns.productionYields(axiom, rules, howMany)
for i in range(howMany):
    print('%5d %s' % (len(y[i]), y[i]))
    
