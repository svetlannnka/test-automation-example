from selenium.webdriver.support.wait import WebDriverWait


class StorePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/en/")
        return self

    def find_product_urls(self, prod_amount):
        product_urls = [l.get_attribute("href") for l in
                    self.driver.find_elements_by_css_selector("div#box-latest-products a.link")][:prod_amount]
        return product_urls
