from pages.Main_page import MainPage
from config import TestData

#Строка для запуска кода
##python -m pytest -v --driver Chrome --driver-path chromedriver test/*

#Поле ввода имени видно на странице регистрации
def test_main_field_name_on_page(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTR)
    logo = main_page.is_visible(MainPage.FIELD_NAME)
    assert logo == True

#Поле ввода фамилии видно на странице регистрации
def test_main_field_surname_on_page(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTR)
    logo = main_page.is_visible(MainPage.FIELD_SURNAME)
    assert logo == True

#Поле ввода Email/мобильного телефона видно на странице регистрации
def test_main_field_email_on_page(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTR)
    logo = main_page.is_visible(MainPage.EMAIL)
    assert logo == True

#Поле ввода Пароль видно на странице регистрации
def test_main_field_password_on_page(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTR)
    logo = main_page.is_visible(MainPage.PASSWORD)
    assert logo == True

#Поле ввода Пдтверждение пароля видно на странице регистрации
def test_main_field_accept_password_on_page(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTR)
    logo = main_page.is_visible(MainPage.ACCEPT_PASSWORD)
    assert logo == True

#Поле выбора региона видно на странице регистрации
def test_main_field_region_on_page(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTR)
    logo = main_page.is_visible(MainPage.REGION)
    assert logo == True

#Кнопка Логин есть на главной странице
def test_main_login_on_page(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.LOGIN_PAGE)
    logo = main_page.is_visible(MainPage.LOGIN)
    assert logo == True

#На главной странице в разделе логин есть поле ввода Логина
def test_main_login_on_login_page(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.LOGIN_PAGE)
    logo = main_page.is_visible(MainPage.LOGIN_FIELD)
    assert logo == True

#На главной странице в разделе логин есть поле ввода Пароля
def test_main_password_on_login_page(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.LOGIN_PAGE)
    logo = main_page.is_visible(MainPage.LOGIN_PASSWORD)
    assert logo == True

#Кнопка Почта есть на главной странице
def test_main_mail_on_page(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.MAIL_PAGE)
    logo = main_page.is_visible(MainPage.MAIL)
    assert logo == True

#На главной странице в разделе почта есть поле ввода Электронной почты
def test_main_mail_on_mail_page(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.MAIL_PAGE)
    logo = main_page.is_visible(MainPage.MAIL_FIELD)
    assert logo == True

#На главной странице в разделе почта есть поле ввода Пароля
def test_main_password_on_mail_page(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.MAIL_PAGE)
    logo = main_page.is_visible(MainPage.MAIL_PASSWORD)
    assert logo == True

#На главной странице есть кнопка Телефон
def test_main_phone_on_page(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.PHONE_PAGE)
    logo = main_page.is_visible(MainPage.PHONE)
    assert logo == True

#На главной странице в разделе телефон есть поле ввода Мобильный телефон
def test_main_phone_mob_on_page(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.PHONE_PAGE)
    logo = main_page.is_visible(MainPage.PHONE_MOB)
    assert logo == True

#На главной странице в разделе телефон есть поле ввода Пароль
def test_main_password_on_phone_page(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.PHONE_PAGE)
    logo = main_page.is_visible(MainPage.PHONE_PASSWORD)
    assert logo == True

#На главной странице есть кнопка Лицевой счет
def test_main_account_on_page(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.ACCOUNT_PAGE)
    logo = main_page.is_visible(MainPage.ACCOUNT)
    assert logo == True

#На главной странице в разделе лицевой счет есть поле ввода Лицевой счет
def test_main_account_on_account_page(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.ACCOUNT_PAGE)
    logo = main_page.is_visible(MainPage.ACCOUNT_PERSONAL)
    assert logo == True

#На главной странице в разделе лицевой счет есть поле ввода Пароль
def test_main_password_on_account_page(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.ACCOUNT_PAGE)
    logo = main_page.is_visible(MainPage.ACCOUNT_PASSWORD)
    assert logo == True

#Кнопка Запомнить меня есть на главной странице
def test_main_remember_on_page(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REMEMBER_PAGE)
    logo = main_page.is_visible(MainPage.REMEMBER)
    assert logo == True

#Кнопка Зарегестрироваться есть на главной странице
def test_main_registration_on_page(driver):
    main_page = MainPage(driver)
    logo = main_page.is_visible(MainPage.REGISTRATION)
    assert logo == True


