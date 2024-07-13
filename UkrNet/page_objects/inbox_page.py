from selenium.webdriver.common.by import By

from UkrNet.utilities.web_ui.base_page import BasePage


class InboxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __user_email = (By.CSS_SELECTOR, 'p.login-button__user')

    def get_username(self):
        return self._get_text(self.__user_email).split('@')[0]

