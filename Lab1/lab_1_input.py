class OrderProcessor:
    def __init__(self, order):
        self.order = order

    def process_order(self):
        # Перевірка наявності товарів
        for item in self.order['items']:
            if item['quantity'] > item['stock']:
                raise ValueError(f"Insufficient stock for item {item['name']}")

        # Розрахунок загальної суми
        total_amount = 0
        for item in self.order['items']:
            total_amount += item['price'] * item['quantity']

        # Застосування знижки
        if self.order['discount_code']:
            if self.order['discount_code'] == 'SUMMER21':
                total_amount *= 0.9
            elif self.order['discount_code'] == 'WINTER21':
                total_amount *= 0.85

        # Оновлення стану замовлення
        self.order['status'] = 'Processed'
        self.order['total_amount'] = total_amount

        # Відправлення підтвердження клієнту
        print(f"Order processed for {self.order['customer_name']}. Total amount: {total_amount}")


if __name__ == "__main__":
    order = {
        'customer_name': 'John Doe',
        'items': [
            {'name': 'Item1', 'price': 100, 'quantity': 2, 'stock': 5},
            {'name': 'Item2', 'price': 50, 'quantity': 1, 'stock': 1},
        ],
        'discount_code': 'SUMMER21'
    }
    
    processor = OrderProcessor(order)
    processor.process_order()
