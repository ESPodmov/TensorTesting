import logging
import re
from .BasePage import BasePage
from selenium.webdriver.common.by import By


class SbisDownloadLocators:
    LOCATOR_SBIS_PLUGIN = (By.XPATH, '//div[@data-id="plugin"]')
    LOCATOR_SBIS_PLUGIN_WINDOWS_TAB = (By.XPATH, '//span[contains(@class, "js-innerTabPlugin")][text()="Windows"]')
    LOCATOR_SBIS_WEB_DOWNLOADER_SECTION = (
        By.XPATH, '//h3[contains(text(), "Веб-установщик")]/parent::node()/parent::node()')
    LOCATOR_DOWNLOAD_IN_WEB_DOWNLOADER_SECTION = (By.TAG_NAME, 'a')
    LOCATOR_MAIN_WRAPPER = (By.XPATH, '//body/div[@hidefocus="true"]')


class SbisDownload(BasePage):

    def _find_sbis_plugin(self):
        return self.find_element(SbisDownloadLocators.LOCATOR_SBIS_PLUGIN)

    def _find_windows_tab(self):
        return self.find_element(SbisDownloadLocators.LOCATOR_SBIS_PLUGIN_WINDOWS_TAB)

    def _select_window_download_tab(self):
        self._find_windows_tab().click()
        logging.info("Windows download tab selected")

    def _select_sbis_plugin_tab(self):
        self.find_element(SbisDownloadLocators.LOCATOR_MAIN_WRAPPER)
        el = self._find_sbis_plugin()
        el.click()
        logging.info("Sbis plugin tab selected")

    def _find_web_downloader_section(self):
        return self.find_element(SbisDownloadLocators.LOCATOR_SBIS_WEB_DOWNLOADER_SECTION)

    def _find_download_element(self):
        return self.find_element_in_element(self._find_web_downloader_section(),
                                            SbisDownloadLocators.LOCATOR_DOWNLOAD_IN_WEB_DOWNLOADER_SECTION)

    def download_file(self):
        self._select_sbis_plugin_tab()
        self._select_window_download_tab()
        download_element = self._find_download_element()
        download_element_inner_html = download_element.get_attribute("innerHTML")
        download_element_inner_html = download_element_inner_html.split("(")[1]
        file_extension = download_element_inner_html.split(" ")[0].lower()
        file_size = float(re.findall(r'\d+\.\d+|\d+', download_element_inner_html)[0])
        download_element.click()
        return file_size, file_extension
