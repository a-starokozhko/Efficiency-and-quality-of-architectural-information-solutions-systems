class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclasses should implement this method")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


# Приклад виклику програми
def main():
    shape_type = input("Enter the type of shape (circle, rectangle, triangle): ").lower()

    if shape_type == "circle":
        radius = float(input("Enter the radius of the circle: "))
        shape = Circle(radius)
    elif shape_type == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        shape = Rectangle(length, width)
    elif shape_type == "triangle":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        shape = Triangle(base, height)
    else:
        print("Invalid shape type")
        return

    area = shape.calculate_area()
    print("Area:", area)

if __name__ == "__main__":
    main()
