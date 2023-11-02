from pages import *
import logging
from test_data import *


def test_first_scenario(browser):
    logging.info("First test is running")

    sbis_main = SbisMain(browser)
    sbis_main.go_to_site(SBIS_URL)
    contacts_menu_element = sbis_main.go_to_contacts()
    assert contacts_menu_element is not None

    sbis_contacts = SbisContacts(browser)
    sbis_contacts.find_tensor_banner_and_click()
    logging.info("Banner found and clicked")

    tensor_main = TensorMain(browser)
    power_in_people = tensor_main.get_power_in_people_header()
    assert power_in_people is not None
    tensor_main.go_to_about()
    logging.info("About clicked")
    current_url = tensor_main.get_current_page_url()
    assert current_url == TENSOR_ABOUT_URL

    logging.info(f"Current url is {TENSOR_ABOUT_URL}")
    tensor_about = TensorAbout(browser)
    working = tensor_about.find_working_title()
    assert working is not None
    logging.info("Working section exists")
    images = tensor_about.get_all_images_in_working()
    needs_width = None
    needs_height = None
    for img in images:
        if needs_height and needs_width:
            assert needs_width == img.get_attribute("width")
            assert needs_height == img.get_attribute("height")
        else:
            needs_width = img.get_attribute("width")
            needs_height = img.get_attribute("height")
    logging.info(f"All pictures have same parameters height:{needs_height} width:{needs_width}")
    logging.info("First test passed")
