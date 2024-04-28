DEFAULT_LANGUAGE = 'uk'
MAXIMUM_LOGIN_LENGTH = 32
MAXIMUM_PASSWORD_LENGTH = 128


def get_title(language):
    match language:
        case 'uk':
            return 'Пошта @ ukr.net - українська електронна пошта • Створи емейл'
        case 'ru':
            return 'Почта @ ukr.net - украинская электронная почта • Создать емейл'
        case 'en':
            return 'Mail @ ukr.net - ukrainian electronic mail • Create email'
        case _:
            return 'Specified language is absent'


def get_description(language):
    match language:
        case 'uk':
            return ('Пошта@ukr.net - швидкий і зручний інтерфейс, відправка по e-mail файлів до 50 Гб, поштова скринька'
                    ' з професійним захистом від спаму і вірусів. Створи свій email на домені ukr.net.')
        case 'ru':
            return ('Почта@ukr.net - быстрый и удобный интерфейс, отправка по e-mail файлов до 50 Гб, почтовый ящик'
                    ' c профессиональной защитой от спама и вирусов. Создай свой email на домене ukr.net.')
        case 'en':
            return ('Mail@ukr.net - fast and convenient interface, send files up to 50 GB in your email, mailbox'
                    ' with professional anti-spam and anti-virus protection. Create your email on the domain ukr.net.')
        case _:
            return 'Specified language is absent'


def get_expected_text(language):
    match language:
        case 'uk':
            return {
                'LANGUAGE_BUTTON_NAME': 'Українська',
                'H1_ANIMATION_1': 'ЦІЛОДОБОВА СЛУЖБА ПІДТРИМКИ',
                'H2_ANIMATION_1': 'Поштою і по телефону.',
                'H1_ANIMATION_2': 'МИТТЄВА ДОСТАВКА ЛИСТІВ',
                'H2_ANIMATION_2': 'Швидкість доставки повідомлень – менше однієї секунди.',
                'H1_ANIMATION_3': 'НАЙПОПУЛЯРНІША УКРАЇНСЬКА ЕЛЕКТРОННА ПОШТА',
                'H2_ANIMATION_3': '42,5% e-mail користувачів в Україні - з @UKR.NET.*',
                'FOOTER_ANIMATION_3': '*За даними дослідження інтернет-аудиторії Opinion Software Media компанії ТОВ'
                                  ' "Інмайнд Опініон Медіа", квітень 2019 року, n=5000.',
                'H1_ANIMATION_4': 'БЕЗЛІМІТНА ПОШТОВА СКРИНЬКА - БЕЗКОШТОВНО',
                'H2_ANIMATION_4': 'Розмір поштової скриньки не обмежений.',
                'H1_ANIMATION_5': 'ЛАКОНІЧНИЙ ДИЗАЙН',
                'H2_ANIMATION_5': 'Простий, зручний та інтуїтивно зрозумілий інтерфейс.',
                'LOGIN_FORM_TITLE': 'Пошта',
                'LOGIN_FIELD_NAME': 'Ім\'я скриньки',
                'EMAIL_DOMAIN': '@ukr.net',
                'PASSWORD_FIELD_NAME': 'Пароль',
                'PUBLIC_COMPUTER_CHECKBOX_NAME': 'Чужий комп\'ютер',
                'CONTINUE_BUTTON_NAME': 'Продовжити',
                'TROUBLE_SIGN_IN_LINK_NAME': 'Не вдається увійти?',
                'SIGN_UP_LINK_NAME': 'Створити скриньку',
                'SUPPORT_TITLE': 'ЦІЛОДОБОВА ПІДТРИМКА',
                'PRIVACY_POLICY_LINK_NAME': 'Угода про конфіденційність',
                'TERMS_OF_SERVICE_LINK_NAME': 'Угода про використання електронної пошти FREEMAIL (mail.ukr.net)'
            }
        case 'ru':
            return {
                'LANGUAGE_BUTTON_NAME': 'Русский',
                'H1_ANIMATION_1': 'КРУГЛОСУТОЧНАЯ СЛУЖБА ПОДДЕРЖКИ',
                'H2_ANIMATION_1': 'По почте и телефону.',
                'H1_ANIMATION_2': 'МГНОВЕННАЯ ДОСТАВКА ПИСЕМ',
                'H2_ANIMATION_2': 'Скорость доставки сообщений – менее одной секунды.',
                'H1_ANIMATION_3': 'САМАЯ ПОПУЛЯРНАЯ УКРАИНСКАЯ ЭЛЕКТРОННАЯ ПОЧТА',
                'H2_ANIMATION_3': '42,5% e-mail пользователей в Украине - с @UKR.NET.*',
                'FOOTER_ANIMATION_3': '*По данным исследования интернет-аудитории Opinion Software Media компании ООО'
                                  ' "Инмайнд Опинион Медиа", апрель 2019 года, n=5000.',
                'H1_ANIMATION_4': 'БЕЗЛИМИТНЫЙ ПОЧТОВЫЙ ЯЩИК – БЕСПЛАТНО',
                'H2_ANIMATION_4': 'Размер почтового ящика не ограничен.',
                'H1_ANIMATION_5': 'ЛАКОНИЧНЫЙ ДИЗАЙН',
                'H2_ANIMATION_5': 'Простой, удобный и интуитивно понятный интерфейс.',
                'LOGIN_FORM_TITLE': 'Почта',
                'LOGIN_FIELD_NAME': 'Имя ящика',
                'EMAIL_DOMAIN': '@ukr.net',
                'PASSWORD_FIELD_NAME': 'Пароль',
                'PUBLIC_COMPUTER_CHECKBOX_NAME': 'Чужой компьютер',
                'CONTINUE_BUTTON_NAME': 'Продолжить',
                'TROUBLE_SIGN_IN_LINK_NAME': 'Не удается войти?',
                'SIGN_UP_LINK_NAME': 'Создать ящик',
                'SUPPORT_TITLE': 'КРУГЛОСУТОЧНАЯ ПОДДЕРЖКА',
                'PRIVACY_POLICY_LINK_NAME': 'Соглашение о конфиденциальности',
                'TERMS_OF_SERVICE_LINK_NAME': 'Соглашение об использовании электронной почты FREEMAIL (mail.ukr.net)'
            }
        case 'en':
            return {
                'LANGUAGE_BUTTON_NAME': 'English',
                'H1_ANIMATION_1': '24/7 SUPPORT SERVICE',
                'H2_ANIMATION_1': 'Via phone and e-mail.',
                'H1_ANIMATION_2': 'LIGHTNING-FAST MESSAGE DELIVERY',
                'H2_ANIMATION_2': 'Average message delivery takes less than one second.',
                'H1_ANIMATION_3': 'THE MOST POPULAR UKRAINIAN WEBMAIL SERVICE',
                'H2_ANIMATION_3': '42,5% of Ukrainian e-mail users are using @UKR.NET.*',
                'FOOTER_ANIMATION_3': '*According to Internet Audience Reseach by Opinion Software Media'
                                  ' (InMind Opinion Media LLC), April 2019, n=5000.',
                'H1_ANIMATION_4': 'UNLIMITED MAILBOX FOR FREE',
                'H2_ANIMATION_4': 'Mailbox will never be full.',
                'H1_ANIMATION_5': 'CLEAN DESIGN',
                'H2_ANIMATION_5': 'Simple, clear and intuitive interface.',
                'LOGIN_FORM_TITLE': 'Mail',
                'LOGIN_FIELD_NAME': 'Login',
                'EMAIL_DOMAIN': '@ukr.net',
                'PASSWORD_FIELD_NAME': 'Password',
                'PUBLIC_COMPUTER_CHECKBOX_NAME': 'Public computer',
                'CONTINUE_BUTTON_NAME': 'Continue',
                'TROUBLE_SIGN_IN_LINK_NAME': 'Trouble signing in?',
                'SIGN_UP_LINK_NAME': 'Sign up',
                'SUPPORT_TITLE': '24/7 SUPPORT SERVICE',
                'PRIVACY_POLICY_LINK_NAME': 'Privacy Policy',
                'TERMS_OF_SERVICE_LINK_NAME': 'FREEMAIL (mail.ukr.net) Terms of Service'
            }
        case _:
            return {}


def get_error_message(language):
    match language:
        case 'uk':
            return 'Неправильні дані'
        case 'ru':
            return 'Неправильные данные'
        case 'en':
            return 'Wrong login or password'
