class OrderProcessor:
    def __init__(self, order):
        self.order = order

    def process_order(self):
        self._check_stock()
        self._calculate_total()
        self._apply_discount()
        self._update_order_status()
        self._send_confirmation()

    def _check_stock(self):
        for item in self.order['items']:
            if item['quantity'] > item['stock']:
                raise ValueError(f"Insufficient stock for item {item['name']}")

    def _calculate_total(self):
        total_amount = 0
        for item in self.order['items']:
            total_amount += item['price'] * item['quantity']
        self.order['total_amount'] = total_amount

    def _apply_discount(self):
        if self.order['discount_code']:
            if self.order['discount_code'] == 'SUMMER21':
                self.order['total_amount'] *= 0.9
            elif self.order['discount_code'] == 'WINTER21':
                self.order['total_amount'] *= 0.85

    def _update_order_status(self):
        self.order['status'] = 'Processed'

    def _send_confirmation(self):
        print(f"Order processed for {self.order['customer_name']}. Total amount: {self.order['total_amount']}")


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
