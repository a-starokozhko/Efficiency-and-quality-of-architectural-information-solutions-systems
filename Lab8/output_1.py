class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_address(self):
        return self.address

    def calculate_shipping_cost(self):
        if "New York" in self.address:
            return 5.00
        elif "California" in self.address:
            return 10.00
        else:
            return 15.00

class Order:
    def __init__(self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.quantity = quantity

    def print_order_details(self):
        print(f"Order for {self.product} x {self.quantity}")
        print(f"Shipping to {self.customer.get_address()}")

    def calculate_shipping_cost(self):
        return self.customer.calculate_shipping_cost()