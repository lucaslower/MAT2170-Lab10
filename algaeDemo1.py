"""
Introduction to L-systems

Submitted by:
"""

import LSysFns

# Axiom and rules for a simple L-system to model algae growth
axiom = 'A'
rules = {'A':'AB', 'B':'A'}

# Display the L-system in a human-readable format
LSysFns.displayLSystem('L-system to model algae growth', axiom, rules)

# Generate and display the first few strings produced by this system
print()
howMany = 10
print('First %d strings produced by this system...' % howMany)
y = LSysFns.productionYields(axiom, rules, howMany)
for i in range(howMany):
    print('%5d %s' % (len(y[i]), y[i]))
    
