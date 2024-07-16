def get_privacy_policy_page_url(language_code: str) -> str:
    return PRIVACY_POLICY_PAGE_URL.format('/' + language_code) if language_code == 'ru' \
        else PRIVACY_POLICY_PAGE_URL.format('')


def get_terms_of_service_url(language_code: str) -> str:
    return TERMS_OF_SERVICE_PAGE_URL.format(language_code)


DOMAIN = 'https://{}ukr.net'
MAIN_DOMAIN = DOMAIN.format('www.')
ACCOUNTS_SUBDOMAIN = DOMAIN.format('accounts.')
MAILBOX_SUBDOMAIN = DOMAIN.format('mail.')

SIGN_UP_PAGE_URL = ACCOUNTS_SUBDOMAIN + '/registration'
LOGIN_PAGE_URL = ACCOUNTS_SUBDOMAIN + '/login'
ACCOUNT_RECOVERY_URL = ACCOUNTS_SUBDOMAIN + '/recovery'

INBOX_PAGE_URL = MAILBOX_SUBDOMAIN + '/desktop#msglist/f0/p0'

PRIVACY_POLICY_PAGE_URL = MAIN_DOMAIN + '{}/terms/'
TERMS_OF_SERVICE_PAGE_URL = MAILBOX_SUBDOMAIN + '/terms_{}.html'

GOOGLE_PLAY_URL = 'https://play.google.com/store/apps/details?id=net.ukr.mail'
APP_STORE_URL = 'https://apps.apple.com/ua/app/ukr-net-mail-app/id1405521485'
