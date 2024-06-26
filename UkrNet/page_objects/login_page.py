from selenium.webdriver.common.by import By

from UkrNet.constants import MAXIMUM_LOGIN_LENGTH
from UkrNet.utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __language_button = (By.XPATH, '//button[@data-lang="{}"]')
    __selected_language = (By.XPATH, '//button[contains(@class, "_30cp__sx")]')

    __h1 = (By.CSS_SELECTOR, 'div._13Fm_HHI:nth-child({})>h1')
    __h2 = (By.CSS_SELECTOR, 'div._13Fm_HHI:nth-child({})>h2')

    __login_form_title = (By.CSS_SELECTOR, 'h2._1azB1YgZ')

    __login_field = (By.XPATH, '//input[@name="login"]')
    __login_field_name = (__login_field[0], f'{__login_field[1]}/ancestor::label/p')
    __login_field_name_pos_focus_modifier = (__login_field[0], f'{__login_field[1]}[contains(@class, "focus-visible")]')
    __login_field_name_pos_input_modifier = (__login_field_name[0], f'{__login_field_name[1]}[contains(@class,'
                                                                    f' "_3aAVn0Us")]')
    __login_field_underline = (__login_field[0], f'{__login_field[1]}/ancestor::label/div[contains(@class,'
                                                 f' "ei5QaAJ0")]')
    __email_domain = (By.CSS_SELECTOR, 'span._38_4DkC1')

    __password_field = (By.XPATH, '//input[@name="password"]')
    __password_field_name = (__password_field[0], f'{__password_field[1]}/ancestor::label/p')
    __password_field_name_pos_focus_modifier = (__password_field[0], f'{__password_field[1]}[contains(@class,'
                                                                     f' "focus-visible")]')
    __password_field_name_pos_input_modifier = (__password_field_name[0], f'{__password_field_name[1]}[contains(@class,'
                                                                          f' "_3aAVn0Us")]')
    __password_field_underline = (__password_field[0], f'{__password_field[1]}/ancestor::label/div[contains(@class,'
                                                       f' "ei5QaAJ0")]')
    __password_eye = (__password_field[0], f'{__password_field[1]}/ancestor::div/button')
    __password_eye_state = (__password_eye[0], f'{__password_eye[1]}//*[name()="use"]')

    __error_message = (By.CSS_SELECTOR, 'p._1oZFLSZ_')

    __animation = (By.CSS_SELECTOR, 'li._82nIdC0D')
    __animation_item_switcher = (By.CSS_SELECTOR, 'li._82nIdC0D:nth-child({})')
    __footer_of_animation = (By.CSS_SELECTOR, 'p._9AaSh-oS')

    __public_computer_checkbox = (By.XPATH, '//input[@type="checkbox"]/ancestor::label')
    __public_computer_checkbox_name = (By.CSS_SELECTOR, 'div._2D_WbGHd')

    __continue_button = (By.XPATH, '//button[@type="submit"]')
    __continue_button_name = (__continue_button[0], f'{__continue_button[1]}/div')

    __trouble_sign_in_link = (By.CSS_SELECTOR, 'div._3GXVBC43>a:nth-child(1)')
    __sign_up_link = (By.CSS_SELECTOR, 'div._3GXVBC43>a:nth-child(2)')

    __support_title = (By.CSS_SELECTOR, 'h4._3qFvKK5H')

    __support_mail_icon = (By.CSS_SELECTOR, 'li._1w0muvWF')
    __support_mail_content = (By.CSS_SELECTOR, 'li._1w0muvWF > a')

    __support_vodafone_icon = (By.CSS_SELECTOR, 'li._1y__-uai')
    __support_vodafone_content = (By.CSS_SELECTOR, 'li._1y__-uai > a')

    __support_kyivstar_icon = (By.CSS_SELECTOR, 'li._2I9ZLTFx')
    __support_kyivstar_content = (By.CSS_SELECTOR, 'li._2I9ZLTFx > a')

    __support_phone_icon = (By.CSS_SELECTOR, 'li._25jRRsf_')
    __support_phone_content = (By.CSS_SELECTOR, 'li._25jRRsf_ > a')

    __privacy_policy_link = (By.CSS_SELECTOR, 'div._3ZKKngSa>a')
    __terms_of_service_link = (By.CSS_SELECTOR, 'div._1DEoOWjX>a')

    def __get_language_button_name(self, language):
        return self._get_text((self.__language_button[0], self.__language_button[1].format(language)))

    def __get_h1(self, animation_number):
        """Returns <h1> header of animation by animation number"""
        return self.switch_animation(animation_number)._get_text((self.__h1[0], self.__h1[1].format(animation_number)))

    def __get_h2(self, animation_number):
        """Returns <h2> header of animation by animation number"""
        return self.switch_animation(animation_number)._get_text((self.__h2[0], self.__h2[1].format(animation_number)))

    def __get_footer_of_animation(self, animation_number):
        """Returns footer of animation by animation number"""
        return self.switch_animation(animation_number)._get_text(self.__footer_of_animation)

    def __get_login_form_title(self):
        return self._get_text(self.__login_form_title)

    def __get_login_field_name(self):
        return self._get_text(self.__login_field_name)

    def __get_email_domain(self):
        return self._get_text(self.__email_domain)

    def __get_password_field_name(self):
        return self._get_text(self.__password_field_name)

    def __get_public_computer_checkbox_name(self):
        return self._get_text(self.__public_computer_checkbox_name)

    def __get_continue_button_name(self):
        return self._get_text(self.__continue_button_name)

    def __get_trouble_sign_in_link_name(self):
        return self._get_text(self.__trouble_sign_in_link)

    def __get_sign_up_link_name(self):
        return self._get_text(self.__sign_up_link)

    def __get_support_title(self):
        return self._get_text(self.__support_title)

    def __get_support_mail_content(self):
        return self._get_text(self.__support_mail_content)

    def __get_support_vodafone_content(self):
        return self._get_text(self.__support_vodafone_content)

    def __get_support_kyivstar_content(self):
        return self._get_text(self.__support_kyivstar_content)

    def __get_support_phone_content(self):
        return self._get_text(self.__support_phone_content)

    def __get_privacy_policy_link_name(self):
        return self._get_text(self.__privacy_policy_link)

    def __get_terms_of_service_link_name(self):
        return self._get_text(self.__terms_of_service_link)

    def switch_animation(self, animation_number: int):
        """Switches the animation to obtained number"""
        self._click((self.__animation_item_switcher[0], self.__animation_item_switcher[1].format(animation_number)))
        return self

    def set_language(self, language):
        self._click((self.__language_button[0], self.__language_button[1].format(language)))
        return self

    def focus_on_login_field(self):
        self._click(self.__login_field)
        return self

    def focus_on_password_field(self):
        self._click(self.__password_field)
        return self

    def input_login(self, login, is_clear=False):
        self._input_text(self.__login_field, login, is_clear)
        return self

    def input_password(self, password, is_clear=False):
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

    def press_terms_of_service_link(self):
        self._click(self.__terms_of_service_link)

    def put_login_inside_spaces(self, login):
        """Surrounds obtained login with random amount of spaces and returns the result string"""
        start_spaces_count = self._generate_random_number(1, MAXIMUM_LOGIN_LENGTH - len(login) - 1)
        end_spaces_count = self._generate_random_number(1, MAXIMUM_LOGIN_LENGTH - len(login) -
                                                        start_spaces_count)
        return f'{" " * start_spaces_count}{login}{" " * end_spaces_count}'

    def check_public_computer_checkbox(self):
        self._click(self.__public_computer_checkbox)
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

    def get_selected_language(self):
        return self._get_attribute(locator=self.__selected_language, attribute='data-lang')

    def get_text_of_element(self, element):
        """Returns the text of element by specific element name"""
        match element:
            case 'UK_LANGUAGE_BUTTON_NAME':
                return self.__get_language_button_name('uk')
            case 'RU_LANGUAGE_BUTTON_NAME':
                return self.__get_language_button_name('ru')
            case 'EN_LANGUAGE_BUTTON_NAME':
                return self.__get_language_button_name('en')
            case 'H1_ANIMATION_1':
                return self.__get_h1(1)
            case 'H2_ANIMATION_1':
                return self.__get_h2(1)
            case 'H1_ANIMATION_2':
                return self.__get_h1(2)
            case 'H2_ANIMATION_2':
                return self.__get_h2(2)
            case 'H1_ANIMATION_3':
                return self.__get_h1(3)
            case 'H2_ANIMATION_3':
                return self.__get_h2(3)
            case 'FOOTER_ANIMATION_3':
                return self.__get_footer_of_animation(3)
            case 'H1_ANIMATION_4':
                return self.__get_h1(4)
            case 'H2_ANIMATION_4':
                return self.__get_h2(4)
            case 'H1_ANIMATION_5':
                return self.__get_h1(5)
            case 'H2_ANIMATION_5':
                return self.__get_h2(5)
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
            case 'SUPPORT_TITLE':
                return self.__get_support_title()
            case 'PRIVACY_POLICY_LINK_NAME':
                return self.__get_privacy_policy_link_name()
            case 'TERMS_OF_SERVICE_LINK_NAME':
                return self.__get_terms_of_service_link_name()
            case _:
                return None

    def get_error_message(self):
        return self._get_text(self.__error_message)

    def get_inputted_login(self):
        return self._get_attribute(self.__login_field, 'value')

    def get_inputted_password(self):
        return self._get_attribute(self.__password_field, 'value')

    def get_inputted_login_length(self):
        return len(self.get_inputted_login())

    def get_inputted_password_length(self):
        return len(self.get_inputted_password())

    def get_animations_amount(self):
        return len(self._get_elements(self.__animation))

    def get_support_content(self, contact):
        match contact:
            case 'MAIL':
                return self.__get_support_mail_content()
            case 'VODAFONE':
                return self.__get_support_vodafone_content()
            case 'KYIVSTAR':
                return self.__get_support_kyivstar_content()
            case 'PHONE':
                return self.__get_support_phone_content()
            case _:
                return None

    def is_login_field_underlined(self):
        return self._is_displayed(self.__login_field_underline)

    def is_password_field_underlined(self):
        return self._is_displayed(self.__password_field_underline)

    def is_login_field_focused(self):
        return self._is_focused(self.__login_field)

    def is_password_field_text_selected(self, inputted_password):
        """Gets selected text and compares it with text from argument"""
        self.hold_on_password_eye()
        return self._get_selected_text() == inputted_password

    def is_continue_button_enabled(self):
        return self._is_enabled(self.__continue_button)

    def is_login_field_name_displayed_as_placeholder(self):
        return not (self._is_displayed(self.__login_field_name_pos_focus_modifier, mode='fast') |
                    self._is_displayed(self.__login_field_name_pos_input_modifier, mode='fast'))

    def is_password_field_name_displayed_as_placeholder(self):
        return not (self._is_displayed(self.__password_field_name_pos_focus_modifier, mode='fast') |
                    self._is_displayed(self.__password_field_name_pos_input_modifier, mode='fast'))

    def is_login_field_name_displayed_above_field(self):
        return (self._is_displayed(self.__login_field_name_pos_focus_modifier, mode='fast') |
                self._is_displayed(self.__login_field_name_pos_input_modifier, mode='fast'))

    def is_password_field_name_displayed_above_field(self):
        return (self._is_displayed(self.__password_field_name_pos_focus_modifier, mode='fast') |
                self._is_displayed(self.__password_field_name_pos_input_modifier, mode='fast'))

    def is_password_hidden(self):
        return self._get_attribute(self.__password_field, 'type') == 'password'

    def is_password_visible(self):
        return self._get_attribute(self.__password_field, 'type') == 'text'

    def is_password_field_eye_opened(self):
        return '-unmask' in self._get_attribute(self.__password_eye_state, 'xlink:href')

    def is_password_field_eye_closed(self):
        return '-mask' in self._get_attribute(self.__password_eye_state, 'xlink:href')

    def is_animation_active(self, animation_number):
        return '_3MsdXPEs' in self._get_attribute(
            (self.__animation_item_switcher[0], self.__animation_item_switcher[1].format(animation_number)), 'class')

    def is_auto_animation_switching_correct(self, animations_duration):
        result = True
        for animation in range(1, self.get_animations_amount() + 1):
            self._make_screenshot(name=f'Animation {animation}')
            if not self.is_animation_active(animation):
                result = False
                break
            self._hard_wait(animations_duration)
        return result

    def is_support_contact_icon_displayed(self, contact):
        match contact:
            case 'MAIL':
                return self._is_displayed(self.__support_mail_icon)
            case 'VODAFONE':
                return self._is_displayed(self.__support_vodafone_icon)
            case 'KYIVSTAR':
                return self._is_displayed(self.__support_kyivstar_icon)
            case 'PHONE':
                return self._is_displayed(self.__support_phone_icon)
            case _:
                return False
