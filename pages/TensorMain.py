from .BasePage import BasePage
from selenium.webdriver.common.by import By


class TensorMainLocators:
    LOCATOR_TENSOR_POWER_IN_PEOPLE = (
        By.XPATH, '//p[contains(@class, "tensor_ru-Index__card-title")][text()="Сила в людях"]')
    LOCATOR_ABOUT_IN_POWER_IN_PEOPLE = (By.XPATH, f"{LOCATOR_TENSOR_POWER_IN_PEOPLE[1]}/parent::node()/p/a")
    LOCATOR_COOKIE = (By.XPATH, "//div[contains(@class, 'tensor_ru-CookieAgreement__close')]")
    LOCATOR_TENSOR_COOKIE_CONTAINER = (By.XPATH, '//div[contains(@class, "tensor_ru-CookieAgreement")]')


class TensorMain(BasePage):

    def get_power_in_people_header(self):
        power_in_people_header = self.find_element(TensorMainLocators.LOCATOR_TENSOR_POWER_IN_PEOPLE)
        return power_in_people_header

    def _find_cookie_container(self):
        cookie_container = self.find_element(TensorMainLocators.LOCATOR_TENSOR_COOKIE_CONTAINER)
        return cookie_container

    def _find_cookie_close(self):
        cookie_close = self.find_element(TensorMainLocators.LOCATOR_COOKIE)
        return cookie_close

    def _close_cookie(self):
        cookie_container = self._find_cookie_container()
        if "ws-hidden" in cookie_container.get_attribute("class"):
            return
        cookie_close = self._find_cookie_close()
        cookie_close.click()
        return

    def go_to_about(self):
        about = self.find_element(TensorMainLocators.LOCATOR_ABOUT_IN_POWER_IN_PEOPLE)
        self._close_cookie()
        self.move_to_element(about)
        about.click()
        return about
