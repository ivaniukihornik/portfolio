import json
import time

import allure
import pytest

from UkrNet.constants import ROOT_DIR
from UkrNet.environments import urls
from UkrNet.page_objects.inbox_page import InboxPage
from UkrNet.page_objects.login_page import LoginPage
from UkrNet.utilities.configuration import Configuration
from UkrNet.utilities.driver_factory import DriverFactory


@allure.title('Connect config file')
@pytest.fixture(scope='session', autouse=True)
def conf():
    with open(f'{ROOT_DIR}/configuration/config.json', 'r') as file:
        conf_dict = json.loads(file.read())
    return Configuration(**conf_dict)


@allure.title('Create webdriver')
@pytest.fixture()
def create_driver(conf):
    # time.sleep(3)  # Using delay between requests not to be banned by urk.net
    driver = DriverFactory.create_driver(driver_id=conf.browser_id)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
@allure.title('Open Login Page')
def open_login_page(create_driver):
    create_driver.get(urls.LOGIN_PAGE_URL)
    return LoginPage(create_driver)


@pytest.fixture()
@allure.title('Create Inbox Page')
def create_inbox_page(create_driver):
    return InboxPage(create_driver)
