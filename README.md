## QA: Selenium Test Automation Project

_written in_
#### Python 2.7 / Selenium / pytest

The project is created to outline most popular Selenium WebDriver
commands and their usage.

Application Under Test is [LiteCart E-commerce Platform](https://www.litecart.net/download)

##### Subjects covered in this project:
- locating elements
- navigation and interaction with elements
- working with alerts, frames, WebDriver window handle
- waits
- browser capabilities
- most common webDriver Exceptions
- PageObjects

#### How to run:

**Installation.**
Running tests locally requires you to have browser drivers installed on your machine.
For more details, check out [Selenuim and Python: drivers and installation](https://pypi.python.org/pypi/selenium).

For test execution you need to have Application Under Test installed locally, it can be downloaded here: [LiteCart E-commerce Platform](https://www.litecart.net/download)
If you do not have local server, you can use a free solution from [MAMP](https://www.mamp.info/en/).

**To run the tests** - run any *test.py file. Each file contains full steps for each actomates test scenario.

To check out **PageObject implementation**, run _tests/productcart_test.py_.
It will initialize app class (_application.py_) that contains references to page classes.
```python
    def test_cart(app):
        test_products = 2
        products = app.get_product_links(test_products)
```

**Pages package** contains sample classes and methods for web pages automation.




#### Useful links:
- [Selenuim and Python: drivers and installation](https://pypi.python.org/pypi/selenium)
- [Selenium and Python: how to, main classes and methods](http://selenium-python.readthedocs.io/installation.html)
- [Python 3, Anaconda Download](https://www.continuum.io/downloads)
- [Python 3, Anaconda, work with environments](https://www.continuum.io/blog/developer-blog/python-3-support-anaconda)
- [Detailed class description](http://software-testing.ru/edu/1-schedule/242-selenium-webdriver)



#### Happy testing!