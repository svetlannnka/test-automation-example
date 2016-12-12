import pytest
from selenium import webdriver
from time import strftime


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

# it makes sense to pull it in a class, but I made it easy
user_data = {"firstname": "Lana", "lastname": "Test", "address1": "Address", "postcode": "123456", "city": "Test",
                 "phone": "123456789", "email": ("test" + strftime("%Y%m%d_%H%M%S") + "@test.com"),
                 "password": "Passw0rd.", "confirmed_password": "Passw0rd."}
k = user_data.keys()
v = user_data.values()
user_email = user_data['email']
user_pw = user_data['password']


def find_name_send_keys(driver,name,keys):
    driver.find_element_by_name(name).send_keys(keys)


def login(driver):
    find_name_send_keys(driver, "email", user_email)
    find_name_send_keys(driver, "password", user_pw)
    driver.find_element_by_name("login").click()


def logout(driver):
    driver.find_element_by_xpath("//div[@id = 'box-account']//a[text()='Logout']").click()


def test_registration(driver):
    driver.implicitly_wait(2)
    driver.get("http://localhost/litecart/en/create_account")

    # registration form, using keys and values from data dict above
    for k, v in user_data.items():
        find_name_send_keys(driver, k, v)
    driver.find_element_by_name("create_account").click()

    logout(driver)
    login(driver)
    logout(driver)