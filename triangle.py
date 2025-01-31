def classify_triangle(a, b, c):
    type1 = ''
    type2 = ''

    if a <= 0 or b <= 0 or c <= 0:
        return 'Invalid side length'
    elif a + b <= c or a + c <= b or b + c <= a:
        return 'Not a triangle'

    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        type1 = "Right"
    else:
        type1 = "Not Right"

    if a == b and b == c:
        type2 = "Equilateral"
    elif a == b or b == c or a == c:
        type2 = "Isosceles"
    else:
        type2 = "Scalene" 
    
    return f'The triangle is {type1} and {type2}'

if __name__ == '__main__':
    print(classify_triangle(3, 4, -5)) # Invalid side length
    print(classify_triangle(3, 4, 7)) # Not a triangle
    print(classify_triangle(3, 4, 5)) # Right and Scalene
    print(classify_triangle(3, 3, 3)) # Not Right and Equilateral
    print(classify_triangle(3, 3, 4)) # Not Right and Isosceles
    print(classify_triangle(3, 4, 6)) # Not Right and Scalene
    
    
