"""
shapes.py
Functions for calculating areas and circumference,
plus a simple console interface for user input.
"""

import math

def area_square(side):
    """Return the area of a square given the side length."""
    return side * side

def area_rectangle(length, width):
    """Return the area of a rectangle."""
    return length * width

def area_triangle(base, height):
    """Return the area of a triangle."""
    return 0.5 * base * height

def area_circle(radius):
    """Return the area of a circle."""
    return math.pi * radius * radius

def circumference_circle(radius):
    """Return the circumference of a circle."""
    return 2 * math.pi * radius

def main():
    print("Shape Calculator")
    print("Options: square, rectangle, triangle, circle_area, circle_circumference")
    shape = input("Enter shape: ").strip().lower()

    if shape == "square":
        side = float(input("Enter side length: "))
        result = area_square(side)

    elif shape == "rectangle":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        result = area_rectangle(length, width)

    elif shape == "triangle":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        result = area_triangle(base, height)

    elif shape == "circle_area":
        radius = float(input("Enter radius: "))
        result = area_circle(radius)

    elif shape == "circle_circumference":
        radius = float(input("Enter radius: "))
        result = circumference_circle(radius)

    else:
        print("Unknown shape.")
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
