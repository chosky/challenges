#!/usr/bin/python
"""
What does this print?

print sum([x * (x - 1) for x in [y * y for y in xrange(3,11)]]) 
"""

print sum([x * (x - 1) for x in [y * y for y in xrange(3,11)]]) 
