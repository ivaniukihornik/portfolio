import allure
import pytest

from UkrNet.environments import urls

from UkrNet.environments.expected_data.login_page_env import LoginPageEnv
from UkrNet.constants import MAXIMUM_LOGIN_LENGTH, MAXIMUM_PASSWORD_LENGTH, MINIMUM_LOGIN_LENGTH, \
    MINIMUM_PASSWORD_LENGTH

ER = LoginPageEnv()


@allure.parent_suite('Login Page')
class TestLoginPage:
    @allure.suite('Page opening')
    @allure.testcase('https://app.qase.io/case/PF-2', 'Opening when unauthorized')
    @allure.severity('blocker')
    def test_opening_when_unauthorized(self, open_login_page):
        with allure.step('Open Login Page'):
            login_page = open_login_page
            default_language = login_page.get_selected_language()
            login_page._make_screenshot()
        with allure.step(f'Expected Result: Default language is {ER.DEFAULT_LANGUAGE}'):
            assert ER.DEFAULT_LANGUAGE == default_language, 'default language is incorrect'
        current_url = login_page._get_current_url()
        with allure.step('Expected Result: Login field is focused'):
            assert login_page.is_login_field_focused(), 'Login field isn\'t focused'
        with allure.step('Expected Result: First animation is active'):
            assert login_page.is_animation_active(1), 'First animation isn\'t active'
        with allure.step(f'Expected Result: URL is {urls.LOGIN_PAGE_URL}'):
            assert urls.LOGIN_PAGE_URL == current_url, 'url is incorrect'

    @allure.suite('Page opening')
    @allure.testcase('https://app.qase.io/case/PF-92', 'Opening when authorized')
    @allure.severity('major')
    def test_opening_when_authorized(self, open_inbox_page, conf):
        inbox_page = open_inbox_page
        with allure.step('Open Login Page'):
            inbox_page._open_page(urls.LOGIN_PAGE_URL)
        with allure.step('Expected Result: Redirect to user\'s inbox'):
            assert inbox_page._is_url_opened(urls.INBOX_PAGE_URL), 'Inbox isn\'t opened'
            inbox_page._make_screenshot(is_current_url_needed=True)
            assert conf.default_account_email == inbox_page.get_user_email(), 'Not user\'s inbox'

    @allure.suite('Page tags')
    @allure.testcase('https://app.qase.io/case/PF-3', 'Page Title')
    @allure.severity('minor')
    @pytest.mark.parametrize('language', ER.ALL_LANGUAGES)
    def test_page_title(self, open_login_page, language):
        login_page = open_login_page
        with allure.step(f'Set language to "{language}" and reload the page'):
            login_page.set_language(language)._reload_page()
        with (allure.step('Check Title')):
            assert ER.get_title(language) == login_page._get_title(), 'Wrong Title'

    @allure.suite('Page tags')
    @allure.testcase('https://app.qase.io/case/PF-144', 'Page Description')
    @allure.severity('minor')
    @pytest.mark.parametrize('language', ER.ALL_LANGUAGES)
    def test_page_description(self, open_login_page, language):
        login_page = open_login_page
        with allure.step(f'Set language to "{language}" and reload the page'):
            login_page.set_language(language)._reload_page()
        with (allure.step('Check Description')):
            assert ER.get_description(language) == login_page._get_description(), 'Wrong Description'

    @allure.suite('Page layout')
    @allure.testcase('https://app.qase.io/case/PF-8', 'Text correctness')
    @allure.severity('minor')
    @pytest.mark.parametrize('language', ER.ALL_LANGUAGES)
    @pytest.mark.parametrize('element', ER.get_all_text_elements())
    def test_text_correctness(self, open_login_page, language, element):
        login_page = open_login_page
        with allure.step(f'Set "{language}" language'):
            login_page.set_language(language)
        with allure.step(f'Check text of {element} element'):
            expected_text = ER.get_expected_text(language)[element]
            actual_text = login_page.get_text_of_element(element)
            login_page._make_screenshot()
            assert expected_text == actual_text, f'Text of {element} element is incorrect'

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
        with allure.step('User\'s inbox is opened'):
            inbox_page = create_inbox_page
            assert login_page._is_url_opened(urls.INBOX_PAGE_URL), 'Inbox isn\'t opened'
            inbox_page._make_screenshot(is_current_url_needed=True)
            assert conf.default_account_email == inbox_page.get_user_email(), 'Not user\'s inbox'

    @allure.suite('Login')
    @allure.testcase('https://app.qase.io/case/PF-10', 'Login with existent username and nonexistent password')
    @allure.severity('critical')
    @pytest.mark.parametrize('language', ER.ALL_LANGUAGES)
    def test_login_with_nonexistent_password(self, open_login_page, language, conf):
        login_page = open_login_page
        with allure.step(f'Set "{language}" language'):
            login_page.set_language(language)
        with allure.step('Input existent account username and nonexistent password'):
            login_page.input_login(conf.default_account_login).input_password(conf.default_account_nonexistent_password)
            login_page.hold_on_password_eye()._make_screenshot()
        with allure.step('Press Continue button'):
            login_page.press_continue_button()
        login_page._make_screenshot(with_hard_wait=True)
        with allure.step('Expected Result: Login and Password fields are underlined by red'):
            assert all([login_page.is_login_field_underlined(), login_page.is_password_field_underlined()]), \
                'Login or/and Password fields aren\'t underlined by red'
        expected_error = ER.get_wrong_data_error_message(language)
        with allure.step(f'Expected Result: Error message "{expected_error}" is displayed under Password field'):
            assert expected_error == login_page.get_error_message(), 'Wrong error message'
        with allure.step('Expected Result: Text inputted to Password field is selected'):
            assert login_page.is_password_field_text_selected(conf.default_account_nonexistent_password), \
                'Text from password field isn\'t selected'

    @allure.suite('Login')
    @allure.testcase('https://app.qase.io/case/PF-11', 'Login with nonexistent username and existent password')
    @allure.severity('critical')
    @pytest.mark.parametrize('language', ER.ALL_LANGUAGES)
    def test_login_with_nonexistent_username(self, open_login_page, language, conf):
        login_page = open_login_page
        with allure.step(f'Set "{language}" language'):
            login_page.set_language(language)
        with allure.step('Input nonexistent account username and existent password'):
            login_page.input_login(conf.default_account_nonexistent_login).input_password(conf.default_account_password)
            login_page.hold_on_password_eye()._make_screenshot()
        with allure.step('Press Continue button'):
            login_page.press_continue_button()
        login_page._make_screenshot(with_hard_wait=True)
        with allure.step('Expected Result: Login and Password fields are underlined by red'):
            assert all([login_page.is_login_field_underlined(), login_page.is_password_field_underlined()]), \
                'Login or/and Password fields aren\'t underlined by red'
        expected_error = ER.get_wrong_data_error_message(language)
        with allure.step(f'Expected Result: Error message "{expected_error}" is displayed under Password field'):
            assert expected_error == login_page.get_error_message(), 'Wrong error message'
        with allure.step('Expected Result: Text inputted to Password field is selected'):
            assert login_page.is_password_field_text_selected(conf.default_account_password), \
                'Text from password field isn\'t selected'

    @allure.suite('Login')
    @allure.testcase('https://app.qase.io/case/PF-12', 'Login with username and password of maximum allowed length')
    @allure.severity('critical')
    @pytest.mark.skip(reason='no registered account with needed credentials')
    def test_login_with_maximum_allowed_length_credentials(self, open_login_page, create_inbox_page, conf):
        login_page = open_login_page
        with allure.step('Input username and password'):
            login_page.input_login(conf.maximum_length_login).input_password(conf.maximum_length_password)
            login_page._make_screenshot()
        with allure.step('Press Continue button'):
            login_page.press_continue_button()
        with allure.step('User\'s inbox is opened'):
            inbox_page = create_inbox_page
            assert login_page._is_url_opened(urls.INBOX_PAGE_URL), 'Inbox isn\'t opened'
            inbox_page._make_screenshot(is_current_url_needed=True)
            assert conf.default_account_email == inbox_page.get_user_email(), 'Not user\'s inbox'

    @allure.suite('Login')
    @allure.testcase('https://app.qase.io/case/PF-13', 'Login with username and password of minimum allowed length')
    @allure.severity('critical')
    @pytest.mark.skip(reason='no registered account with needed credentials')
    def test_login_with_minimum_allowed_length_credentials(self, open_login_page, create_inbox_page, conf):
        login_page = open_login_page
        with allure.step('Input username and password'):
            login_page.input_login(conf.minimum_length_login).input_password(conf.minimum_length_password)
            login_page._make_screenshot()
        with allure.step('Press Continue button'):
            login_page.press_continue_button()
        with allure.step('User\'s inbox is opened'):
            inbox_page = create_inbox_page
            assert login_page._is_url_opened(urls.INBOX_PAGE_URL), 'Inbox isn\'t opened'
            inbox_page._make_screenshot(is_current_url_needed=True)
            assert conf.default_account_email == inbox_page.get_user_email(), 'Not user\'s inbox'

    @allure.suite('Login')
    @allure.testcase('https://app.qase.io/case/PF-14', 'Login with username containing allowed symbols')
    @allure.severity('critical')
    @pytest.mark.skip(reason='no registered account with needed credentials')
    def test_login_with_username_containing_allowed_symbols(self, open_login_page, create_inbox_page, conf):
        login_page = open_login_page
        with allure.step('Input username and password'):
            login_page.input_login(conf.login_with_allowed_symbols).input_password(
                conf.password_for_login_with_allowed_symbols)
            login_page._make_screenshot()
        with allure.step('Press Continue button'):
            login_page.press_continue_button()
        with allure.step('User\'s inbox is opened'):
            inbox_page = create_inbox_page
            assert login_page._is_url_opened(urls.INBOX_PAGE_URL), 'Inbox isn\'t opened'
            inbox_page._make_screenshot(is_current_url_needed=True)
            assert conf.default_account_email == inbox_page.get_user_email(), 'Not user\'s inbox'

    @allure.suite('Login')
    @allure.testcase('https://app.qase.io/case/PF-15', 'Login with password containing special symbols')
    @allure.severity('critical')
    @pytest.mark.skip(reason='no registered account with needed credentials')
    def test_login_with_password_containing_special_symbols(self, open_login_page, create_inbox_page, conf):
        login_page = open_login_page
        with allure.step('Input username and password'):
            login_page.input_login(conf.login_for_password_with_special_symbols).input_password(
                conf.password_with_special_symbols)
            login_page._make_screenshot()
        with allure.step('Press Continue button'):
            login_page.press_continue_button()
        with allure.step('User\'s inbox is opened'):
            inbox_page = create_inbox_page
            assert login_page._is_url_opened(urls.INBOX_PAGE_URL), 'Inbox isn\'t opened'
            inbox_page._make_screenshot(is_current_url_needed=True)
            assert conf.default_account_email == inbox_page.get_user_email(), 'Not user\'s inbox'

    @allure.suite('Login')
    @allure.testcase('https://app.qase.io/case/PF-91', 'Login with username beginning and ending with spaces')
    @allure.severity('minor')
    def test_login_with_username_inside_spaces(self, open_login_page, create_inbox_page, conf):
        login_page = open_login_page
        login = login_page.put_login_inside_spaces(conf.default_account_login)
        with allure.step('Input username and password'):
            login_page.input_login(login).input_password(conf.default_account_password)._make_screenshot()
        with allure.step('Press Continue button'):
            login_page.press_continue_button()
        with allure.step('Expected Result: All side spaces are trimmed on login. User\'s inbox is opened'):
            inbox_page = create_inbox_page
            assert inbox_page._is_url_opened(urls.INBOX_PAGE_URL), 'Inbox isn\'t opened'
            inbox_page._make_screenshot(is_current_url_needed=True)
            assert conf.default_account_email == inbox_page.get_user_email(), 'Not user\'s inbox'

    @allure.suite('Login')
    @allure.testcase('https://app.qase.io/case/PF-90', 'Login with username containing only spaces')
    @allure.severity('minor')
    @pytest.mark.parametrize('language', ER.ALL_LANGUAGES)
    def test_login_with_username_containing_only_spaces(self, open_login_page, conf, language):
        login_page = open_login_page
        with allure.step(f'Set "{language}" language'):
            login_page.set_language(language)
        username_to_input = conf.login_only_with_spaces
        with allure.step('Input username containing only spaces and any password'):
            login_page.input_login(username_to_input).input_password(conf.default_account_password). \
                _make_screenshot()
        with allure.step('Press Continue button'):
            login_page.press_continue_button()
        login_page._make_screenshot(with_hard_wait=True)
        with allure.step('Expected Result: Login field is underlined by red'):
            assert login_page.is_login_field_underlined(), 'Login field isn\'t underlined by red'
        expected_error = ER.get_empty_login_error_message(language)
        with allure.step(f'Expected Result: Error message "{expected_error}" is displayed under Password field'):
            assert expected_error == login_page.get_error_message(), 'Wrong error message'
        with allure.step('Expected Result: Login field is focused'):
            assert login_page.is_login_field_focused(), 'Login field isn\'t focused'

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
                         f' Login field. Inputted value is: "{expected_login}"'):
            login_page.select_inputted_login()._make_screenshot()
            assert (MAXIMUM_LOGIN_LENGTH == login_page.get_inputted_login_length()), \
                f'Inputted more than {MAXIMUM_LOGIN_LENGTH} chars'
            assert (expected_login == login_page.get_inputted_login()), 'Inputted login is wrong'
        with allure.step('Input password'):
            login_page.input_password(conf.more_than_maximum_length_password)
        with allure.step('Check inputted data'):
            expected_password = login_page._lslice_text(conf.more_than_maximum_length_password, MAXIMUM_PASSWORD_LENGTH)
        with allure.step(f'Expected Result: Unable to enter more than {MAXIMUM_PASSWORD_LENGTH} characters to '
                         f'Password field. Inputted value is: "{expected_password}"'):
            login_page.hold_on_password_eye().select_inputted_password()._make_screenshot()
            assert (MAXIMUM_PASSWORD_LENGTH == login_page.get_inputted_password_length()), \
                f'Inputted more than {MAXIMUM_PASSWORD_LENGTH} chars'
            assert (expected_password == login_page.get_inputted_password()), 'Inputted password is wrong'

    @allure.suite('Login form')
    @allure.testcase('https://app.qase.io/case/PF-24', 'Show password icon')
    @allure.severity('minor')
    def test_show_password_icon(self, open_login_page, conf):
        login_page = open_login_page
        with allure.step('Input some data to Password field'):
            login_page.input_password(conf.default_account_password)
            login_page._make_screenshot()
        with allure.step('Expected Result: Password is hidden by default'):
            assert login_page.is_password_hidden(), 'Password isn\'t hidden'
        with allure.step('Expected Result: Icon eye is opened'):
            assert login_page.is_password_field_eye_opened(), 'Icon eye isn\'t opened'
        with allure.step('Press and hold "Show password" icon'):
            login_page.hold_on_password_eye()._make_screenshot()
        with allure.step('Expected Result: Password is displayed when holding on icon'):
            assert login_page.is_password_visible(), 'Password isn\'t displayed'
        with allure.step('Expected Result: Icon eye is closed'):
            assert login_page.is_password_field_eye_closed(), 'Icon eye isn\'t closed'
        with allure.step('Release "Show password" icon'):
            login_page.release_password_eye()._make_screenshot()
        with allure.step('Expected Result: Password is hidden when not holding on icon'):
            assert login_page.is_password_hidden(), 'Password isn\'t hidden'
        with allure.step('Expected Result: Icon eye is opened'):
            assert login_page.is_password_field_eye_opened(), 'Icon eye isn\'t opened'

    @allure.suite('Login form')
    @allure.testcase('https://app.qase.io/case/PF-16', 'Continue button state')
    @allure.severity('trivial')
    def test_continue_button_state(self, open_login_page, conf):
        login_page = open_login_page
        random_login = login_page._generate_random_string(login_page._generate_random_number(
            MINIMUM_LOGIN_LENGTH, MAXIMUM_LOGIN_LENGTH))
        random_password = login_page._generate_random_string(login_page._generate_random_number(
            MINIMUM_PASSWORD_LENGTH, MAXIMUM_PASSWORD_LENGTH))
        with allure.step('Leave Login and Password fields empty'):
            login_page.input_login(conf.blank_input, is_clear=True).input_password(conf.blank_input,
                                                                                   is_clear=True)._make_screenshot()
        with allure.step('Expected Result: Continue button is disabled'):
            assert not login_page.is_continue_button_enabled(), 'Button isn\'t disabled'
        with allure.step('Input any username and leave Password field empty'):
            login_page.input_login(random_login).input_password(conf.blank_input, is_clear=True)._make_screenshot()
        with allure.step('Expected Result: Continue button is disabled'):
            assert not login_page.is_continue_button_enabled(), 'Button isn\'t disabled'
        with allure.step('Input any password and leave Login field empty'):
            login_page.input_login(conf.blank_input, is_clear=True).input_password(random_password)._make_screenshot()
        with allure.step('Expected Result: Continue button is disabled'):
            assert not login_page.is_continue_button_enabled(), 'Button isn\'t disabled'
        with allure.step('Input any username and password'):
            login_page.input_login(random_login, is_clear=True).input_password(random_password,
                                                                               is_clear=True)._make_screenshot()
        with allure.step('Expected Result: Continue button is enabled'):
            assert login_page.is_continue_button_enabled(), 'Button isn\'t enabled'

    @allure.suite('Login form')
    @allure.testcase('https://app.qase.io/case/PF-25', 'Links correctness')
    @allure.severity('major')
    def test_links_correctness(self, open_login_page):
        login_page = open_login_page
        with allure.step('Follow "Trouble signing in?" link'):
            login_page.press_trouble_sign_in_link()._make_screenshot(is_current_url_needed=True)
        with allure.step('Expected Result: Link is opened in current tab'):
            assert not login_page._is_link_opened_in_new_tab(), 'Link isn\'t opened in current tab'
        with allure.step(f'Expected Result: "Trouble signing in?" goes to {urls.ACCOUNT_RECOVERY_URL}'):
            assert login_page._is_url_opened(urls.ACCOUNT_RECOVERY_URL), f'URL is wrong'
        with allure.step('Return to Login Page and follow "Sign up" link'):
            login_page._back()
            login_page.press_sign_up_link()._make_screenshot(is_current_url_needed=True)
        with allure.step('Expected Result: Link is opened in current tab'):
            assert not login_page._is_link_opened_in_new_tab(), 'Link isn\'t opened in current tab'
        with allure.step(f'Expected Result: Sign up goes to {urls.SIGN_UP_PAGE_URL}'):
            assert login_page._is_url_opened(urls.SIGN_UP_PAGE_URL), f'URL is wrong'

    @allure.suite('Animations')
    @allure.testcase('https://app.qase.io/case/PF-28', 'Automated switching')
    @allure.severity('normal')
    def test_automated_switching(self, open_login_page):
        login_page = open_login_page
        with allure.step('Check automated switching of animations'):
            with allure.step(f'Expected Result: Animations change automatically in sequential order with timeout '
                             f'{ER.ANIMATIONS_DURATION} seconds'):
                assert login_page.is_auto_animation_switching_correct(ER.ANIMATIONS_DURATION), \
                    'Automated switching doesn\'t work correctly'
            with allure.step('Expected Result: Cycle repeats after finishing of the last animation'):
                login_page._make_screenshot()
                assert login_page.is_animation_active(1), 'Animation cycle doesn\'t repeat'

    @allure.suite('Animations')
    @allure.testcase('https://app.qase.io/case/PF-29', 'Manual switching')
    @allure.severity('normal')
    def test_manual_switching(self, open_login_page):
        login_page = open_login_page
        animation_number = login_page._generate_random_number(2, login_page.get_animations_amount())
        with allure.step(f'Switch animation with random step in direct order (to {animation_number})'):
            login_page.switch_animation(animation_number)._make_screenshot(with_hard_wait=True)
        with allure.step(f'Expected Result: Active animation is {animation_number}'):
            assert login_page.is_animation_active(animation_number), 'Active animation is wrong'
        animation_number = login_page._generate_random_number(1, animation_number - 1)
        with allure.step(f'Switch animation with random step in backward order (to {animation_number})'):
            login_page.switch_animation(animation_number)._make_screenshot(with_hard_wait=True)
        with allure.step(f'Expected Result: Active animation is {animation_number}'):
            assert login_page.is_animation_active(animation_number), 'Active animation is wrong'
        with allure.step(f'Switch animation to current (to {animation_number})'):
            login_page.switch_animation(animation_number)._make_screenshot(with_hard_wait=True)
        with allure.step(f'Expected Result: Active animation is {animation_number}'):
            assert login_page.is_animation_active(animation_number), 'Active animation is wrong'

    @allure.suite('Footer')
    @allure.testcase('https://app.qase.io/case/PF-31', 'Contacts content')
    @allure.severity('normal')
    @pytest.mark.parametrize('contact', ER.get_all_support_contacts())
    def test_contacts_content(self, open_login_page, contact):
        login_page = open_login_page
        with allure.step(f'Check content of {contact} contact'):
            expected_content = ER.get_support_content()[contact]
            actual_content = login_page.get_support_content(contact)
        login_page._make_screenshot()
        with allure.step('Expected Result: Content is correct'):
            assert expected_content == actual_content, 'Content is incorrect'
        with allure.step('Expected Result: Icon is displayed'):
            assert login_page.is_support_contact_icon_displayed(contact), 'Icon isn\'t displayed'

    @allure.suite('Footer')
    @allure.testcase('https://app.qase.io/case/PF-32', 'Links to agreements')
    @allure.severity('minor')
    @pytest.mark.parametrize('language', ER.ALL_LANGUAGES)
    def test_links_to_agreements(self, open_login_page, language):
        login_page = open_login_page
        with allure.step(f'Set language to "{language}" and follow "Privacy Policy" link'):
            login_page.set_language(language)
            login_page.press_privacy_policy_link()
            expected_url = urls.get_privacy_policy_page_url(language)
        with allure.step('Expected Result: Link is opened in new tab'):
            assert login_page._is_link_opened_in_new_tab(is_switching_to_new_tab_needed=True), \
                'Link isn\'t opened in new tab'
        with allure.step(f'Expected Result: "Privacy Policy" goes to {expected_url}'):
            login_page._make_screenshot(is_current_url_needed=True)
            assert login_page._is_url_opened(expected_url), 'Url is wrong'
        with allure.step('Close link and return to Login Page'):
            login_page._close_current_tab(is_switching_to_first_tab_needed=True)
        with allure.step('Follow "Terms of Service" link'):
            login_page.press_terms_of_service_link()
            expected_url = urls.get_terms_of_service_url(language)
        with allure.step('Expected Result: Link is opened in new tab'):
            assert login_page._is_link_opened_in_new_tab(is_switching_to_new_tab_needed=True), \
                'Link isn\'t opened in new tab'
        with allure.step(f'Expected Result: "Terms of Service" goes to {expected_url}'):
            login_page._make_screenshot(is_current_url_needed=True)
            assert login_page._is_url_opened(expected_url), 'Url is wrong'
