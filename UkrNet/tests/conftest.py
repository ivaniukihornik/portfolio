import csv
import json
import time
from typing import Literal

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
    driver = DriverFactory.create_driver(driver_id=conf.browser_id)
    driver.maximize_window()
    yield driver
    time.sleep(2)  # Using delay between requests not to be banned by urk.net
    driver.quit()


@pytest.fixture()
@allure.title('Open Login Page')
def open_login_page(create_driver):
    create_driver.get(urls.LOGIN_PAGE_URL)
    return LoginPage(create_driver)


@pytest.fixture()
@allure.title('Open Inbox Page')
def open_inbox_page(create_driver, open_login_page, conf):
    login_page = open_login_page
    login_page.login(conf.default_account_username, conf.default_account_password)
    if login_page._is_url_opened(urls.INBOX_PAGE_URL):
        return InboxPage(create_driver)


@pytest.fixture()
@allure.title('Create Inbox Page')
def create_inbox_page(create_driver):
    return InboxPage(create_driver)


@pytest.fixture()
@allure.title('Get data driven test cases')
def get_data_driven_test_cases():
    return {
        '9': ('https://app.qase.io/case/PF-9', 'Login with existent credentials'),
        '10': ('https://app.qase.io/case/PF-10', 'Login with existent username and nonexistent password'),
        '11': ('https://app.qase.io/case/PF-11', 'Login with nonexistent username and existent password'),
        '90': ('https://app.qase.io/case/PF-90', 'Login with username containing only spaces'),
        '91': ('https://app.qase.io/case/PF-91', 'Login with username beginning and ending with spaces'),
    }


def read_test_data(module: Literal['login']):
    with open(f'{ROOT_DIR}/configuration/test_data/{module}_data.csv', 'r') as file:
        test_data = []
        next(file)
        csv_reader = csv.reader(file)
        for row in csv_reader:
            test_data.append(row)
        file.close()
        return test_data


def pytest_generate_tests(metafunc):
    if 'valid_login_test_data' in metafunc.fixturenames:
        test_data = [row for row in read_test_data('login') if 'valid_data' in row]
        metafunc.parametrize('valid_login_test_data', test_data)
    elif 'nonexistent_login_test_data' in metafunc.fixturenames:
        test_data = [row for row in read_test_data('login') if 'nonexistent_data' in row]
        metafunc.parametrize('nonexistent_login_test_data', test_data)
    elif 'only_spaces_login_test_data' in metafunc.fixturenames:
        test_data = [row for row in read_test_data('login') if 'only_spaces' in row]
        metafunc.parametrize('only_spaces_login_test_data', test_data)
