from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from driver import get_driver
from excel import get_excel_records
from whatsapp import automate
import file_utils as fs
import constants as const

if __name__ == "__main__":

    try:
        driver = get_driver()
        driver.get(const.URL)

        files = fs.read_files()
        records = get_excel_records()

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')
            )
        )

        for r in records:
            contact = str(r[0])
            message = str(r[1])

            automate(driver, contact, message, files)

    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        msg = template.format(type(ex).__name__, ex.args)

        print(msg)

        driver.quit()
    finally:
        driver.quit()
