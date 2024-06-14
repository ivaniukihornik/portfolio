def get_privacy_policy_page_url(language):
    return PRIVACY_POLICY_PAGE_URL.format('/' + language) if language == 'ru' else PRIVACY_POLICY_PAGE_URL.format('')


def get_terms_of_service_url(language):
    return TERMS_OF_SERVICE_PAGE_URL.format(language)


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
