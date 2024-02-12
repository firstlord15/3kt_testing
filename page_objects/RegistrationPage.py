from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
from config import *

class RegistrationPage(BasePage):
    INPUT_FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    INPUT_LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    INPUT_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#input-confirm")
    BUTTON_ACCEPTANCE = (By.XPATH, "//body/div[@id='account-register']/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]")
    BUTTON_NEXT = (By.XPATH, "//body/div[@id='account-register']/div[1]/div[1]/form[1]/div[1]/div[1]/input[2]")
    BUTTON_TRUE_SUBNEWS = (By.XPATH, "//body/div[@id='account-register']/div[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/label[1]/input[1]")
    BUTTON_FALSE_SUBNEWS = (By.XPATH, "//body/div[@id='account-register']/div[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/label[2]/input[1]")
