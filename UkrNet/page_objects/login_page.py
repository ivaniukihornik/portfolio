from typing import Literal

from selenium.webdriver.common.by import By
from UkrNet.utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __login_form_title = (By.CSS_SELECTOR, 'h2.DhiDxejH')

    __login_field = (By.XPATH, '//input[@name="login"]')
    __login_field_name = (__login_field[0], f'{__login_field[1]}/ancestor::*[contains(@class, "mJOT30ua")]//label')
    __login_field_underline_green = (__login_field[0], f'{__login_field[1]}'
                                                       f'/ancestor::*[contains(@class, "_2xcBpEBl")]')
    __login_field_underline_orange = (__login_field[0], f'{__login_field[1]}'
                                                        f'/ancestor::*[contains(@class, "_3zE00K5Z")]')
    __email_domain = (By.CSS_SELECTOR, 'span._2wDvNoc7')

    __password_field = (By.XPATH, '//input[@name="password"]')
    __password_field_name = (__password_field[0], f'{__password_field[1]}/ancestor::*[contains(@class,'
                                                  f' "mJOT30ua")]//label')
    __password_field_underline_green = (__password_field[0], f'{__password_field[1]}//ancestor::*[contains(@class,'
                                                             f' "_2xcBpEBl")]')
    __password_field_underline_orange = (__password_field[0], f'{__password_field[1]}//ancestor::*[contains(@class,'
                                                              f' "_3zE00K5Z")]')
    __password_eye = (__password_field[0], f'{__password_field[1]}/ancestor::div/button')
    __password_eye_state = (__password_eye[0], f'{__password_eye[1]}//*[name()="use"]')

    __error_message = (By.CSS_SELECTOR, 'p._3ctepfDF')

    __google_play_badge = (By.CSS_SELECTOR, 'a._3eUlYfeH:nth-child(1)')
    __app_store_badge = (By.CSS_SELECTOR, 'a._3eUlYfeH:nth-child(2)')

    __animation = (By.CSS_SELECTOR, 'button._3ZaS2DCq')
    __animation_item_switcher = (By.XPATH, '//button[contains(@class, "_3ZaS2DCq")][@data-index={}]')
    __animation_title = (By.XPATH, '//*[contains(@class, "zMtDsG7W")][{}]/h2')
    __animation_paragraph = (By.XPATH, '//*[contains(@class, "zMtDsG7W")][{}]/p')

    __public_computer_checkbox_name = (By.CSS_SELECTOR, 'div._30hjWeHY')

    __continue_button = (By.XPATH, '//button[@type="submit"]')

    __trouble_sign_in_link = (By.CSS_SELECTOR, 'a._3PrwZZRJ:nth-child(1)')
    __sign_up_link = (By.CSS_SELECTOR, 'a._3PrwZZRJ:nth-child(2)')

    __apps_title = (By.CSS_SELECTOR, 'p._1zLZRANz')

    __support_title = (By.CSS_SELECTOR, 'div.WO9yyhGJ')

    __support_mail_icon = (By.XPATH, '//*[@class="_1VAZ3WYQ"][1]//*[name()="use"][@*[name()="xlink:href"'
                                     ' and .="/login/assets/file-20d110f0.svg#icon-support-email-4cea"]]')
    __support_mail_content = (By.XPATH, '//*[@class="_1VAZ3WYQ"][1]')

    __support_vodafone_icon = (By.XPATH, '//*[@class="_1VAZ3WYQ"][2]//*[name()="use"][@*[name()="xlink:href"'
                                         ' and .="/login/assets/file-20d110f0.svg#icon-support-vodafone-5f9c"]]')
    __support_vodafone_content = (By.XPATH, '//*[@class="_1VAZ3WYQ"][2]')

    __support_kyivstar_icon = (By.XPATH, '//*[@class="_1VAZ3WYQ"][3]//*[name()="use"][@*[name()="xlink:href"'
                                         ' and .="/login/assets/file-20d110f0.svg#icon-support-kyivstar-0398"]]')
    __support_kyivstar_content = (By.XPATH, '//*[@class="_1VAZ3WYQ"][3]')

    __privacy_policy_link = (By.XPATH, '//*[@class="_31Ul8LLC"][1]/a')
    __terms_of_service_link = (By.XPATH, '//*[@class="_31Ul8LLC"][2]/a')

    __selected_language = (By.CSS_SELECTOR, 'button._15CzUyms')
    __language_button = __selected_language
    __language_to_select = (By.XPATH, '//button[@class="Ii4YrhIX"][text()="{}"]')

    __language_dropdown = (By.CSS_SELECTOR, 'div._1zRGeyrM')
    __language_dropdown_icon = (By.CSS_SELECTOR, f'{__language_button[1]} > svg')
    __language_dropdown_item = (By.CSS_SELECTOR, 'button.Ii4YrhIX')
    __language_dropdown_selected_item = (By.XPATH, '//button[@class="Ii4YrhIX"]/*[name()="svg"]/ancestor::button')

    def __get_animation_title(self, animation_number: int) -> str:
        """Returns <h2> header content of animation by animation number"""
        return self.switch_animation(animation_number)._get_text(
            (self.__animation_title[0], self.__animation_title[1].format(animation_number)))

    def __get_animation_paragraph(self, animation_number: int) -> str:
        """Returns <p> content of animation by animation number"""
        return self.switch_animation(animation_number)._get_text(
            (self.__animation_paragraph[0], self.__animation_paragraph[1].format(animation_number)))

    def __get_login_form_title(self) -> str:
        return self._get_text(self.__login_form_title)

    def __get_login_field_name(self) -> str:
        return self._get_text(self.__login_field_name)

    def __get_email_domain(self) -> str:
        return self._get_text(self.__email_domain)

    def __get_password_field_name(self) -> str:
        return self._get_text(self.__password_field_name)

    def __get_public_computer_checkbox_name(self) -> str:
        return self._get_text(self.__public_computer_checkbox_name)

    def __get_continue_button_name(self) -> str:
        return self._get_text(self.__continue_button)

    def __get_trouble_sign_in_link_name(self) -> str:
        return self._get_text(self.__trouble_sign_in_link)

    def __get_sign_up_link_name(self) -> str:
        return self._get_text(self.__sign_up_link)

    def __get_apps_title(self) -> str:
        return self._get_text(self.__apps_title)

    def __get_support_title(self) -> str:
        return self._get_text(self.__support_title)

    def __get_support_mail_content(self) -> str:
        return self._get_text(self.__support_mail_content)

    def __get_support_vodafone_content(self) -> str:
        return self._get_text(self.__support_vodafone_content)

    def __get_support_kyivstar_content(self) -> str:
        return self._get_text(self.__support_kyivstar_content)

    def __get_privacy_policy_link_name(self) -> str:
        return self._get_text(self.__privacy_policy_link)

    def __get_terms_of_service_link_name(self) -> str:
        return self._get_text(self.__terms_of_service_link)

    def switch_animation(self, animation_number: int):
        """Switches the animation to obtained number"""
        self._click((self.__animation_item_switcher[0], self.__animation_item_switcher[1].format(animation_number - 1)))
        return self

    def set_language(self, language: str, is_scroll_to_top: bool = True):
        self.press_language_button()
        self._click((self.__language_to_select[0], self.__language_to_select[1].format(language)))
        if is_scroll_to_top:
            self._scroll_to_page_position('top')
        return self

    def focus_on_login_field(self):
        self.unfocus_login_field()
        self._click(self.__login_field)
        return self

    def focus_on_password_field(self):
        self.unfocus_password_field()
        self._click(self.__password_field)
        return self

    def unfocus_login_field(self):
        self._unfocus_field(self.__login_field)
        return self

    def unfocus_password_field(self):
        self._unfocus_field(self.__password_field)
        return self

    def input_login(self, login: str, is_clear: bool = False):
        self._input_text(self.__login_field, login, is_clear)
        return self

    def input_password(self, password: str, is_clear: bool = False):
        self._input_text(self.__password_field, password, is_clear)
        return self

    def press_continue_button(self):
        self._click(self.__continue_button)
        return self

    def login(self, login, password):
        self.input_login(login).input_password(password).press_continue_button()
        return self

    def press_trouble_sign_in_link(self):
        self._click(self.__trouble_sign_in_link)
        return self

    def press_sign_up_link(self):
        self._click(self.__sign_up_link)
        return self

    def press_privacy_policy_link(self):
        self._click(self.__privacy_policy_link)
        return self

    def press_terms_of_service_link(self):
        self._click(self.__terms_of_service_link)
        return self

    def press_google_play_badge(self):
        self._click(self.__google_play_badge)
        return self

    def press_app_store_badge(self):
        self._click(self.__app_store_badge)
        return self

    def press_language_button(self):
        self._scroll_to_element(self.__language_button)
        self._click(self.__language_button)
        return self

    def hold_on_password_eye(self):
        self._hold_mouse(self.__password_eye)
        return self

    def release_password_eye(self):
        self._release_mouse(self.__password_eye)
        return self

    def select_inputted_login(self):
        self._select_text(self.__login_field)
        return self

    def select_inputted_password(self):
        self._select_text(self.__password_field)
        return self

    def get_selected_language(self) -> str:
        """Returns language set in footer"""
        return self._get_text(self.__selected_language)

    def get_checked_language_in_dropdown(self) -> str:
        """Returns language checked in language dropdown"""
        return self._get_text(self.__language_dropdown_selected_item)

    def get_animations_amount(self) -> int:
        return len(self._get_elements(self.__animation))

    def get_text_of_element(self, element: str) -> str:
        """Returns the text of element by specific element name"""
        match element:
            case 'LOGIN_FORM_TITLE':
                return self.__get_login_form_title()
            case 'LOGIN_FIELD_NAME':
                return self.__get_login_field_name()
            case 'EMAIL_DOMAIN':
                return self.__get_email_domain()
            case 'PASSWORD_FIELD_NAME':
                return self.__get_password_field_name()
            case 'PUBLIC_COMPUTER_CHECKBOX_NAME':
                return self.__get_public_computer_checkbox_name()
            case 'CONTINUE_BUTTON_NAME':
                return self.__get_continue_button_name()
            case 'TROUBLE_SIGN_IN_LINK_NAME':
                return self.__get_trouble_sign_in_link_name()
            case 'SIGN_UP_LINK_NAME':
                return self.__get_sign_up_link_name()
            case 'APPS_TITLE':
                return self.__get_apps_title()
            case 'SUPPORT_TITLE':
                return self.__get_support_title()
            case 'PRIVACY_POLICY_LINK_NAME':
                return self.__get_privacy_policy_link_name()
            case 'TERMS_OF_SERVICE_LINK_NAME':
                return self.__get_terms_of_service_link_name()
            case _:
                if 'ANIMATION' in element:
                    for animation_number in range(1, self.get_animations_amount() + 1):
                        if element == f'ANIMATION_{animation_number}_TITLE':
                            return self.__get_animation_title(animation_number)
                        elif element == f'ANIMATION_{animation_number}_PARAGRAPH':
                            return self.__get_animation_paragraph(animation_number)
                else:
                    return 'Specified element is absent'

    def get_error_message(self) -> str:
        """Returns text of error message for unsuccessful login attempt"""
        return self._get_text(self.__error_message)

    def get_inputted_login(self) -> str:
        return self._get_attribute(self.__login_field, 'value')

    def get_inputted_password(self) -> str:
        return self._get_attribute(self.__password_field, 'value')

    def get_inputted_login_length(self) -> int:
        return len(self.get_inputted_login())

    def get_inputted_password_length(self) -> int:
        return len(self.get_inputted_password())

    def get_support_content(self, contact: str) -> str:
        """Returns content of specific support contact"""
        self._scroll_to_page_position('bottom')
        match contact:
            case 'MAIL':
                return self.__get_support_mail_content()
            case 'VODAFONE':
                return self.__get_support_vodafone_content()
            case 'KYIVSTAR':
                return self.__get_support_kyivstar_content()
            case _:
                return 'Contact not found'

    def is_login_field_underlined(self, color: Literal['orange', 'green']) -> bool:
        """Returns if field and its name underlined by specific color"""
        match color:
            case 'orange':
                return self._is_displayed(self.__login_field_underline_orange, mode='fast')
            case 'green':
                return self._is_displayed(self.__login_field_underline_green, mode='fast')

    def is_password_field_underlined(self, color: Literal['orange', 'green']) -> bool:
        """Returns if field and its name underlined by specific color"""
        match color:
            case 'orange':
                return self._is_displayed(self.__password_field_underline_orange, mode='fast')
            case 'green':
                return self._is_displayed(self.__password_field_underline_green, mode='fast')

    def is_login_field_focused(self) -> bool:
        return self._is_focused(self.__login_field)

    def is_password_field_text_selected(self, inputted_password: str) -> bool:
        """Gets selected text on page and compares it with obtained text"""
        self.hold_on_password_eye()
        return self._get_selected_text() == inputted_password

    def is_continue_button_enabled(self) -> bool:
        return self._is_enabled(self.__continue_button)

    def is_password_hidden(self) -> bool:
        return self._get_attribute(self.__password_field, 'type') == 'password'

    def is_password_visible(self) -> bool:
        return self._get_attribute(self.__password_field, 'type') == 'text'

    def is_password_field_eye_opened(self) -> bool:
        return '-unmask' in self._get_attribute(self.__password_eye_state, 'xlink:href')

    def is_password_field_eye_closed(self) -> bool:
        return '-mask' in self._get_attribute(self.__password_eye_state, 'xlink:href')

    def is_animation_active(self, animation_number: int) -> bool:
        return '_3frXUy4p' in self._get_attribute(
            (self.__animation_item_switcher[0], self.__animation_item_switcher[1].format(animation_number - 1)),
            'class')

    def is_auto_animation_switching_correct(self, animations_duration: int) -> bool:
        """Verifies if automated animations switching works correctly within obtained duration. Considers one by one
        switching from the first animation to the last one"""
        self._scroll_to_element(self.__language_button)
        result = True
        for animation in range(1, self.get_animations_amount() + 1):
            self._make_screenshot(name=f'Animation {animation}')
            if not self.is_animation_active(animation):
                result = False
                break
            self._hard_wait(animations_duration)
        return result

    def is_support_contact_icon_displayed(self, contact: str) -> bool:
        """Verifies if icon present for specified support contact"""
        match contact:
            case 'MAIL':
                return self._is_displayed(self.__support_mail_icon)
            case 'VODAFONE':
                return self._is_displayed(self.__support_vodafone_icon)
            case 'KYIVSTAR':
                return self._is_displayed(self.__support_kyivstar_icon)
            case _:
                return False

    def is_language_dropdown_expanded(self) -> bool:
        self._scroll_to_page_position('bottom')
        return self._is_displayed(self.__language_dropdown, mode='fast') and '_3Vk-yMvH' in self._get_attribute(
            self.__language_dropdown_icon, 'class')

    def is_languages_order_in_dropdown_correct(self, expected_order: [list, set, tuple]) -> bool:
        actual_order = tuple(
            self._get_text(element, is_element=True) for element in self._get_elements(self.__language_dropdown_item))
        return actual_order == expected_order
