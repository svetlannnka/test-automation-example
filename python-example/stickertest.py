import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_only_one_sticker(driver):
    # driver.implicitly_wait(5)
    driver.get("http://localhost/litecart/en/")
    products = driver.find_elements_by_css_selector("li.product")

    for product in products:
        # context search
        sticker = product.find_elements_by_css_selector("div.sticker")

        if len(sticker) != 1:
            print product.get_attribute('innerHTML')
            raise StandardError(" Ha! Wrong amount of stickers for element found! Should be 1 instead of %s. "
                                "Element-id: %s" % (len(sticker), product.id))
