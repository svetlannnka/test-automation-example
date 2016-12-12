import pytest
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def find_name_send_keys(driver,name,keys):
    driver.find_element_by_name(name).send_keys(keys)


def login(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    find_name_send_keys(driver,"username","admin")
    find_name_send_keys(driver, "password", "admin")
    driver.find_element_by_name("login").click()


def checkbox_select(cb):
    if not cb.is_selected():
        cb.click()


def test_next_product(driver):
    driver.implicitly_wait(2)
    login(driver)
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
    driver.find_element_by_xpath("//a[@class = 'button' and contains(text(),'Add New Product')]").click()
    path = os.path.join(os.path.dirname(os.getcwd()), 'img', 'bird.png')  # path to image

    # Add New product page - General tab
    general_data = {"name[en]": "Blue Bird Test Product", "code": "12345", "new_images[]": path,
                    "date_valid_from": "02012016","date_valid_to":"02012017"}
    k = general_data.keys()
    v = general_data.values()
    pr_name = general_data['name[en]']
    for k, v in general_data.items():
        find_name_send_keys(driver, k, v)

    driver.find_element_by_xpath("//label[contains(text(),'Enabled')]").click()
    checkbox_select(driver.find_element_by_xpath("//input[@data-name = 'Rubber Ducks']"))
    checkbox_select(driver.find_element_by_xpath("//tr[./td[text()='Unisex']]//input"))

    amount = driver.find_element_by_name("quantity")
    amount.clear()
    amount.send_keys("1")
    Select(driver.find_element_by_name("sold_out_status_id")).select_by_visible_text("Temporary sold out")

    # Information tab
    driver.find_element_by_xpath("//div[@class='tabs']//a[text()='Information']").click()
    information_data = {"keywords": "Blue Bird, Bird", "short_description[en]": "Best Blue Bird Ever",
                        "head_title[en]": "Blue Bird", "meta_description[en]": "Blue Bird. Best one."}
    k = information_data.keys()
    v = information_data.values()
    for k, v in information_data.items():
        find_name_send_keys(driver, k, v)

    Select(driver.find_element_by_name("manufacturer_id")).select_by_visible_text("ACME Corp.")
    driver.find_element_by_class_name("trumbowyg-editor").send_keys("Best Blue Bird Ever. Guaranteed.")

    # Prices tab
    driver.find_element_by_xpath("//div[@class='tabs']//a[text()='Prices']").click()
    price = driver.find_element_by_name("purchase_price")
    price.clear()
    price.send_keys("7.77")

    Select(driver.find_element_by_name("purchase_price_currency_code")).select_by_visible_text("US Dollars")
    new_price = "17.77"
    driver.find_element_by_name("prices[USD]").send_keys(new_price)
    driver.find_element_by_name("save").click()  # Saving

    # Making sure the product got created is Admin Catalog
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
    driver.find_element_by_xpath("//table[@class = 'dataTable']//a[text()='%s']" % pr_name)  # searching for new pr Name

    # Making sure the product got created in Store
    driver.get("http://localhost/litecart/en/")
    # Searching among Latest Products, looking for Name and Price of the new product
    driver.find_element_by_xpath("//div[@id='box-latest-products']//a[.//div"
        "[@class='name' and text()= '%s'] and .//span[@class='price' and text() = '$%s']]" % (pr_name, new_price))