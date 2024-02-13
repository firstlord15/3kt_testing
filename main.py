import time
from conftest import *
from config import *
from page_objects.MainPage import MainPage
from page_objects.ProductPage import ProductPage
from page_objects.RegistrationPage import RegistrationPage
from page_objects.CartPage import CartPage
from selenium.webdriver.common.by import By

def first_task(driver):
    time.sleep(1)
    mainPage = MainPage(driver)
    mainPage.click(MainPage.PRODUCTS[0])
    time.sleep(1)
    
    productPage = ProductPage(driver)
    productPage.click(ProductPage.MAIN_PICTURE)
    time.sleep(1)
    productPage.right_arrow(3)
    time.sleep(2)

def second_task(driver):
    time.sleep(3)
    mainPage = MainPage(driver)
    mainPage.click(MainPage.PRODUCTS_BUTTON[0])
    mainPage.click(MainPage.PRODUCTS_BUTTON[1])
    mainPage.click(MainPage.BUTTON_CART)
    time.sleep(3)

def third_task(driver):
    time.sleep(3)
    mainPage = MainPage(driver)
    mainPage.click(MainPage.DROPDOWN_PC)
    mainPage.click(MainPage.LI_PC)
    time.sleep(3)

def test_forth_task(driver):
    time.sleep(3)
    mainPage = MainPage(driver)
    mainPage.click(MainPage.BUTTON_REGLOG)
    mainPage.click(MainPage.BUTTON_REGISTER)
    time.sleep(3)

    registrationPage = RegistrationPage(driver)
    registrationPage.registration()
    registrationPage.click(RegistrationPage.BUTTON_TRUE_SUBNEWS)
    registrationPage.click(RegistrationPage.BUTTON_ACCEPTANCE)
    registrationPage.click(RegistrationPage.BUTTON_NEXT)
    time.sleep(3)

