import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome


class BasePage:

    def __init__(self, browser: Chrome, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait = timeout

    def go_to_site(self):
        return self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def allure_screenshot(self):
        return allure.attach(self.browser.get_screenshot_as_png(),
                             name="Screenshot", attachment_type=AttachmentType.PNG)
