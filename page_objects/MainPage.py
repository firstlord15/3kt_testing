from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
from config import *

class MainPage(BasePage):
    INPUT_SEARCH = (By.CSS_SELECTOR, "div.container div.row div.col-sm-5 div.input-group > input.form-control.input-lg")
    BUTTON_CART_TOTAL = (By.CSS_SELECTOR, "#cart-total")
    BUTTON_CART = (By.XPATH, "//body/nav[@id='top']/div[1]/div[1]/ul[1]/li[4]/a[1]")
    BUTTON_REGLOG = (By.XPATH, "//span[contains(text(),'Личный кабинет')]")
    BUTTON_REGISTER = (By.LINK_TEXT, "Регистрация")
    BUTTON_LOGIN = (By.LINK_TEXT, "Авторизация")
    BUTTON_HOME = (By.LINK_TEXT, "Интернет магазин Opencart")
    
    PRODUCTS = [
        (By.CSS_SELECTOR, product.format(str(i), product_element)) 
        for i in range(1, 5)
    ]
    
    PRODUCTS_BUTTON = [
        (By.CSS_SELECTOR, product.format(str(i), product_button)) 
        for i in range(1, 5)
    ]
    

    
    
