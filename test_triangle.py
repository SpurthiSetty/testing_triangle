import pytest
from triangle import classify_triangle

def test_classify_triangle():
    assert classify_triangle(3, 4, -5) == 'Invalid side length'
    assert classify_triangle(3, 4, 7) == 'Not a triangle'
    assert classify_triangle(3, 4, 5) == 'The triangle is Right and Scalene'
    assert classify_triangle(3, 3, 3) == 'The triangle is Not Right and Equilateral'
    assert classify_triangle(3, 3, 4) == 'The triangle is Not Right and Isosceles'
    assert classify_triangle(3, 4, 6) == 'The triangle is Not Right and Scalene'