import time

import allure
import pytest

from UkrNet.environments import urls

from UkrNet.environments.expected_data import login_page_env as ER
from UkrNet.environments.expected_data.login_page_env import MAXIMUM_LOGIN_LENGTH, MAXIMUM_PASSWORD_LENGTH
from UkrNet.environments.languages import ALL_LANGUAGES


@allure.parent_suite('Login Page')
class TestLoginPage:
    @allure.suite('Page opening')
    @allure.testcase('https://app.qase.io/case/PF-2', 'Page opening')
    @allure.severity('blocker')
    def test_page_opening(self, open_login_page):
        login_page = open_login_page
        with allure.step('Check default language'):
            default_language = login_page.get_selected_language()
            login_page._make_screenshot()
            assert default_language == ER.DEFAULT_LANGUAGE, 'default language is incorrect'
        with allure.step('Check page URL'):
            current_url = login_page._get_current_url()
            assert current_url == urls.LOGIN_PAGE_URL, 'url is incorrect'

    @allure.suite('Page opening')
    @allure.testcase('https://app.qase.io/case/PF-3', 'Title and Description')
    @allure.severity('minor')
    @pytest.mark.parametrize('language', ALL_LANGUAGES)
    def test_title_and_description(self, open_login_page, language):
        login_page = open_login_page
        with allure.step('Set language to "uk" and reload the page'):
            login_page.set_language(language)._reload_page()
            title = login_page._get_title()
            description = login_page._get_description()
        with (allure.step('Check Title and Description')):
            assert all([title == ER.get_title(language), description == ER.get_description(language)
                        ]), 'Wrong Title or/and Description'

    @allure.suite('Page layout')
    @allure.testcase('https://app.qase.io/case/PF-8', 'Text correctness')
    @allure.severity('minor')
    @pytest.mark.parametrize('language', ALL_LANGUAGES)
    @pytest.mark.parametrize('element', ['LANGUAGE_BUTTON_NAME', 'H1_ANIMATION_1', 'H2_ANIMATION_1', 'H1_ANIMATION_2',
                                         'H2_ANIMATION_2', 'H1_ANIMATION_3', 'H2_ANIMATION_3', 'FOOTER_ANIMATION_3',
                                         'H1_ANIMATION_4', 'H2_ANIMATION_4', 'H1_ANIMATION_5', 'H2_ANIMATION_5',
                                         'LOGIN_FORM_TITLE', 'LOGIN_FIELD_NAME', 'EMAIL_DOMAIN', 'PASSWORD_FIELD_NAME',
                                         'PUBLIC_COMPUTER_CHECKBOX_NAME', 'CONTINUE_BUTTON_NAME',
                                         'TROUBLE_SIGN_IN_LINK_NAME', 'SIGN_UP_LINK_NAME', 'SUPPORT_TITLE',
                                         'PRIVACY_POLICY_LINK_NAME', 'TERMS_OF_SERVICE_LINK_NAME'])
    def test_text_correctness(self, open_login_page, language, element):
        login_page = open_login_page
        with allure.step('Set Ukrainian language'):
            login_page.set_language(language)
        with allure.step(f'Check text of {element} element'):
            expected_text = ER.get_expected_text(language)[element]
            actual_text = login_page.get_text_of_element(element, language)
            login_page._make_screenshot()
            assert actual_text == expected_text, f'Text of {element} element is incorrect'

    @allure.suite('Login')
    @allure.testcase('https://app.qase.io/case/PF-9', 'Login with existent credentials')
    @allure.severity('critical')
    def test_login_with_existent_credentials(self, open_login_page, create_inbox_page, conf):
        login_page = open_login_page
        with allure.step('Input username and password'):
            login_page.input_login(conf.default_account_login).input_password(conf.default_account_password)
            login_page._make_screenshot()
        with allure.step('Press Continue button'):
            login_page.press_continue_button()
        with allure.step('Redirect to user\'s inbox'):
            inbox_page = create_inbox_page
            assert login_page.is_inbox_opened(), 'Inbox isn\'t opened'
            inbox_page._make_screenshot()
            assert conf.default_account_email == inbox_page.get_user_email(), 'Not user\'s inbox'

    @allure.suite('Login')
    @allure.testcase('https://app.qase.io/case/PF-10', 'Login with existent username and nonexistent password')
    @allure.severity('critical')
    @pytest.mark.parametrize('language', ALL_LANGUAGES)
    def test_login_with_nonexistent_password(self, open_login_page, language, conf):
        login_page = open_login_page
        with allure.step('Set Ukrainian language'):
            login_page.set_language(language)
        with allure.step('Input existent account username and nonexistent password'):
            login_page.input_login(conf.default_account_login).input_password(conf.default_account_nonexistent_password)
            login_page._make_screenshot()
        with allure.step('Press Continue button'):
            login_page.press_continue_button()
        login_page._make_screenshot(with_hard_wait=True)
        with allure.step('Expected Result: Username and Password fields are underlined by red'):
            assert all([login_page.is_login_field_underlined(),
                        login_page.is_password_field_underlined()]), ('Login or/and Password fields aren\'t underlined '
                                                                      'by red')
        with allure.step(f'Expected Result: Error message "{ER.get_error_message(language)}" is displayed under '
                         f'Password field'):
            assert login_page.get_error_message() == ER.get_error_message(language)
        with allure.step('Expected Result: Text inputted to Password field is selected'):
            assert login_page.is_password_field_text_selected(conf.default_account_nonexistent_password)

    @allure.suite('Login')
    @allure.testcase('https://app.qase.io/case/PF-11', 'Login with nonexistent username and existent password')
    @allure.severity('critical')
    @pytest.mark.parametrize('language', ALL_LANGUAGES)
    def test_login_with_nonexistent_username(self, open_login_page, language, conf):
        login_page = open_login_page
        with allure.step('Set Ukrainian language'):
            login_page.set_language(language)
        with allure.step('Input existent account username and nonexistent password'):
            login_page.input_login(conf.default_account_nonexistent_login).input_password(conf.default_account_password)
            login_page._make_screenshot()
        with allure.step('Press Continue button'):
            login_page.press_continue_button()
        login_page._make_screenshot(with_hard_wait=True)
        with allure.step('Expected Result: Username and Password fields are underlined by red'):
            assert all([login_page.is_login_field_underlined(),
                        login_page.is_password_field_underlined()]), ('Login or/and Password fields aren\'t underlined '
                                                                      'by red')
        with allure.step(f'Expected Result: Error message "{ER.get_error_message(language)}" is displayed under '
                         f'Password field'):
            assert login_page.get_error_message() == ER.get_error_message(language)
        with allure.step('Expected Result: Text inputted to Password field is selected'):
            assert login_page.is_password_field_text_selected(conf.default_account_password)

    @allure.suite('Login')
    @allure.testcase('https://app.qase.io/case/PF-12', 'Login with username and password of maximum allowed length')
    @allure.severity('critical')
    @pytest.mark.skip(reason='no registered account with needed credentials')
    def test_login_with_existent_credentials(self, open_login_page, create_inbox_page, conf):
        login_page = open_login_page
        with allure.step('Input username and password'):
            login_page.input_login(conf.maximum_length_login).input_password(conf.maximum_length_password)
            login_page._make_screenshot()
        with allure.step('Press Continue button'):
            login_page.press_continue_button()
        with allure.step('Redirect to user\'s inbox'):
            inbox_page = create_inbox_page
            assert login_page.is_inbox_opened(), 'Inbox isn\'t opened'
            inbox_page._make_screenshot()
            assert conf.default_account_email == inbox_page.get_user_email(), 'Not user\'s inbox'

    @allure.suite('Login')
    @allure.testcase('https://app.qase.io/case/PF-13', 'Login with username and password of minimum allowed length')
    @allure.severity('critical')
    @pytest.mark.skip(reason='no registered account with needed credentials')
    def test_login_with_existent_credentials(self, open_login_page, create_inbox_page, conf):
        login_page = open_login_page
        with allure.step('Input username and password'):
            login_page.input_login(conf.minimum_length_login).input_password(conf.minimum_length_password)
            login_page._make_screenshot()
        with allure.step('Press Continue button'):
            login_page.press_continue_button()
        with allure.step('Redirect to user\'s inbox'):
            inbox_page = create_inbox_page
            assert login_page.is_inbox_opened(), 'Inbox isn\'t opened'
            inbox_page._make_screenshot()
            assert conf.default_account_email == inbox_page.get_user_email(), 'Not user\'s inbox'

    @allure.suite('Login')
    @allure.testcase('https://app.qase.io/case/PF-14', 'Login with username containing allowed symbols')
    @allure.severity('critical')
    @pytest.mark.skip(reason='no registered account with needed credentials')
    def test_login_with_existent_credentials(self, open_login_page, create_inbox_page, conf):
        login_page = open_login_page
        with allure.step('Input username and password'):
            login_page.input_login(conf.login_with_allowed_symbols).input_password(
                conf.password_for_login_with_allowed_symbols)
            login_page._make_screenshot()
        with allure.step('Press Continue button'):
            login_page.press_continue_button()
        with allure.step('Redirect to user\'s inbox'):
            inbox_page = create_inbox_page
            assert login_page.is_inbox_opened(), 'Inbox isn\'t opened'
            inbox_page._make_screenshot()
            assert conf.default_account_email == inbox_page.get_user_email(), 'Not user\'s inbox'

    @allure.suite('Login')
    @allure.testcase('https://app.qase.io/case/PF-15', 'Login with password containing special symbols')
    @allure.severity('critical')
    @pytest.mark.skip(reason='no registered account with needed credentials')
    def test_login_with_existent_credentials(self, open_login_page, create_inbox_page, conf):
        login_page = open_login_page
        with allure.step('Input username and password'):
            login_page.input_login(conf.login_for_password_with_special_symbols).input_password(
                conf.password_with_special_symbols)
            login_page._make_screenshot()
        with allure.step('Press Continue button'):
            login_page.press_continue_button()
        with allure.step('Redirect to user\'s inbox'):
            inbox_page = create_inbox_page
            assert login_page.is_inbox_opened(), 'Inbox isn\'t opened'
            inbox_page._make_screenshot()
            assert conf.default_account_email == inbox_page.get_user_email(), 'Not user\'s inbox'

    # @allure.suite('Login')
    # @allure.testcase('https://app.qase.io/case/PF-17', 'Login with Public computer')
    # @allure.severity('major')
    # def test_login_with_public_computer(self, open_login_page, conf):
    #     login_page = open_login_page
    #     with allure.step('Input username and password'):
    #         login_page.input_login(conf.default_account_login).input_password(conf.default_account_password)
    #     with allure.step('Check "Public computer" checkbox and press "Continue" button'):
    #         login_page.press_continue_button()
    #         login_page._make_screenshot()
    #     with allure.step('Close all browser windows and reopen one'):
    #         cookies = login_page.driver.get_cookies()
    #         login_page._close_window()
    #         driver = DriverFactory.create_driver(driver_id=conf.browser_id)
    #         driver.maximize_window()
    #         driver.get(LOGIN_PAGE_URL)
    #         driver.delete_all_cookies()
    #         for cookie in cookies:
    #             driver.add_cookie(cookie)
    #         driver.get(LOGIN_PAGE_URL)
    #         driver.quit()

    @allure.suite('Login form')
    @allure.testcase('https://app.qase.io/case/PF-20', 'Displaying of input field names')
    @allure.severity('trivial')
    def test_displaying_of_input_field_titles(self, open_login_page, conf):
        login_page = open_login_page
        with allure.step('Clear and unfocus Username and Password fields'):
            login_page.check_public_computer_checkbox()
            with allure.step('Expected Result: Names are displayed as field placeholders'):
                login_page._make_screenshot()
                assert all([login_page.is_login_field_name_displayed_as_placeholder(),
                            login_page.is_password_field_name_displayed_as_placeholder()
                            ]), 'Login and/or Password fields aren\'t displayed as placeholders'
        with allure.step('Focus on Username and Password fields'):
            login_page.focus_on_login_field()
            is_login_field_name_displayed_above_field = login_page.is_login_field_name_displayed_above_field()
            login_page._make_screenshot('Focus on Login field')
            login_page.focus_on_password_field()
            is_password_field_name_displayed_above_field = login_page.is_password_field_name_displayed_above_field()
            login_page._make_screenshot('Focus on Password field')
            with allure.step('Expected Result: Names appear above fields when focusing on them'):
                assert all([is_login_field_name_displayed_above_field, is_password_field_name_displayed_above_field
                            ]), 'Login and/or Password fields aren\'t displayed above fields'
        with allure.step('Input some data to Username and Password fields and unfocus them'):
            login_page.input_login(conf.default_account_login).input_password(conf.default_account_password
                                                                              ).check_public_computer_checkbox()
            with allure.step('Expected Result: Names appear above fields when there is some data entered'):
                login_page._make_screenshot()
                assert all([login_page.is_login_field_name_displayed_above_field(),
                            login_page.is_password_field_name_displayed_above_field()
                            ]), 'Login and/or Password fields aren\'t displayed above fields'

    @allure.suite('Login form')
    @allure.testcase('https://app.qase.io/case/PF-19', 'Input username and password of more than maximum'
                                                       ' allowed length')
    @allure.severity('minor')
    def test_input_more_than_maximum_allowed_values(self, open_login_page, conf):
        login_page = open_login_page
        with allure.step('Input username'):
            login_page.input_login(conf.more_than_maximum_length_login)
        with allure.step('Check inputted data'):
            expected_login = login_page._lslice_text(conf.more_than_maximum_length_login, MAXIMUM_LOGIN_LENGTH)
            with allure.step(f'Expected Result: Unable to enter more than {MAXIMUM_LOGIN_LENGTH} characters to'
                             f' Username field. Inputted value is: "{expected_login}"'):
                login_page._make_screenshot()
                assert (login_page.get_inputted_login_length() ==
                        MAXIMUM_LOGIN_LENGTH), f'Inputted more than {MAXIMUM_LOGIN_LENGTH} chars'
                assert (login_page.get_inputted_login() ==
                        expected_login), f'Inputted login isn\'t: "{expected_login}"'
        with allure.step('Input password'):
            login_page.input_password(conf.more_than_maximum_length_password)
        with allure.step('Check inputted data'):
            expected_password = login_page._lslice_text(conf.more_than_maximum_length_password, MAXIMUM_PASSWORD_LENGTH)
            with allure.step(f'Expected Result: Unable to enter more than {MAXIMUM_PASSWORD_LENGTH} characters to '
                             f'Password field. Inputted value is: "{expected_password}"'):
                login_page.hold_on_password_eye()._make_screenshot()
                assert (login_page.get_inputted_password_length() ==
                        MAXIMUM_PASSWORD_LENGTH), f'Inputted more than {MAXIMUM_PASSWORD_LENGTH} chars'
                assert (login_page.get_inputted_password() ==
                        expected_password), f'Inputted password isn\'t: "{expected_password}"'

