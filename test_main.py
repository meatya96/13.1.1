from main import Product, Category
import pytest


@pytest.fixture
def category_test():
    data_category = {'name': 'Шоколад',
                     'description': 'Сладкий',
                     'products': ['mars', 'snickers', 'bounty']}

    return Category(data_category['name'], data_category['description'], data_category['products'])


@pytest.fixture
def product_test():
    data_product = {'name': 'mars',
                    'description': 'Очень вкусный',
                    'price': 50,
                    'amount': 10}
    return Product(data_product['name'], data_product['description'], data_product['price'], data_product['amount'])


def test_products_amount(category_test):
    expected_products_amount = 3
    assert category_test.products_amount == expected_products_amount

def test_category_amount(category_test):
    expected_category_amount = 2
    assert category_test.category_amount == expected_category_amount


def test_category_name(category_test):
    expected_name = 'Шоколад'
    assert category_test.name == expected_name


def test_category_description(category_test):
    expected_description = 'Сладкий'
    assert category_test.description == expected_description


def test_category_products(category_test):
    expected_item = ['mars', 'snickers', 'bounty']
    assert category_test.products == expected_item






def test_product_name(product_test):
    expected_product_name = 'mars'
    assert product_test.name == expected_product_name


def test_product_description(product_test):
    expected_product_description = 'Очень вкусный'
    assert product_test.description == expected_product_description


def test_product_price(product_test):
    expected_product_price = 50
    assert product_test.price == expected_product_price


def test_product_amount(product_test):
    expected_product_amount = 10
    assert product_test.amount == expected_product_amount
