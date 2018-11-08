"""
Support functions for L-Systems

Submitted by:
"""

import turtle

def readLSystem(filename):
    """
    Opens the given file and retrieves the axiom and rewriting rules
    from the information in the file

    Args:
        filename: the name of a text file of the appropriate format

    Returns:
        a pair (a, d) where a is the initial axiom for the system and d
        is a dictionary of symbol:rule pairs for the rewriting rules
    """
    # NOT IMPLEMENTED...
    pass


def displayLSystem(title, axiom, rules):
    """
    Displays an L-system in a human-readable format

    Args:
        title: a string with the desired L-system title
        axiom: the axiom for the L-system
        rules: a dictionary of all production rules for the L-system

    Returns:
        None
    """
    print(title)
    print('-'*len(title))
    print('Axiom:')
    print('  ', axiom)
    print('  ')
    print('Rules:')
    # get rules
    rule_keys = list(rules.keys())
    for key in rule_keys:
        print(key, ' -> ', rules[key])
        print('  ')
        print('First 10 strings produced by this system...')
        l_string = axiom
        for i in range(10):
            print(len(l_string), ' ', l_string)
            l_string = nextGeneration(l_string, rules)


def nextGeneration(s, rules):
    """
    Re-writes a string by replacing each character in s by the
    string of characters, using the appropriate rewriting rule.

    Args:
        s: the string to be rewritten
        rules: a dictionary which defines the rewriting rules

    Returns:
        a string representing the rewritten string
    """

    result = ""
    for c in s:
        if c in rules:
            # use the RHS portion of the rewriting rule to replace c
            result = result + rules[c]
        else:
            # no rule for c, so leave it as is
            result = result + c

    return result


def applyProduction(axiom, rules, n):
    """
    Determines the string generated from axiom by n rewritings

    Args:
        axiom: the initial string
        rules: A dictionary with the rewriting rules
        n: The number of rewritings

    Returns:
        The string resulting from the rewritings
    """

    if n == 0:
        return axiom
    else:
        return nextGeneration(applyProduction(axiom, rules, n - 1), rules)

    
def productionYields(axiom, rules, n):
    """
    Create a list of the first n strings produced by a given L-system

    Args:
        axiom: the initial string
        rules: the rewriting rules
        n: how many strings to produce, where n >= 0

    Returns:
        A list of the first n strings produced by the given L-system
    """
    # NOT IMPLEMENTED...
    pass


def interpret(myTurtle, s, dist, angle):
    """
    Interpret a string generated by an L-system, moving a turtle appropriately

    Args:
        myTurtle: the turtle to do the drawing
        s: the string to interpret
        dist: the amount to move on any given turtle movement
        angle: the amount to turn, left or right, in degrees

    Returns:
        None
    """
    for c in s:
        if c == 'F':
            # forward
            myTurtle.forward(dist)
        elif c == '-':
            # left turn
            myTurtle.left(angle)
        elif c == '+':
            # right turn
            myTurtle.right(angle)
        else:
            # unrecognized action
            pass

        
def getTurtleState(myTurtle):
    """
    Saves (as a triple) the current pencolor, position, and heading

    Args:
        myTurtle: the turtle in question

    Returns:
        a triple of the form (color, (x,y), heading)
    """

    return (myTurtle.pencolor(), myTurtle.position(), myTurtle.heading())


def resetTurtle(myTurtle, stateTriple):
    """
    restores the turtle to the indicated state

    Args:
        myTurtle: the turtle being restored

    Returns:
        None
    """

    myTurtle.penup()
    color,pos,angle = stateTriple
    myTurtle.pencolor(color)
    myTurtle.goto(pos)
    myTurtle.setheading(angle)
    myTurtle.pendown()

        
def showLSystemCurve(filename, n, origin, heading, length, angle):
    """
    Compute and display a fractal curve defined by an L-system

    Args:
        filename: a string containing the name of a L-system description file
        n: the desired generation
        origin: an ordered pair, indicating where to begin drawing
        heading: desired initial heading of turtle (0 = east, 90 = north, etc.)
        length: step size for each turtle move
        angle: angle to turn in reaction to each +/-

    Returns:
        None
    """
    
    # NOT IMPLEMENTED...
    pass
