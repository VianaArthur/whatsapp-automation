from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import time
import random

import file_utils as fs
import constants as const


def automate(driver, contact, message, files):
    search_contact(driver, contact)
    send_msg(driver, message)

    filtered_files = fs.filter_files(contact, files)

    for file in filtered_files:
        send_file(driver, file)

    time.sleep(random.random())


def search_contact(driver, contact):
    search_field = driver.find_element_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]'
    )

    search_field.click()
    search_field.send_keys(contact)
    search_field.send_keys(Keys.ENTER)


def send_msg(driver, message):
    msg_field = driver.find_element_by_xpath(
        '//div[contains(@class,"copyable-area")]//div[contains(@class,"copyable-text selectable-text")]'
    )

    msg_field.click()
    msg_field.send_keys(str(message))
    msg_field.send_keys(Keys.ENTER)


def send_file(driver, file):
    time.sleep(random.uniform(2, 4))

    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    file_field = driver.find_element_by_css_selector("input[type='file']")

    file_name = file["name"]
    full_path = f"{const.FILES_FOLDER}/{file_name}"

    if not Path(full_path).is_file():
        return

    file_field.send_keys(full_path)

    send_field = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-icon='send']"))
    )

    send_field.click()

    WebDriverWait(driver, 60).until(
        EC.invisibility_of_element_located(
            (By.CSS_SELECTOR, "span[data-icon*='cancel']")
        )
    )

    time.sleep(random.random())

    fs.move_file(full_path, file)
