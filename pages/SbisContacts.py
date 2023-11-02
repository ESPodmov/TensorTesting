from .BasePage import BasePage
from selenium.webdriver.common.by import By


class SbisContactsLocators:
    LOCATOR_TENSOR_BANNER = (By.XPATH, '//a[@href="https://tensor.ru/"]')
    LOCATOR_REGION = (By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']")
    LOCATOR_PARTNERS = (By.XPATH, '//div[contains(@class, "sbisru-Contacts-List__name")]')

    @staticmethod
    def LOCATOR_REGION_SELECT(region_name) -> tuple:
        return tuple((By.XPATH, f'//li[@class="sbis_ru-Region-Panel__item"]/span[@title="{region_name}"]'))

    @staticmethod
    def LOCATOR_NAMED_REGION(region_name) -> tuple:
        return tuple((By.XPATH, f"//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link'][text()='{region_name}']"))


class SbisContacts(BasePage):

    def find_tensor_banner_and_click(self):
        tensor_banner = self.find_element(SbisContactsLocators.LOCATOR_TENSOR_BANNER)
        tensor_banner.click()
        tensor_banner_target = tensor_banner.get_attribute("target")
        if tensor_banner_target and tensor_banner_target == "_blank":
            window_handles = self.driver.window_handles
            current_window_index = window_handles.index(self.driver.current_window_handle)
            next_window_index = (current_window_index + 1) % len(window_handles)
            self.driver.switch_to.window(window_handles[next_window_index])
        return tensor_banner

    def _get_region_element(self):
        region_element = self.find_element(SbisContactsLocators.LOCATOR_REGION)
        return region_element

    def get_region(self):
        region_element = self._get_region_element()
        return region_element.get_attribute("innerHTML")

    def wait_for_new_region(self, region_name):
        new_region = self.find_element(SbisContactsLocators.LOCATOR_NAMED_REGION(region_name))
        return new_region.get_attribute("innerHTML")

    def _get_partner_list(self):
        partner_container = self.find_elements(SbisContactsLocators.LOCATOR_PARTNERS)
        return partner_container

    def get_all_partners_names(self):
        partners_list = self._get_partner_list()
        if partners_list is None:
            return None
        return [partner.get_attribute("innerHTML") for partner in partners_list]

    def _find_needed_region(self, region_name: str):
        return self.find_element(SbisContactsLocators.LOCATOR_REGION_SELECT(region_name))

    def change_region(self, region_name: str):
        region_element = self._get_region_element()
        region_element.click()
        needed_region = self._find_needed_region(region_name)
        region_num = needed_region.get_attribute("innerHTML").split(" ")[0]
        needed_region.click()
        return region_num
