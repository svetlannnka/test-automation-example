import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def wait_for_any_new_window(driver, old_windows, seconds):
    WebDriverWait(driver, seconds).until(
        lambda driver: old_windows != driver.window_handles)


def login(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()


def test_links(driver):
    driver.implicitly_wait(5)
    login(driver)
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_xpath("//td[@id='content']//a[@class='button' and contains(text(),'New Country')]").click()

    links = driver.find_elements_by_css_selector("i.fa.fa-external-link")

    for link in links:
        original_window = driver.current_window_handle
        old_windows = driver.window_handles

        link.click()
        wait_for_any_new_window(driver, old_windows, 5)
        # switching to new window
        new_window = driver.window_handles[1]
        driver.switch_to_window(new_window)
        driver.close()
        # and returning back
        driver.switch_to_window(original_window)