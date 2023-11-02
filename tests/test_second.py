from pages import *
import logging
from test_data import *


def test_first_scenario(browser):
    logging.info("Second test is running")

    sbis_main = SbisMain(browser)
    sbis_main.go_to_site(SBIS_URL)
    contacts_menu_element = sbis_main.go_to_contacts()
    assert contacts_menu_element is not None

    sbis_contacts = SbisContacts(browser)
    start_region = sbis_contacts.get_region()
    logging.info(f"Current region is {start_region}")
    assert start_region == REGION
    logging.info(f"Current region is equal to {REGION}")

    start_partners = sbis_contacts.get_all_partners_names()
    assert start_partners is not None
    logging.info(f"Current partners is {start_partners}")

    region_num = sbis_contacts.change_region(NEEDED_REGION)
    new_region = sbis_contacts.wait_for_new_region(NEEDED_REGION)
    assert new_region == NEEDED_REGION
    new_partners = sbis_contacts.get_all_partners_names()
    assert new_partners != start_partners
    logging.info("Region has been changed successfully")

    assert NEEDED_REGION in sbis_contacts.get_current_tab_title()
    assert region_num in sbis_contacts.get_current_page_url()
    logging.info("Url and title have been updated")

    logging.info("Second test passed")
