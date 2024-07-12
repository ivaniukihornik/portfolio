class LoginPageEnv:
    UK_LANGUAGE = 'Українська'
    RU_LANGUAGE = 'Русский'
    EN_LANGUAGE = 'English'
    DEFAULT_LANGUAGE = UK_LANGUAGE
    ALL_LANGUAGES = (UK_LANGUAGE, RU_LANGUAGE, EN_LANGUAGE)

    ANIMATIONS_DURATION = 7

    def get_title(self, language):
        match language:
            case self.UK_LANGUAGE:
                return 'Пошта @ ukr.net - українська електронна пошта • Створи емейл'
            case self.RU_LANGUAGE:
                return 'Почта @ ukr.net - украинская электронная почта • Создать емейл'
            case self.EN_LANGUAGE:
                return 'Mail @ ukr.net - Ukrainian electronic mail • Create email'
            case _:
                return 'Specified language is absent'

    def get_description(self, language):
        match language:
            case self.UK_LANGUAGE:
                return (
                    'Пошта@ukr.net - швидкий і зручний інтерфейс, відправка по e-mail файлів до 50 Гб, поштова скринька'
                    ' з професійним захистом від спаму і вірусів. Створи свій email на домені ukr.net.')
            case self.RU_LANGUAGE:
                return ('Почта@ukr.net - быстрый и удобный интерфейс, отправка по e-mail файлов до 50 Гб, почтовый ящик'
                        ' c профессиональной защитой от спама и вирусов. Создай свой email на домене ukr.net.')
            case self.EN_LANGUAGE:
                return ('Mail@ukr.net - fast and convenient interface, send files up to 50 GB in your email, mailbox'
                        ' with professional anti-spam and anti-virus protection. Create your email on the domain'
                        ' ukr.net.')
            case _:
                return 'Specified language is absent'

    def get_expected_text(self, language):
        match language:
            case self.UK_LANGUAGE:
                return {
                    'ANIMATION_1_TITLE': 'Цілодобова служба підтримки',
                    'ANIMATION_1_PARAGRAPH': 'Поштою і по телефону',
                    'ANIMATION_2_TITLE': 'Найпопулярніша українська електронна пошта',
                    'ANIMATION_2_PARAGRAPH': 'Майже половина всіх користувачів електронної пошти в Україні – з'
                                             ' @UKR.NET',
                    'ANIMATION_3_TITLE': 'Сучасний дизайн',
                    'ANIMATION_3_PARAGRAPH': 'Срібний призер світового конкурсу Indigo Design Awards!',
                    'ANIMATION_4_TITLE': 'Двофакторна автентифікація',
                    'ANIMATION_4_PARAGRAPH': 'Для додаткового захисту вашої скриньки',
                    'ANIMATION_5_TITLE': 'Резервне копіювання',
                    'ANIMATION_5_PARAGRAPH': 'Для відновлення несанкціоновано видалених даних',
                    'ANIMATION_6_TITLE': 'Зручні маркери листів',
                    'ANIMATION_6_PARAGRAPH': 'Маркер останнього прочитаного й відмітки для важливих листів',
                    'ANIMATION_7_TITLE': 'Можливість пересилати великі файли',
                    'ANIMATION_7_PARAGRAPH': 'До 50 ГБ кожен або до 100 ГБ сумарно',
                    'ANIMATION_8_TITLE': 'Темна тема',
                    'ANIMATION_8_PARAGRAPH': 'Для комфорту ваших очей',
                    'ANIMATION_9_TITLE': 'Миттєва доставка листів',
                    'ANIMATION_9_PARAGRAPH': 'Швидкість доставки повідомлень – менше однієї секунди',
                    'ANIMATION_10_TITLE': 'Безлімітна поштова скринька ‑ безкоштовно',
                    'ANIMATION_10_PARAGRAPH': 'Розмір поштової скриньки не обмежений',
                    'ANIMATION_11_TITLE': 'Українській пошті - українські стікери',
                    'ANIMATION_11_PARAGRAPH': 'Сповніть ваші листи настроєм й національним колоритом',
                    'LOGIN_FORM_TITLE': 'Пошта',
                    'LOGIN_FIELD_NAME': 'Ім\'я скриньки',
                    'EMAIL_DOMAIN': '@ukr.net',
                    'PASSWORD_FIELD_NAME': 'Пароль',
                    'PUBLIC_COMPUTER_CHECKBOX_NAME': 'Чужий комп\'ютер',
                    'CONTINUE_BUTTON_NAME': 'Продовжити',
                    'TROUBLE_SIGN_IN_LINK_NAME': 'Не вдається увійти?',
                    'SIGN_UP_LINK_NAME': 'Створити скриньку',
                    'APPS_TITLE': 'Наші офіційні застосунки',
                    'SUPPORT_TITLE': 'Цілодобова підтримка',
                    'PRIVACY_POLICY_LINK_NAME': 'Угода про конфіденційність',
                    'TERMS_OF_SERVICE_LINK_NAME': 'Угода про використання електронної пошти FREEMAIL (mail.ukr.net)'
                }
            case self.RU_LANGUAGE:
                return {
                    'ANIMATION_1_TITLE': 'Круглосуточная служба поддержки',
                    'ANIMATION_1_PARAGRAPH': 'По почте и телефону',
                    'ANIMATION_2_TITLE': 'Самая популярная украинская электронная почта',
                    'ANIMATION_2_PARAGRAPH': 'Почти половина всех пользователей электронной почты в Украине – с'
                                             ' @UKR.NET',
                    'ANIMATION_3_TITLE': 'Современный дизайн',
                    'ANIMATION_3_PARAGRAPH': 'Серебряный призер мирового конкурса Indigo Design Awards!',
                    'ANIMATION_4_TITLE': 'Двухфакторная аутентификация',
                    'ANIMATION_4_PARAGRAPH': 'Для дополнительной защиты вашей почты',
                    'ANIMATION_5_TITLE': 'Резервное копирование',
                    'ANIMATION_5_PARAGRAPH': 'Для восстановления несанкционированно удаленных данных',
                    'ANIMATION_6_TITLE': 'Удобные маркеры писем',
                    'ANIMATION_6_PARAGRAPH': 'Маркер последнего прочитанного и отметки для важных писем',
                    'ANIMATION_7_TITLE': 'Возможность пересылать большие файлы',
                    'ANIMATION_7_PARAGRAPH': 'До 50 ГБ каждый или до 100 ГБ суммарно',
                    'ANIMATION_8_TITLE': 'Темная тема',
                    'ANIMATION_8_PARAGRAPH': 'Для комфорта ваших глаз',
                    'ANIMATION_9_TITLE': 'Мгновенная доставка писем',
                    'ANIMATION_9_PARAGRAPH': 'Скорость доставки сообщений – менее одной секунды',
                    'ANIMATION_10_TITLE': 'Безлимитный почтовый ящик ‑ бесплатно',
                    'ANIMATION_10_PARAGRAPH': 'Размер почтового ящика не ограничен',
                    'ANIMATION_11_TITLE': 'Украинской почте ‑ украинские стикеры',
                    'ANIMATION_11_PARAGRAPH': 'Добавьте в ваши письма настроение и национальный колорит',
                    'LOGIN_FORM_TITLE': 'Почта',
                    'LOGIN_FIELD_NAME': 'Имя ящика',
                    'EMAIL_DOMAIN': '@ukr.net',
                    'PASSWORD_FIELD_NAME': 'Пароль',
                    'PUBLIC_COMPUTER_CHECKBOX_NAME': 'Чужой компьютер',
                    'CONTINUE_BUTTON_NAME': 'Продолжить',
                    'TROUBLE_SIGN_IN_LINK_NAME': 'Не удается войти?',
                    'SIGN_UP_LINK_NAME': 'Создать ящик',
                    'APPS_TITLE': 'Наши официальные приложения',
                    'SUPPORT_TITLE': 'Круглосуточная поддержка',
                    'PRIVACY_POLICY_LINK_NAME': 'Соглашение о конфиденциальности',
                    'TERMS_OF_SERVICE_LINK_NAME': 'Соглашение об использовании электронной почты FREEMAIL'
                                                  ' (mail.ukr.net)'
                }
            case self.EN_LANGUAGE:
                return {
                    'ANIMATION_1_TITLE': '24/7 Support Service',
                    'ANIMATION_1_PARAGRAPH': 'Via phone and e-mail',
                    'ANIMATION_2_TITLE': 'The most popular Ukrainian email service',
                    'ANIMATION_2_PARAGRAPH': 'Nearly half of all email users in Ukraine prefer to use @UKR.NET Mail',
                    'ANIMATION_3_TITLE': 'Modern look',
                    'ANIMATION_3_PARAGRAPH': 'A Silver Winner in UX, Interface and Navigation in Indigo Design Awards!',
                    'ANIMATION_4_TITLE': 'The two-factor authentication',
                    'ANIMATION_4_PARAGRAPH': 'To ensure enhanced security of your account',
                    'ANIMATION_5_TITLE': 'Mailbox content backup',
                    'ANIMATION_5_PARAGRAPH': 'We will restore your messages and contacts in case your account has been'
                                             ' compromised',
                    'ANIMATION_6_TITLE': 'Email marks for your convenience',
                    'ANIMATION_6_PARAGRAPH': 'Marks for last-read and important emails',
                    'ANIMATION_7_TITLE': 'An option to send large files',
                    'ANIMATION_7_PARAGRAPH': 'Up to 50 GB each or 100 GB in total',
                    'ANIMATION_8_TITLE': 'Dark theme',
                    'ANIMATION_8_PARAGRAPH': 'For the comfort of your eyes',
                    'ANIMATION_9_TITLE': 'Messages delivered in lightning-fast speed',
                    'ANIMATION_9_PARAGRAPH': 'On average, messages are delivered in less than one second',
                    'ANIMATION_10_TITLE': 'The unlimited mailbox for free',
                    'ANIMATION_10_PARAGRAPH': 'The mailbox will never become full',
                    'ANIMATION_11_TITLE': 'National stickers for a national email service',
                    'ANIMATION_11_PARAGRAPH': 'Add national spirit to your emails',
                    'LOGIN_FORM_TITLE': 'Mail',
                    'LOGIN_FIELD_NAME': 'Login',
                    'EMAIL_DOMAIN': '@ukr.net',
                    'PASSWORD_FIELD_NAME': 'Password',
                    'PUBLIC_COMPUTER_CHECKBOX_NAME': 'Public computer',
                    'CONTINUE_BUTTON_NAME': 'Continue',
                    'TROUBLE_SIGN_IN_LINK_NAME': 'Trouble signing in?',
                    'SIGN_UP_LINK_NAME': 'Sign up',
                    'APPS_TITLE': 'Our official applications',
                    'SUPPORT_TITLE': '24/7 Support Service',
                    'PRIVACY_POLICY_LINK_NAME': 'Privacy Policy',
                    'TERMS_OF_SERVICE_LINK_NAME': 'FREEMAIL (mail.ukr.net) Terms of Service'
                }
            case _:
                return {}

    def get_wrong_data_error_message(self, language):
        match language:
            case self.UK_LANGUAGE:
                return 'Неправильні дані'
            case self.RU_LANGUAGE:
                return 'Неправильные данные'
            case self.EN_LANGUAGE:
                return 'Wrong login or password'

    def get_empty_login_error_message(self, language):
        match language:
            case self.UK_LANGUAGE:
                return 'Поле має бути заповнене'
            case self.RU_LANGUAGE:
                return 'Поле должно быть заполнено'
            case self.EN_LANGUAGE:
                return 'You can’t leave this empty'

    @staticmethod
    def get_support_content():
        return {
            'MAIL': 'support@ukr.net',
            'VODAFONE': '(050) 204-14-24',
            'KYIVSTAR': '(096) 718-55-52',
            'PHONE': '(044) 235-85-55'
        }

    def get_all_text_elements(self) -> tuple:
        return tuple(self.get_expected_text(self.DEFAULT_LANGUAGE).keys())

    def get_all_support_contacts(self) -> tuple:
        return tuple(self.get_support_content().keys())
