from .BasePage import BasePage
from selenium.webdriver.common.by import By


class SbisMainLocators:
    LOCATOR_SBIS_CONTACTS = (By.XPATH, '//li/a[@href="/contacts"]')
    LOCATOR_SBIS_COOKIE = (By.XPATH, '//div[contains(@class, "sbis_ru-CookieAgreement")]')
    LOCATOR_SBIS_COOKIE_CLOSE = (By.XPATH, '//div[contains(@class, "sbis_ru-CookieAgreement__close")]')
    LOCATOR_FOOTER_DOWNLOAD_SBIS = (By.XPATH, '//a[@class="sbisru-Footer__link"][text()="Скачать СБИС"]')


class SbisMain(BasePage):

    def go_to_contacts(self):
        contacts_bar_element = self.find_element(SbisMainLocators.LOCATOR_SBIS_CONTACTS)
        contacts_bar_element.click()
        return contacts_bar_element

    def _find_cookie_container(self):
        cookie_container = self.find_element(SbisMainLocators.LOCATOR_SBIS_COOKIE)
        return cookie_container

    def _find_cookie_close(self):
        cookie_close = self.find_element(SbisMainLocators.LOCATOR_SBIS_COOKIE_CLOSE)
        return cookie_close

    def _close_cookie(self):
        cookie_container = self._find_cookie_container()
        if "ws-hidden" in cookie_container.get_attribute("class"):
            return
        cookie_close = self._find_cookie_close()
        cookie_close.click()
        return

    def _find_download_sbis(self):
        download_sbis = self.find_element(SbisMainLocators.LOCATOR_FOOTER_DOWNLOAD_SBIS)
        return download_sbis

    def click_download_sbis(self):
        download_sbis = self._find_download_sbis()
        self.move_to_element(download_sbis)
        self._close_cookie()
        download_sbis.click()
        return download_sbis
