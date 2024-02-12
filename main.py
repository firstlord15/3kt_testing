import time
from conftest import *
from page_objects.MainPage import MainPage
from page_objects.ProductPage import ProductPage
from page_objects.RegistrationPage import RegistrationPage
from page_objects.CartPage import CartPage

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

def test_second_task(driver):
    time.sleep(1)
    mainPage = MainPage(driver)
    mainPage.click(MainPage.PRODUCTS_BUTTON[2])
    time.sleep(3)

    # time.sleep(1)
    # mainPage.click(MainPage.BUTTON_CART)
    # time.sleep(3) 
