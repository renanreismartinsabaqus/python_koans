#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#

def count_equals(elements, count):
    if (elements == []):
         return count
    #reduce?
    return count_equals(elements[1:], count + elements[1:].count(elements[0]))

def triangle(a, b, c):
    c = count_equals([a, b, c], 0) 
    print(c)
    match c:
        case 0:
            return "scalene"
        case 1:
            return "isosceles"
        case 3:
            return "equilateral"

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
