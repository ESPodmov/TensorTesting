from .BasePage import BasePage
from selenium.webdriver.common.by import By


class TensorAboutLocators:
    LOCATOR_WORKING = (By.XPATH, "//h2[text()='Работаем']")
    LOCATOR_IMAGES_IN_WORKING = (By.TAG_NAME, "img")
    LOCATOR_WORKING_PARENT = (By.XPATH, f"{LOCATOR_WORKING[1]}/parent::node()/parent::node()")


class TensorAbout(BasePage):

    def find_working_title(self):
        return self.find_element(TensorAboutLocators.LOCATOR_WORKING)

    def get_all_images_in_working(self):
        working_title_parent_parent = self.find_element(TensorAboutLocators.LOCATOR_WORKING_PARENT)
        return self.find_elements_in_element(working_title_parent_parent, TensorAboutLocators.LOCATOR_IMAGES_IN_WORKING)
