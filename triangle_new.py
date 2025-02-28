"""
Triangle Classification Module

This module classifies a triangle based on the lengths of its sides.
"""

import math

RIGHT = "Right"
NOT_RIGHT = "Not Right"
EQUILATERAL = "Equilateral"
ISOSCELES = "Isosceles"
SCALENE = "Scalene"
INVALID = "Invalid side length"
NOT_TRIANGLE = "Not a triangle"

def classify_triangle(side_a: float, side_b: float, side_c: float) -> str:
    """
    Classifies a triangle based on its side lengths.
    """

    # Validate side lengths
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return "Invalid side length"

    # Ensure sides satisfy the triangle inequality
    if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
        return "Not a triangle"

    # ✅ Use `math.isclose()` to handle floating-point precision in right triangle check
    is_right = (math.isclose(side_a**2 + side_b**2, side_c**2, rel_tol=1e-5) or
                math.isclose(side_a**2 + side_c**2, side_b**2, rel_tol=1e-5) or
                math.isclose(side_b**2 + side_c**2, side_a**2, rel_tol=1e-5))

    # Determine triangle type
    if side_a == side_b == side_c:
        return f'The triangle is Not Right and Equilateral'
    elif side_a == side_b or side_b == side_c or side_a == side_c:
        return f'The triangle is {"Right" if is_right else "Not Right"} and Isosceles'
    else:
        return f'The triangle is {"Right" if is_right else "Not Right"} and Scalene'


if __name__ == '__main__':
    print(classify_triangle(3, 4, -5))  # Invalid side length
    print(classify_triangle(3, 4, 7))   # Not a triangle
    print(classify_triangle(3, 4, 5))   # Right and Scalene
    print(classify_triangle(3, 3, 3))   # Not Right and Equilateral
    print(classify_triangle(3, 3, 4))   # Not Right and Isosceles
    print(classify_triangle(3, 4, 6))   # Not Right and Scalene

