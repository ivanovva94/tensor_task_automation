import allure
from .base_page import BasePage
from .yandex_search_locators import YandexSearchLocators


class YandexSearch(BasePage):

    @allure.step("Проверка наличия поля поиска")
    def is_search_field_exists(self):
        self.allure_screenshot()
        assert self.is_element_present(*YandexSearchLocators.SEARCH_FIELD), "Поле поиска не найдено"

    @allure.step("Ввод текста")
    def enter_text(self, text):
        search_line = self.browser.find_element(*YandexSearchLocators.SEARCH_FIELD)
        search_line.click()
        search_line.send_keys(text)
        self.allure_screenshot()
        return search_line

    @allure.step("Проверка наличия таблицы с подсказками")
    def is_suggest_popup_exists(self):
        self.allure_screenshot()
        assert self.is_element_present(*YandexSearchLocators.SEARCH_POPUP),\
            "Таблица с подсказками(suggest) не появилась"

    @allure.step("Нажатие на кнопку 'поиск'")
    def click_on_the_search_button(self):
        return self.browser.find_element(*YandexSearchLocators.SEARCH_BUTTON).click()

    @allure.step("Проверка, что 1 ссылка ведет на tensor.ru")
    def is_first_link(self):
        search_result = self.browser.find_element(*YandexSearchLocators.SEARCH_FIRST_LINK).text
        self.allure_screenshot()
        assert search_result == "tensor.ru", "1 ссылка не ведет на сайт tensor.ru"
