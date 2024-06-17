class ShapeCalculator:
    def calculate_area(self, shape_type):
        # Словник, що мапить тип фігури на відповідний метод
        shape_methods = {
            "circle": self.calculate_circle_area,
            "rectangle": self.calculate_rectangle_area,
            "triangle": self.calculate_triangle_area
        }

        # Виклик відповідного методу, якщо він існує
        calculate_method = shape_methods.get(shape_type)
        if calculate_method:
            calculate_method()
        else:
            print("Invalid shape type")

    def calculate_circle_area(self):
        radius = float(input("Enter the radius of the circle: "))
        area = 3.14 * radius * radius
        print("Area:", area)

    def calculate_rectangle_area(self):
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print("Area:", area)

    def calculate_triangle_area(self):
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print("Area:", area)

# Приклад використання класу
calculator = ShapeCalculator()
shape_type = input("Enter the type of shape (circle, rectangle, triangle): ").lower()
calculator.calculate_area(shape_type)
