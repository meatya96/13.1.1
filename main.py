class Category():
    name: str
    description: str
    __products: list
    category_amount = 0
    products_amount = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        products_name = []
        for item in self.__products:
            products_name.append(item['name'])
        set_products = set(products_name)
        self.__class__.products_amount += len(set_products)
        self.__class__.category_amount += 1

    def add_product(self, product):
        self.__products.append(product)

    @property
    def products(self):
        product_list = []
        for product in self.__products:
            product_list.append(f"{product['name']}, {product['price']} руб. Остаток: {product['amount']} шт.")
        return product_list


data_category = {'name': 'Шоколад',
                 'description': 'Сладкий',
                 'products': [{'name': 'mars',
                               'description': 'Очень вкусный',
                               'price': 50,
                               'amount': 10},
                              {'name': 'bounty',
                               'description': 'Очень вкусный',
                               'price': 55,
                               'amount': 7},
                              {'name': 'snickers',
                               'description': 'Очень вкусный',
                               'price': 60,
                               'amount': 12}]}
category_1 = Category(data_category['name'], data_category['description'], data_category['products'])

print(category_1.products)


class Product():
    name: str
    description: str
    _price: float
    amount: int

    def __init__(self, name, description, price, amount):
        self.name = name
        self.description = description
        self._price = price
        self.amount = amount

    @staticmethod
    def create_product(name, description, price, amount):
        return Product(name, description, price, amount)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Ошибка: Цена должна быть больше нуля.")
        else:
            self._price = value
