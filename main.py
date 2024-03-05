class Category():
    name: str
    description: str
    products: list
    category_amount = 0
    products_amount = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        set_products = set(products)
        self.__class__.products_amount += len(set_products)
        self.__class__.category_amount += 1

class Product():
    name: str
    description: str
    price: float
    amount: int

    def __init__(self, name, description, price, amount):
        self.name = name
        self.description = description
        self.price = price
        self.amount = amount
