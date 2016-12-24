import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


# Test product name and price
def test_product(driver):
    driver.implicitly_wait(2)
    driver.get("http://localhost/litecart/en/")

    # by default driver will pick the first one
    e = driver.find_element_by_css_selector("div#box-campaigns a.link")
    name = e.find_element_by_css_selector("div.name").text
    reg_price = e.find_element_by_css_selector("s.regular-price").text
    camp_price = e.find_element_by_css_selector("strong.campaign-price").text

    e.click()

    e = driver.find_element_by_css_selector("div#box-product")
    name_pr = e.find_element_by_css_selector("h1.title").text
    reg_price_pr = e.find_element_by_css_selector("s.regular-price").text
    camp_price_pr = e.find_element_by_css_selector("strong.campaign-price").text

    assert name == name_pr
    assert reg_price == reg_price_pr
    assert camp_price == camp_price_pr


# Test CSS on 2 diff page
def test_styles(driver):
    driver.implicitly_wait(2)
    driver.get("http://localhost/litecart/en/")

    # by default driver will pick the first one
    e = driver.find_element_by_css_selector("div#box-campaigns a.link")

    # styles
    css_props = ['color','text-decoration','font-weight']
    styles_reg_price = []
    styles_camp_price = []
    for prop in css_props:
        styles_reg_price.append(e.find_element_by_css_selector("s.regular-price").value_of_css_property(prop))
        styles_camp_price.append(e.find_element_by_css_selector("strong.campaign-price").value_of_css_property(prop))

    e.click()

    e = driver.find_element_by_css_selector("div#box-product")
    styles_reg_price_new = []
    styles_camp_price_new = []
    for prop in css_props:
        styles_reg_price_new.append(e.find_element_by_css_selector("s.regular-price").value_of_css_property(prop))
        styles_camp_price_new.append(e.find_element_by_css_selector("strong.campaign-price").value_of_css_property(prop))

    assert styles_camp_price == styles_camp_price_new
    assert styles_reg_price == styles_reg_price_new # test fails: different shades of gray