from selenium.webdriver.common.by import By


class YandexSearchLocators:
    SEARCH_FIELD = (By.ID, "text")
    SEARCH_BUTTON = (By.CLASS_NAME, "search3__button")
    SEARCH_POPUP = (By.CSS_SELECTOR, "div.mini-suggest__popup.mini-suggest__popup_svg_yes")
    SEARCH_FIRST_LINK = (By.CSS_SELECTOR, "div.Path.Organic-Path.Organic-Path > a > b")
