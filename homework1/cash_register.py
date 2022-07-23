class CashRegister:

    def __init__(self):

        self.total_items = [] # {'item': 'apple','price': 10}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item_dict):
        self.total_items.append(item_dict)
        self.total_price += item_dict['price']

    def remove_item(self, item_dict):
        for i in range(len(self.total_items)):
            if self.total_items[i]['item'] == item_dict['item'] and self.total_items[i]['price'] == item_dict['price']:
                del self.total_items[i]

    def apply_discount(self, discount_amt):
        self.discount += discount_amt

    def get_total(self):
        return self.total_price - self.discount

    def show_items(self):
        print(self.total_items)

    def reset_register(self):
        self.total_items = []
        self.total_price = 0
        self.discount = 0


cash_register = CashRegister()

item_apple = {"item": "apple", "price": 10}
cash_register.add_item(item_apple)

item_banana = {"item": "banana", "price": 8}
cash_register.add_item(item_banana)

items = cash_register.show_items()

cash_register.apply_discount(2)

total = cash_register.get_total()

print(f"Total Amount: {total}")