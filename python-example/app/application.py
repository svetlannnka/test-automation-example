from selenium import webdriver
from pages.store_page import StorePage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.store_page = StorePage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

    def quit(self):
        self.driver.quit()

    def implicitly_wait(self,time):
        self.driver.implicitly_wait(time)

    def get_product_links(self,amount):
        self.store_page.open()
        product_urls = self.store_page.find_product_urls(amount)
        return product_urls

    def add_product_to_cart(self,url):
        self.product_page.open(url)
        items = self.product_page.items_count()
        self.product_page.select()
        self.product_page.add_to_cart()
        self.product_page.wait_prod_added(items+1)

    def remove_from_cart(self):
        self.checkout_page.open()
        total = self.checkout_page.get_total()
        prod_price = self.checkout_page.get_prod_price()
        self.checkout_page.remove_from_cart()
        self.checkout_page.check_if_correct_price(prod_price, total)