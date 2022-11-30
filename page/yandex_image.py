import allure
from .base_page import BasePage
from .yandex_image_locators import YandexImageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YandexImage(BasePage):

    @allure.step("Клик на меню 'Все сервисы'")
    def click_on_all_services_menu(self):
        services_menu = self.browser.find_element(*YandexImageLocators.ALL_SERVICES)
        services_menu.click()
        self.allure_screenshot()
        return services_menu

    @allure.step("Проверка нахождения иконки 'Картинки'")
    def is_images_icon_exists(self):
        assert self.is_element_present(*YandexImageLocators.IMAGES_ICON), \
            "Элемент 'Картинки' не найден в всплывающем окне"

    @allure.step("Клик на иконку 'Картинки'")
    def click_on_images_icon(self):
        icon = self.browser.find_element(*YandexImageLocators.IMAGES_ICON)
        icon.click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.allure_screenshot()
        return icon

    @allure.step("Проверка текущего URL")
    def check_url(self):
        current_url = self.browser.current_url
        assert current_url == "https://yandex.ru/images/", "Загружена страница с другим URL"

    @allure.step("Открытие 1 категории. Проверка названия категории в поле поиска")
    def open_first_category(self):
        first_cat = self.browser.find_element(*YandexImageLocators.IMAGES_FIRST_CAT)
        first_cat_name = first_cat.get_attribute("data-grid-text")
        first_cat.click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.element_to_be_clickable(YandexImageLocators.FIRST_IMAGE))
        first_cat_result = self.browser.find_element(*YandexImageLocators.IMAGES_FC_RESULT).get_attribute("value")
        self.allure_screenshot()
        assert first_cat_name == first_cat_result, "Название категории не отображается в поле поиска"

    @allure.step("Открытие 1 картинки")
    def open_first_image(self):
        first_img = self.browser.find_element(*YandexImageLocators.FIRST_IMAGE)
        first_img.click()
        self.allure_screenshot()
        assert self.is_element_present(*YandexImageLocators.ORIGIN_IMAGE), "Картинка не открылась"

    @allure.step("Проверка на корректность смены изображений")
    def switch_image(self):
        next_button = self.browser.find_element(*YandexImageLocators.NEXT_BUTTON)
        prev_button = self.browser.find_element(*YandexImageLocators.PREV_BUTTON)
        origin_image = self.browser.find_element(*YandexImageLocators.ORIGIN_IMAGE).get_attribute("src")
        next_button.click()
        next_image = self.browser.find_element(*YandexImageLocators.ORIGIN_IMAGE).get_attribute("src")
        self.allure_screenshot()
        prev_button.click()
        prev_image = self.browser.find_element(*YandexImageLocators.ORIGIN_IMAGE).get_attribute("src")
        self.allure_screenshot()
        assert origin_image != next_image, "Картинка не изменилась"
        assert origin_image == prev_image, "Картинка не соответствует начальной"
