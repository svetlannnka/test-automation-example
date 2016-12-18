import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_cart(driver):
    wait = WebDriverWait(driver, 5)
    driver.get("http://localhost/litecart/en/")
    cart = "//div[@id='cart']//span[@class='quantity']"

    # getting first 3 product of the latest products category
    products = [l.get_attribute("href") for l in driver.find_elements_by_css_selector("div#box-latest-products a.link")][:3]
    for l in products:
        driver.get(l)
        # selecting size if required
        if len(driver.find_elements_by_name("options[Size]")) > 0:
            Select(driver.find_element_by_name("options[Size]")).select_by_index(1)

        items = int((driver.find_element_by_xpath(cart)).text)
        driver.find_element_by_name("add_cart_product").click()

        wait.until(EC.text_to_be_present_in_element((By.XPATH, cart), str(items+1)))
        driver.get("http://localhost/litecart/en/")

    driver.find_element_by_xpath(cart).click()

    i = len(products)
    while i > 0:
        # Checking deduction from total price by removing products 1 by 1
        prod_price = float(driver.find_element_by_xpath("//form[@name='cart_form']//p[contains(text(),'$')]").text[1:])
        total = float(driver.find_element_by_xpath("//tr[@class = 'footer']//strong[contains(text(),'$')]").text[1:])
        driver.find_element_by_name("remove_cart_item").click()

        if total - prod_price > 0:
            wait.until(EC.text_to_be_present_in_element((By.XPATH,
                        "//tr[@class = 'footer']//strong[contains(text(),'$')]"), str(total - prod_price)))
        elif total - prod_price == 0:
            print 'price is 0'
            wait.until(EC.text_to_be_present_in_element((By.XPATH, "//em"), "There are no items in your cart."))
        else:
            raise StandardError("Incorrect price: ", total - prod_price)

        i -= 1