from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/en/checkout")
        sleep(1)
        return self

    def get_prod_price(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,"//form[@name='cart_form']//p[contains(text(),'$')]")))
        prod_price = float(self.driver.find_element_by_xpath("//form[@name='cart_form']//p[contains(text(),'$')]").text[1:])
        return prod_price

    def get_total(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,"//tr[@class = 'footer']//strong[contains(text(),'$')]")))
        total = float(self.driver.find_element_by_xpath("//tr[@class = 'footer']//strong[contains(text(),'$')]").text[1:])
        return total

    def remove_from_cart(self):
        self.wait.until(EC.visibility_of_element_located((By.NAME,"remove_cart_item")))
        self.driver.find_element_by_name("remove_cart_item").click()

    def check_if_correct_price(self,prod_price,total):
        if total - prod_price > 0:
            self.wait.until(EC.text_to_be_present_in_element((By.XPATH,
                        "//tr[@class = 'footer']//strong[contains(text(),'$')]"), str(total - prod_price)))
        elif total - prod_price == 0:
            print 'price is 0'
            self.wait.until(EC.text_to_be_present_in_element((By.XPATH, "//em"), "There are no items in your cart."))
        else:
            raise StandardError("Incorrect price: ", total - prod_price)
