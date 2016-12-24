from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self,prod_url):
        self.driver.get(prod_url)
        return self

    def select(self):
        if len(self.driver.find_elements_by_name("options[Size]")) > 0:
            Select(self.driver.find_element_by_name("options[Size]")).select_by_index(1)

    def items_count(self):
        items = int((self.driver.find_element_by_xpath("//div[@id='cart']//span[@class='quantity']")).text)
        return items

    def add_to_cart(self):
        self.driver.find_element_by_name("add_cart_product").click()

    def wait_prod_added(self,item):
        self.wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div[@id='cart']//span[@class='quantity']"),
                                                         str(item)))

    def go_to_cart(self):
        self.driver.find_element_by_xpath("//div[@id='cart']//span[@class='quantity']").click()