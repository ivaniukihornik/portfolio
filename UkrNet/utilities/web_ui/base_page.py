import random
import string
import time

import allure
import pyperclip
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.__wait = WebDriverWait(self.driver, 10, 1)
        self.__fast_wait = WebDriverWait(self.driver, timeout=1, poll_frequency=0.1)
        self.__description = (By.XPATH, '//meta[@name="description"]')
        self.actions = ActionChains(driver)

    def __wait_until_element_located(self, locator, mode=''):
        match mode:
            case 'fast':
                return self.__fast_wait.until(EC.presence_of_element_located(locator))
            case _:
                return self.__wait.until(EC.presence_of_element_located(locator))

    def __wait_until_element_visible(self, locator):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def __wait_until_element_clickable(self, locator):
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def __hard_wait(self, seconds):
        time.sleep(seconds)
        return self

    def _open_page(self, url):
        self.driver.get(url)

    def _reload_page(self):
        self.__hard_wait(0.5).driver.refresh()

    def _back(self):
        self.driver.back()

    def _close_window(self):
        self.driver.close()

    def _make_screenshot(self, name='Screenshot', is_current_url_needed=False, with_hard_wait=False):
        if with_hard_wait:
            self.__hard_wait(0.5)
        if is_current_url_needed:
            allure.attach(f"Current URL: {self._get_current_url()}", name="Current URL",
                          attachment_type=allure.attachment_type.TEXT)
        allure.attach(self.driver.get_screenshot_as_png(), name, allure.attachment_type.PNG)

    def _click(self, locator):
        self.__wait_until_element_clickable(locator).click()

    def _input_text(self, locator, text, is_clear=False):
        if is_clear:
            self._select_text(locator)
            self._clear_text(locator)
        self.__wait_until_element_visible(locator).send_keys(text)

    def _clear_text(self, locator):
        self.__wait_until_element_visible(locator).send_keys(Keys.BACKSPACE)

    def _hold_mouse(self, locator):
        self.actions.click_and_hold(self.__wait_until_element_clickable(locator))
        self.actions.perform()

    def _release_mouse(self, locator):
        self.actions.release(self.__wait_until_element_clickable(locator))
        self.actions.perform()

    def _select_text(self, locator):
        self.__wait_until_element_clickable(locator).send_keys(Keys.CONTROL + 'a')

    def _copy_text_to_clipboard(self):
        self.driver.execute_script('document.execCommand("copy")')

    @staticmethod
    def _read_text_from_clipboard():
        return pyperclip.paste()

    @staticmethod
    def _lslice_text(text: str, length):
        return text[0:length]

    @staticmethod
    def _generate_random_number(min_value, max_value):
        return random.randint(min_value, max_value)

    @staticmethod
    def _generate_random_string(length):
        letters = string.ascii_letters
        numbers = string.digits
        punctuation = string.punctuation
        characters = letters + numbers + punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def _get_current_url(self):
        return self.driver.current_url

    def _get_text(self, locator):
        return self.__wait_until_element_visible(locator).text

    def _get_attribute(self, locator, attribute):
        return self.__wait_until_element_located(locator).get_attribute(attribute)

    def _get_title(self):
        return self.driver.title

    def _get_description(self):
        return self._get_attribute(self.__description, 'content')

    def _is_url_opened(self, url):
        try:
            self.__wait.until(EC.url_contains(url))
            return True
        except TimeoutException:
            return False

    def _is_selected(self, locator):
        try:
            return self.__wait_until_element_visible(locator).is_selected()
        except TimeoutException:
            return False

    def _is_displayed(self, locator, mode=''):
        try:
            return self.__wait_until_element_located(locator, mode).is_displayed()
        except TimeoutException:
            return False

    def _is_enabled(self, locator):
        try:
            return self.__wait_until_element_visible(locator).is_enabled()
        except TimeoutException:
            return False

    def _is_focused(self, locator):
        element = self.__wait_until_element_visible(locator)
        focused_element = self.driver.switch_to.active_element
        return element == focused_element

    def _is_target_blank_link(self, locator):
        try:
            return self._get_attribute(locator, 'target') == '_blank'
        except TimeoutException:
            return False
