from abc import ABC, abstractmethod


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
            products_name.append(item.name)
        set_products = set(products_name)
        self.__class__.products_amount += len(set_products)
        self.__class__.category_amount += 1

    def add_product(self, product):
        if isinstance(product,Product):
            self.__products.append(product)
        else:
            raise TypeError('Можно добавить только наследника класса Product')


    @property
    def products(self):
        product_list = []
        for product in self.__products:
            product_list.append(f"{product.name}, {product.price} руб. Остаток: {product.amount} шт.")
        return product_list

    def __len__(self):
        return len(self.products)

    def __str__(self):
        return f"{self.name}, Количество продуктов: {len(self)} шт."



class AbstractProduct(ABC):
    @abstractmethod
    def __add__(self):
        pass

class Mixin():
    def print_console(self):
        print(repr(self))

class Product(AbstractProduct,Mixin):
    name: str
    description: str
    _price: float
    amount: int

    def __init__(self, name, description, price, amount):
        self.name = name
        self.description = description
        self._price = price
        self.amount = amount
        self.print_console()

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

    def __add__(self, other):
        if type(self) == type(other):
            total_price = self._price * self.amount + other._price * other.amount
            return total_price
        else:
            raise TypeError('Экземпляры разных классов складывать нельзя')

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.amount} шт."

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.amount})"


class Smartphone(Product):
    perfomance: str
    model: str
    osu: str
    color: str
    def __init__(self, name, description, price, amount, perfomance, model, osu, color):
        self.perfomance = perfomance
        self.model = model
        self.osu = osu
        self.color = color
        super().__init__(name, description, price, amount)
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.amount}, {self.perfomance}, {self.model}, {self.osu}, {self.color} )"

class Grass(Product):
    country: str
    growth_period: str
    color: str
    def __init__(self, name, description, price, amount, country,growth_period, color):
        self.country = country
        self.growth_period = growth_period
        self.color = color
        super().__init__(name, description, price, amount)
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.amount}, {self.country}, {self.growth_period}, {self.color})"


'''
product_a = Product("Шоколад", "Очень вкусный", 100, 10)
product_b = Product("Шоколад", "Очень вкусный", 200, 2)

data_category = {'name': 'Шоколад',
                 'description': 'Сладкий',
                 'products': [product_a,
                              product_b]}
category_1 = Category(data_category['name'], data_category['description'], data_category['products'])
print(category_1.products)
'''

"""
product_a = Smartphone("Шоколад", "Очень вкусный", 100, 10, 'lol','kek','lol','kk')
product_aa = Smartphone("Шоколад", "Очень вкусный!!!w", 100, 10, 'lol','kek','lol','kk')
product_b = Grass("Шоколад", "Очень вкусный", 200, 2, 'lol','kek','lol')

print(product_a)
print(product_b)
data_category = {'name': 'Шоколад',
                 'description': 'Сладкий',
                 'products': [product_a,
                              product_b]}
category_1 = Category(data_category['name'], data_category['description'], data_category['products'])


print(repr(category_1))
"""
