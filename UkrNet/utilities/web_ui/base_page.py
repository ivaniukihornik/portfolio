import random
import string
import time
from typing import Literal

import allure
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.__wait = WebDriverWait(self.driver, 10, 1)
        self.__fast_wait = WebDriverWait(self.driver, timeout=1, poll_frequency=0.1)
        self.actions = ActionChains(driver)

    __description = (By.XPATH, '//meta[@name="description"]')
    __html_language_code = (By.XPATH, '//html[@lang]')
    __head_language_code = (By.XPATH, '//head[@lang]')

    def __wait_until_element_located(self, locator: tuple[str, str], mode: Literal['default', 'fast'] = 'default'):
        """Waits for element to be present in DOM tree of page and returns it if it is or raises TimeoutException if it
        is not. Mode describes the amount of time to wait"""
        match mode:
            case 'fast':
                return self.__fast_wait.until(EC.presence_of_element_located(locator))
            case _:
                return self.__wait.until(EC.presence_of_element_located(locator))

    def __wait_until_element_visible(self, locator: tuple[str, str]):
        """Waits for element to be visible on page and returns it if it is or raises TimeoutException if it is not."""
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def __wait_until_element_clickable(self, locator: tuple[str, str]) -> WebElement:
        """Waits for element to be clickable on page and returns it if it is or raises TimeoutException if it is not."""
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def _hard_wait(self, seconds: [int, float]):
        """Sleeps for obtained period in seconds"""
        time.sleep(seconds)
        return self

    def _open_page(self, url: str):
        self.driver.get(url)

    def _reload_page(self, with_hard_wait: bool = False):
        """Reloads page. If 'with_hard_wait', waits 0.5 sec before refreshing"""
        if with_hard_wait:
            self._hard_wait(0.5)
        self.driver.refresh()

    def _back(self):
        self.driver.back()

    def _switch_to_tab(self, tab: int):
        """Switches to tab"""
        self.driver.switch_to.window(self._get_window_handles()[tab - 1])

    def _close_current_tab(self, is_switching_to_first_tab_needed: bool = False):
        """Closes current tab. If 'is_switching_to_first_tab_needed', switches driver to the first tab"""
        self.driver.close()
        if is_switching_to_first_tab_needed:
            self._switch_to_tab(1)

    def _make_screenshot(self, name: str = 'Screenshot', is_current_url_needed: bool = False,
                         with_hard_wait: bool = False):
        """Makes a screenshot of page current state for allure report. Can take arguments:
           \n\t- name: screenshot name;
           \n\t- is_current_url_needed: if current url is needed to be attached;
           \n\t- with_hard_wait: if some pause is needed before making a screenshot"""
        if with_hard_wait:
            self._hard_wait(0.5)
        if is_current_url_needed:
            allure.attach(f'Current URL: {self._get_current_url()}', name='Current URL',
                          attachment_type=allure.attachment_type.TEXT)
        allure.attach(self.driver.get_screenshot_as_png(), name, allure.attachment_type.PNG)

    def _click(self, locator: tuple[str, str]) -> None:
        try:
            self.__wait_until_element_clickable(locator).click()
        except ElementClickInterceptedException:
            self._click(locator)

    def _input_text(self, locator: tuple[str, str], text: str, is_clear: bool = False):
        """Inputs text to field by locator. Clears the field before inputting if 'is_clear' argument is True"""
        if is_clear:
            self._clear_text(locator)
        self.__wait_until_element_visible(locator).send_keys(text)

    def _clear_text(self, locator: tuple[str, str]):
        self._select_text(locator)
        self.__wait_until_element_clickable(locator).send_keys(Keys.BACKSPACE)

    def _hold_mouse(self, locator: tuple[str, str]):
        self.actions.click_and_hold(self.__wait_until_element_clickable(locator))
        self.actions.perform()

    def _release_mouse(self, locator: tuple[str, str]) -> None:
        self.actions.release(self.__wait_until_element_clickable(locator))
        self.actions.perform()

    def _unfocus_field(self, locator: tuple[str, str]) -> None:
        self.driver.execute_script('arguments[0].blur();', self.__wait_until_element_visible(locator))

    def _scroll_to_page_position(self, page_position: Literal['top', 'bottom']):
        """Scrolls to specified page position"""
        match page_position:
            case 'top':
                self.driver.execute_script('window.scrollTo(0, 0);')
            case 'bottom':
                self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def _scroll_to_element(self, locator: tuple[str, str]):
        self.actions.scroll_to_element(self.__wait_until_element_visible(locator)).perform()

    def _select_text(self, locator: tuple[str, str]):
        self.__wait_until_element_clickable(locator).send_keys(Keys.CONTROL + 'a')

    @staticmethod
    def _lslice_text(text: str, length: int) -> str:
        """Returns the first part of obtained text of specified length"""
        return text[0:length]

    @staticmethod
    def _generate_random_number(min_value: int, max_value: int) -> int:
        """Returns random integer in specified range, including both end points"""
        return random.randint(min_value, max_value)

    @staticmethod
    def _generate_random_string(length: int) -> str:
        """Returns random string of specific length"""
        letters = string.ascii_letters
        numbers = string.digits
        punctuation = string.punctuation
        characters = letters + numbers + punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def _get_current_url(self) -> str:
        return self.driver.current_url

    def _get_window_handles(self) -> list:
        """Returns the handles of all windows within the current session"""
        return self.driver.window_handles

    def _get_elements(self, locator: tuple[str, str]) -> list:
        """Returns the list of all elements found on page by specific locator"""
        self.__wait_until_element_visible(locator)
        return self.driver.find_elements(*locator)

    def _get_text(self, locator: [tuple, WebElement], is_element=False) -> str:
        if is_element:
            element: WebElement = locator
            return element.text
        return self.__wait_until_element_visible(locator).text

    def _get_attribute(self, locator: tuple[str, str], attribute: str) -> str:
        return self.__wait_until_element_located(locator).get_attribute(attribute)

    def _get_title(self) -> str:
        return self.driver.title

    def _get_description(self) -> str:
        return self._get_attribute(self.__description, 'content')

    def _get_selected_text(self) -> str:
        return self.driver.execute_script('return window.getSelection().toString()')

    def _get_html_language_code(self) -> str:
        """Returns language code from <html lang="{}"> tag"""
        return self._get_attribute(self.__html_language_code, 'lang')

    def _get_head_language_code(self) -> str:
        """Returns language code from <head lang="{}"> tag"""
        return self._get_attribute(self.__head_language_code, 'lang')

    def _is_url_opened(self, url: str) -> bool:
        try:
            self.__wait.until(EC.url_contains(url))
        except TimeoutException:
            return False
        else:
            return True

    def _is_displayed(self, locator: tuple[str, str], mode: Literal['default', 'fast'] = 'default') -> bool:
        """Returns True if element is displayed on the page or False otherwise.
        'mode' parameter determines the time for expectation of displaying."""
        try:
            return self.__wait_until_element_located(locator, mode).is_displayed()
        except TimeoutException:
            return False

    def _is_enabled(self, locator: tuple[str, str]) -> bool:
        try:
            return self.__wait_until_element_visible(locator).is_enabled()
        except TimeoutException:
            return False

    def _is_focused(self, locator: tuple[str, str]) -> bool:
        """Determines current focused element and compares it with element found by obtained locator"""
        element = self.__wait_until_element_visible(locator)
        focused_element = self.driver.switch_to.active_element
        return element == focused_element

    def _is_link_opened_in_new_tab(self, is_switching_to_new_tab_needed: bool = False) -> bool:
        """Verifies if link was opened in new tab ind switches driver to it if 'is_switching_to_new_tab_needed'"""
        try:
            self.__fast_wait.until(EC.number_of_windows_to_be(2))
        except TimeoutException:
            return False
        else:
            if is_switching_to_new_tab_needed:
                self._switch_to_tab(2)
            return True
