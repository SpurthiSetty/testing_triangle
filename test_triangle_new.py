import pytest
from triangle_new import classify_triangle

def test_invalid_triangles():
    """Test cases for invalid triangles"""
    assert classify_triangle(-1, -1, -1) == 'Invalid side length'
    assert classify_triangle(0, 0, 0) == 'Invalid side length'
    assert classify_triangle(0, 1, 2) == 'Invalid side length'
    assert classify_triangle(-3, 4, 5) == 'Invalid side length'

def test_not_a_triangle():
    """Test cases where sum of two sides is less than or equal to third side"""
    assert classify_triangle(1, 2, 3) == 'Not a triangle'
    assert classify_triangle(2, 2, 5) == 'Not a triangle'
    assert classify_triangle(10, 10, 20) == 'Not a triangle'
    assert classify_triangle(5, 5, 10) == 'Not a triangle'  # Exact sum test case

def test_right_triangles():
    """Test right triangles"""
    assert classify_triangle(3, 4, 5) == 'The triangle is Right and Scalene'
    assert classify_triangle(5, 12, 13) == 'The triangle is Right and Scalene'
    assert classify_triangle(8, 15, 17) == 'The triangle is Right and Scalene'
    assert classify_triangle(6, 8, 10) == 'The triangle is Right and Scalene'
    assert classify_triangle(5, 5, 7.07) == 'The triangle is Right and Isosceles'

def test_equilateral_triangle():
    """Test equilateral triangles"""
    assert classify_triangle(5, 5, 5) == 'The triangle is Not Right and Equilateral'
    assert classify_triangle(100, 100, 100) == 'The triangle is Not Right and Equilateral'

def test_isosceles_triangle():
    """Test isosceles triangles"""
    assert classify_triangle(5, 5, 8) == 'The triangle is Not Right and Isosceles'
    assert classify_triangle(7, 7, 10) == 'The triangle is Not Right and Isosceles'
    assert classify_triangle(10, 10, 15) == 'The triangle is Not Right and Isosceles'

def test_scalene_triangle():
    """Test scalene triangles"""
    assert classify_triangle(7, 8, 9) == 'The triangle is Not Right and Scalene'
    assert classify_triangle(10, 12, 15) == 'The triangle is Not Right and Scalene'
    assert classify_triangle(20, 25, 30) == 'The triangle is Not Right and Scalene'

def test_large_numbers():
    """Test large numbers"""
    assert classify_triangle(1000000, 1000001, 1414213) == 'The triangle is Right and Scalene'
    assert classify_triangle(999999, 999998, 999997) == 'The triangle is Not Right and Scalene'

def test_floating_point_numbers():
    """Test floating point numbers"""
    assert classify_triangle(3.0, 4.0, 5.0) == 'The triangle is Right and Scalene'
    assert classify_triangle(5.5, 5.5, 7.8) == 'The triangle is Not Right and Isosceles'
    assert classify_triangle(6.1, 6.1, 6.1) == 'The triangle is Not Right and Equilateral'
    assert classify_triangle(999999.5, 999999.5, 1414212.83) == 'The triangle is Right and Isosceles'

def test_input_order():
    """Test different input orders to ensure correct classification"""
    assert classify_triangle(3, 4, 5) == classify_triangle(5, 4, 3)
    assert classify_triangle(7, 8, 9) == classify_triangle(9, 8, 7)
    assert classify_triangle(5, 5, 8) == classify_triangle(8, 5, 5)
