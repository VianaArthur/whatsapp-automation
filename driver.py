from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import constants as const


def get_driver():
    options = Options()
    options.binary_location = const.GOOGLE_CHROME_BIN
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(executable_path=const.CHROME_DRIVER, options=options)
    return driver
