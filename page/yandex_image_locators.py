from selenium.webdriver.common.by import By


class YandexImageLocators:
    ALL_SERVICES = (By.XPATH, "//a[@title='Все сервисы']")
    IMAGES_ICON = (By.CSS_SELECTOR, "div.services-pinned__more-popup-list > a:nth-child(14)")
    IMAGES_FIRST_CAT = (By.CSS_SELECTOR, "div.PopularRequestList-Item.PopularRequestList-Item_pos_0")
    IMAGES_FC_RESULT = (By.XPATH, "//input[@class='input__control mini-suggest__input']")
    FIRST_IMAGE = (By.CSS_SELECTOR, ".serp-item_pos_0")
    ORIGIN_IMAGE = (By.CSS_SELECTOR, ".MMImage-Origin")
    NEXT_BUTTON = (By.CSS_SELECTOR, ".CircleButton_type_next")
    PREV_BUTTON = (By.CSS_SELECTOR, ".CircleButton_type_prev")
