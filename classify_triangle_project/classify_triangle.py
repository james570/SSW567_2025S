def classify_triangle(a, b, c):
    if not all(isinstance(side, (int, float)) for side in [a, b, c]):
        return "Invalid input: Side lengths must be numbers"
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid input: Side lengths must be positive"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid input: Not a valid triangle"

    sides = sorted([a, b, c])
    is_right = sides[0]**2 + sides[1]**2 == sides[2]**2

    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    if is_right:
        return f"{triangle_type} and Right Triangle"
    return triangle_type

if __name__ == "__main__":
    test_cases = [
        (3, 4, 5),     
        (5, 5, 5),     
        (5, 5, 8),     
        (7, 10, 5),    
        (1, 2, 3),     
        (-3, 4, 5),    
        ("a", 4, 5)    
    ]

    for a, b, c in test_cases:
        print(f"classify_triangle({a}, {b}, {c}) ➝ {classify_triangle(a, b, c)}")
