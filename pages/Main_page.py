from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import os,pickle

from pages.Base_page import BasePage
from config import TestData

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    FIELD_NAME = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/div/input")
    FIELD_SURNAME = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input")
    PASSWORD = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[1]/div/input")
    ACCEPT_PASSWORD = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[2]/div/input")
    EMAIL = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[3]/div/input")
    REGION = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/div/input")
    REGISTR = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[6]/a")
    LOGIN = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/div[3]")
    LOGIN_PAGE = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/div[3]")
    LOGIN_FIELD = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input")
    LOGIN_PASSWORD = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/input")
    MAIL = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/div[2]")
    MAIL_PAGE = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/div[2]")
    MAIL_FIELD = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input")
    MAIL_PASSWORD = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/input")
    PHONE = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/div[1]")
    PHONE_PAGE = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/div[1]")
    PHONE_MOB = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input")
    PHONE_PASSWORD = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/input")
    REMEMBER = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[3]/label/span[2]/span[1]")
    REMEMBER_PAGE = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[3]/label/span[2]/span[1]")
    REGISTRATION = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[6]/a")
    ACCOUNT = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/div[4]")
    ACCOUNT_PAGE = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/div[4]")
    ACCOUNT_PERSONAL = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input")
    ACCOUNT_PASSWORD = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/input")











