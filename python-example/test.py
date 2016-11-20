import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("https://www.whil.com/welcome")
    driver.find_element_by_id("login").click()
    WebDriverWait(driver, 10).until(EC.title_contains("Whil - Login"))