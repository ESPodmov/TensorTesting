from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self, url):
        return self.driver.get(url)

    @staticmethod
    def find_element_in_element(element: WebElement, locator: tuple):
        return element.find_element(locator[0], locator[1])

    @staticmethod
    def find_elements_in_element(element: WebElement, locator: tuple):
        return element.find_elements(locator[0], locator[1])

    def get_current_page_url(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.presence_of_element_located((By.TAG_NAME, "body")))
        return self.driver.current_url

    def get_current_tab_title(self):
        return self.driver.title

    def move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        return
