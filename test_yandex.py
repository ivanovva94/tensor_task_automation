from page.yandex_search import YandexSearch
from page.yandex_image import YandexImage


def test_yandex_search(browser):
    link = "https://ya.ru/"
    page = YandexSearch(browser, link)
    page.go_to_site()
    page.is_search_field_exists()
    page.enter_text("тензор")
    page.is_suggest_popup_exists()
    page.click_on_the_search_button()
    page.is_first_link()


def test_yandex_images(browser):
    link = "https://ya.ru/"
    page = YandexImage(browser, link)
    page.go_to_site()
    page.click_on_all_services_menu()
    page.is_images_icon_exists()
    page.click_on_images_icon()
    page.check_url()
    page.open_first_category()
    page.open_first_image()
    page.switch_image()
