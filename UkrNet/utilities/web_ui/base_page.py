import random
import string
import time
from typing import Literal

import allure
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

    def __wait_until_element_located(self, locator, mode: Literal['default', 'fast'] = 'default'):
        """Waits for element to be present in DOM tree of page and returns it if it is or raises TimeoutException if it
        is not. Mode describes the amount of time to wait"""
        match mode:
            case 'fast':
                return self.__fast_wait.until(EC.presence_of_element_located(locator))
            case _:
                return self.__wait.until(EC.presence_of_element_located(locator))

    def __wait_until_element_visible(self, locator):
        """Waits for element to be visible on page and returns it if it is or raises TimeoutException if it is not."""
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def __wait_until_element_clickable(self, locator):
        """Waits for element to be clickable on page and returns it if it is or raises TimeoutException if it is not."""
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def _hard_wait(self, seconds):
        time.sleep(seconds)
        return self

    def _open_page(self, url):
        self.driver.get(url)

    def _reload_page(self):
        self._hard_wait(0.5).driver.refresh()

    def _back(self):
        self.driver.back()

    def _switch_to_tab(self, tab: int):
        """Switches to tab"""
        self.driver.switch_to.window(self._get_window_handles()[tab - 1])

    def _close_current_tab(self, is_switching_to_first_tab_needed=False):
        self.driver.close()
        if is_switching_to_first_tab_needed:
            self._switch_to_tab(1)

    def _make_screenshot(self, name='Screenshot', is_current_url_needed=False, with_hard_wait=False):
        """Makes a screenshot of page current state for allure report. Can take arguments:
           \n\t- name: screenshot name;
           \n\t- is_current_url_needed: if current url is needed to be attached;
           \n\t- with_hard_wait: if some pause is needed before making a screenshot"""
        if with_hard_wait:
            self._hard_wait(0.5)
        if is_current_url_needed:
            allure.attach(f"Current URL: {self._get_current_url()}", name="Current URL",
                          attachment_type=allure.attachment_type.TEXT)
        allure.attach(self.driver.get_screenshot_as_png(), name, allure.attachment_type.PNG)

    def _click(self, locator):
        self.__wait_until_element_clickable(locator).click()

    def _input_text(self, locator, text, is_clear=False):
        """Inputs text to field by locator. Clears the field before inputting if 'is_clear' argument is True"""
        if is_clear:
            self._clear_text(locator)
        self.__wait_until_element_visible(locator).send_keys(text)

    def _clear_text(self, locator):
        self._select_text(locator)
        self.__wait_until_element_clickable(locator).send_keys(Keys.BACKSPACE)

    def _hold_mouse(self, locator):
        self.actions.click_and_hold(self.__wait_until_element_clickable(locator))
        self.actions.perform()

    def _release_mouse(self, locator):
        self.actions.release(self.__wait_until_element_clickable(locator))
        self.actions.perform()

    def _scroll_to_page_position(self, page_position: Literal['top']):
        match page_position:
            case 'top':
                self.driver.execute_script("window.scrollTo(0, 0);")

    def _scroll_to_element(self, locator: tuple):
        self.actions.scroll_to_element(self.__wait_until_element_visible(locator)).perform()

    def _select_text(self, locator):
        self.__wait_until_element_clickable(locator).send_keys(Keys.CONTROL + 'a')

    @staticmethod
    def _lslice_text(text, length):
        """Returns the first part of obtained text of specified length"""
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

    def _get_window_handles(self):
        return self.driver.window_handles

    def _get_elements(self, locator):
        self.__wait_until_element_visible(locator)
        return self.driver.find_elements(*locator)

    def _get_text(self, locator):
        return self.__wait_until_element_visible(locator).text

    def _get_attribute(self, locator, attribute):
        return self.__wait_until_element_located(locator).get_attribute(attribute)

    def _get_title(self):
        return self.driver.title

    def _get_description(self):
        return self._get_attribute(self.__description, 'content')

    def _get_selected_text(self):
        return self.driver.execute_script('return window.getSelection().toString()')

    def _is_url_opened(self, url):
        try:
            self.__wait.until(EC.url_contains(url))
            return True
        except TimeoutException:
            return False

    def _is_displayed(self, locator, mode: Literal['default', 'fast'] = 'default'):
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

    def _is_link_opened_in_new_tab(self, is_switching_to_new_tab_needed=False):
        try:
            self.__fast_wait.until(EC.number_of_windows_to_be(2))
            if is_switching_to_new_tab_needed:
                self._switch_to_tab(2)
            return True
        except TimeoutException:
            return False
