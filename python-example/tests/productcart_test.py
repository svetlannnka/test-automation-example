import pytest
from selenium import webdriver
from app.application import Application


@pytest.fixture
def app(request):
    app = Application()
    request.addfinalizer(app.quit)
    return app


def test_cart(app):
    test_products = 2

    products = app.get_product_links(test_products)
    for product in products:
        app.add_product_to_cart(product)

    while test_products > 0:
        app.remove_from_cart()
        test_products -=1