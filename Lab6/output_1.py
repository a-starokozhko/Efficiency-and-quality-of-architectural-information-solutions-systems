def apply_discount(price, discount):
    if discount:
        return price * 0.9  # 10% discount
    else:
        return price

def calculate_total_price(product_prices, discount):
    total_price = sum(apply_discount(price, discount) for price in product_prices)
    return total_price

def calculate_total_price_with_tax(product_prices, discount, tax_rate):
    total_price = calculate_total_price(product_prices, discount)
    total_price *= (1 + tax_rate)
    return total_price

# Приклад використання функцій
product_prices = [100, 200, 300]
discount = True
tax_rate = 0.07

print("Total price without tax:", calculate_total_price(product_prices, discount))
print("Total price with tax:", calculate_total_price_with_tax(product_prices, discount, tax_rate))
