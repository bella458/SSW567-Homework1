"""Bella Manoim's HW 01: Testing Triangle Classification

"""
import unittest
from __builtin__ import False

    
greeting = 'Hello, this program will determine classify triangles based on the 3 side values.'

print(greeting)

triangleType = ''

def classify_triangle(a,b,c):
    triangleType = ''
    if a<1 or b<1 or c<1:
        triangleType = 'Only integer values allowed. Please run program again.\n'
        print(triangleType)
        return(triangleType)
    if a == b == c:
        triangleType = 'This is an equilateral triangle'
    elif (a == b and b != c) or (a == c and b != c) or (b == c and b != a):
        triangleType = 'This is an isosceles triangle'
    elif (a != b and a != c and b != c):
        triangleType = 'This is a scalene triangle'
    if ((a * a) + (b * b) == (c * c)):
        triangleType = triangleType + ' and right triangle'
    print (triangleType)
    return triangleType

try:
    classify_triangle(2,2,3)
    classify_triangle(-5,2,5)
    classify_triangle(3,4,5)
    classify_triangle(1,2,3)
    classify_triangle(2,2,2)
    classify_triangle(5,12,13)
    classify_triangle(5,5,5)
    classify_triangle(5,2,5)
except:
    print ('Only integer values allowed. Please run program again.\n')
    
class TestTriangles(unittest.TestCase):
    def testIsoceles(self): 
        self.assertEqual(classify_triangle(2,2,5),'This is an isosceles triangle')
        
    def testScaleneRight(self): 
        self.assertEqual(classify_triangle(3,4,5), 'This is a scalene triangle and right triangle')
    
    def testScalene(self):
        self.assertEqual(classify_triangle(7,10,16),'This is a scalene triangle')
        self.assertEqual(classify_triangle(1,15,70),'This is a scalene triangle')
        
    def testEquilateral(self):
        self.assertEqual(classify_triangle(6,6,6),'This is an equilateral triangle')
        self.assertEqual(classify_triangle(8,8,8),'This is an equilateral triangle')

    def testWrongInput(self):
        self.assertEqual(classify_triangle(-3,8,8),'Only integer values allowed. Please run program again.\n')
        