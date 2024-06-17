class Product:
    def __init__(self, product_id, name, category, price):
        self.__product_id = product_id  # Приватне поле
        self.__name = name  # Приватне поле
        self.__category = category  # Приватне поле
        self.__price = price  # Приватне поле

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_category(self):
        return self.__category

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

class InventoryManagement:
    def __init__(self, products):
        self.__products = products  # Приватне поле

    def print_product_details(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                print(f"Product ID: {product.get_product_id()}, Name: {product.get_name()}, Category: {product.get_category()}, Price: {product.get_price()}")

    def update_product_price(self, product_id, new_price):
        for product in self.__products:
            if product.get_product_id() == product_id:
                product.set_price(new_price)
                print(f"Price of {product.get_name()} updated to {new_price}")

# Приклад використання
products = [
    Product(1, "Laptop", "Electronics", 1000),
    Product(2, "Chair", "Furniture", 150),
    Product(3, "Book", "Stationery", 20)
]

inventory = InventoryManagement(products)
inventory.print_product_details(1)

inventory.update_product_price(2, 200)
inventory.print_product_details(2)
