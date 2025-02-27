"""
Module: classify_triangle
This module contains a function to classify triangles based on side lengths.
"""

def classify_triangle(side_a, side_b, side_c):
    """
    Classifies a triangle based on its three sides.

    Args:
        side_a (int or float): Length of the first side.
        side_b (int or float): Length of the second side.
        side_c (int or float): Length of the third side.

    Returns:
        str: Type of the triangle or an error message.
    """
    if not all(isinstance(side, (int, float)) for side in [side_a, side_b, side_c]):
        return "Invalid input: Side lengths must be numbers"
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return "Invalid input: Side lengths must be positive"
    if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
        return "Invalid input: Not a valid triangle"

    sides = sorted([side_a, side_b, side_c])
    is_right = sides[0]**2 + sides[1]**2 == sides[2]**2

    if side_a == side_b == side_c:
        triangle_type = "Equilateral"
    elif side_a == side_b or side_b == side_c or side_a == side_c:
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

    for side_a, side_b, side_c in test_cases:
        print(f"classify_triangle({side_a}, {side_b}, {side_c}) ➝ {classify_triangle(side_a, side_b, side_c)}")
