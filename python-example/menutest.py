import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_menu(driver):
    # driver.implicitly_wait(5)
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    menu_items = driver.find_elements_by_css_selector("li#app-")
    item_count = len(menu_items)

    while item_count > 0:
        driver.find_element_by_css_selector("li#app-:nth-of-type(%d)" % item_count).click()
        # sleep(1)
        sub_menu_items = driver.find_elements_by_css_selector("li#app-.selected li")
        sub_item_count = len(sub_menu_items)

        while sub_item_count > 0:
            driver.find_element_by_css_selector("li#app-.selected li:nth-of-type(%d)" % sub_item_count).click()
            WebDriverWait(driver, 5).until(EC.title_contains("My Store"))
            sub_item_count -= 1

        item_count -= 1
