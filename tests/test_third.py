from pages import *
from test_data import *
from tests.utils.utils import *


def test_first_scenario(browser):
    logging.info("Third test is running")

    sbis_main = SbisMain(browser)
    sbis_main.go_to_site(SBIS_URL)
    sbis_main.click_download_sbis()
    logging.info("Download sbis clicked")

    sbis_download = SbisDownload(browser)
    file_size, file_extension = sbis_download.download_file()

    download_path = get_downloads_path()
    wait_for_files_deleted(download_path)
    downloading_file_name = get_last_created_file_in_dir(download_path, f".{file_extension}")

    downloaded_file_size_in_mb = float(os.path.getsize(downloading_file_name) / (1024 * 1024))

    assert round(downloaded_file_size_in_mb, 2) == file_size

    logging.info("Third test passed")
