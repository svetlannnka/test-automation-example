import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def login(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()


def test_catalog_logs(driver):
    driver.implicitly_wait(2)
    login(driver)
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")

    products = len(driver.find_elements_by_xpath("//table[@class = 'dataTable']//tr[.//img]//a[text()!=0]"))
    while products > 0:
        driver.find_elements_by_xpath("//table[@class = 'dataTable']//tr[.//img]//a[text()!=0]")[products-1].click()
        for l in driver.get_log('browser'):
            print 'Logs:\n',l
        products -= 1
        driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")


def test_whil_reg(driver):
    # Took a page with WARNINGs to make sure it actually works
    driver.get("https://www.whil.com/")
    for l in driver.get_log('browser'):
            print 'Logs (2nd test):\n',l