import pytest
from selenium import webdriver
from tests.utils.utils import *


@pytest.fixture(scope="function")
def browser():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger()
    file_handler = logging.FileHandler(f'{get_logs_path()}\\pytest_logs.txt', mode='a')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    options = webdriver.ChromeOptions()
    prefs = {
        'download.default_directory': get_downloads_path(),
        "safebrowsing.disable_download_protection": True,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    }
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    logging.info("Tests running")

    yield driver

    logger.removeHandler(file_handler)
    driver.quit()
