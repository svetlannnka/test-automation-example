import pytest
from selenium import webdriver
from time import sleep

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


# Test to check country list sorting - 1a
def test_countries(driver):
    login(driver)
    driver.implicitly_wait(2)
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")

    # creating the list of countries from the page 'before list'
    countries = driver.find_elements_by_xpath("//form[@name = 'countries_form']//table//a[text()!=0]")
    countries_list = []
    for country in countries:
        countries_list.append(country.text)

    # list after sorting
    countries_list_sorted = sorted(countries_list)

    if countries_list_sorted != countries_list:
        raise StandardError("Countries not sorted alphabetically. "
                            "List should be: ", countries_list_sorted,
                            "instead of ", countries_list, ".")


# Test to check geo zones sorting inside countries with zones - 1b
def test_zones_for_countries(driver):
    login(driver)
    driver.implicitly_wait(2)
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")

    # searching for countries with zone pages td[6]>0
    zone_pages = driver.find_elements_by_xpath("//form[@name = 'countries_form']//tr[@class ='row' and ./td[6]>0]//a[text()!=0]")
    page_count = len(zone_pages)

    while page_count > 0:
        e = driver.find_elements_by_xpath("//form[@name = 'countries_form']//tr[@class ='row' and ./td[6]>0]//a[text()!=0]")
        e[page_count-1].click()

        # creating the list of zones from the page
        zones = driver.find_elements_by_xpath("//table[@id = 'table-zones']//td[text()!=0][3]")
        zones_list = []
        for zone in zones:
            zones_list.append(zone.text)

        # list after sorting
        zones_list_sorted = sorted(zones_list)

        if zones_list_sorted != zones_list:
            raise StandardError("Countries not sorted alphabetically. "
                                "List should be: ", zones_list_sorted,
                                "instead of ", zones_list, ".")

        page_count -= 1
        driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")


# Test to check country list sorting - 2
def test_zones_page(driver):
    login(driver)
    driver.implicitly_wait(2)
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")

    zone_pages = driver.find_elements_by_xpath("//form[@name = 'geo_zones_form']//tr[@class ='row']//a[text()!=0]")
    page_count = len(zone_pages)

    while page_count > 0:
        e = driver.find_elements_by_xpath("//form[@name = 'geo_zones_form']//tr[@class ='row']//a[text()!=0]")
        e[page_count-1].click()

        # creating the list of zones from the page, collecting only shown 'selected' elements
        zones = driver.find_elements_by_xpath("//table[@id = 'table-zones']//td[3]//option[@selected='selected']")
        zones_list = []
        for zone in zones:
            zones_list.append(zone.text)

        # list after sorting
        zones_list_sorted = sorted(zones_list)

        if zones_list_sorted != zones_list:
            raise StandardError("Countries not sorted alphabetically. "
                                "List should be: ", zones_list_sorted,
                                "instead of ", zones_list, ".")

        page_count -= 1
        driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")