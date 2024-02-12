from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from config import *
import time

class ProductPage(BasePage):
    MAIN_PICTURE = (By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-12 div.row div.col-sm-8 ul.thumbnails li:nth-child(1) > a.thumbnail")
    
    BUTTON_FAVORITE = (By.XPATH, "//body/div[@id='product-product']/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]")
    BUTTON_BUY = (By.CSS_SELECTOR, "#button-cart")
    
    INPUT_COUNT = (By.CSS_SELECTOR, "#input-quantity")
    BUTTON_DESCRIPTION = (By.LINK_TEXT, "Описание")
    BUTTON_CHARACTERISTICS = (By.LINK_TEXT, "Характеристики")
    BUTTON_FEEDBACK = (By.PARTIAL_LINK_TEXT, "Отзывов (")

    INPUT_NAME_REVIEW = (By.CSS_SELECTOR, "#input-name")
    INPUT_REVIEW = (By.CSS_SELECTOR, "#input-review")

    BUTTON_REVIEW_MARK = [2, 3, 4, 5, 6]

    BUTTON_REVIEW_MARK = [
        (By.CSS_SELECTOR, review_mark_cs.format(mark))
        for mark in BUTTON_REVIEW_MARK
    ]

    def right_arrow(self, count: int):
        action_chains = ActionChains(self.driver)

        if (count < 0 | count == 1):
            action_chains.send_keys(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT).perform()
        else:
            for _ in range(count):
                action_chains.send_keys(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT).perform()
                time.sleep(1)
        
        time.sleep(1)

