class Product:
    def __init__(self, name, price, product_type):
        self.name = name
        self.price = price
        self.product_type = product_type

def search_product(products, query):
    # Пошук товару за запитом
    return [product for product in products if query.lower() in product.name.lower()]

def display_product(product):
    # Відображення інформації про товар
    print(f"Name: {product.name}")
    print(f"Price: {product.price}")
    print(f"Type: {product.product_type}")

def order_product(product, quantity):
    # Замовлення товару
    print(f"Ordered {quantity} of {product.name} at {product.price} each.")

# Приклад використання
products = [
    Product("Laptop", 1000, "Electronics"),
    Product("Chair", 150, "Furniture"),
    Product("Book", 20, "Stationery")
]

# Пошук продукту
query = "Laptop"
found_products = search_product(products, query)
for product in found_products:
    display_product(product)
    order_product(product, 2)
