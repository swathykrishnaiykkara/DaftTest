from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultPage:
    def __init__(self, driver):
        self.driver = driver

    def select_first_item(self):
        partial_href = "/for-sale/"
        items =(By.XPATH, f'(//a[contains(@href, "{partial_href}")] )[2]')

        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(items)
        )

        # Click the element, but handle Stale Element Reference Exception if it occurs
        try:
            element.click()
        except Exception as e:
            # Re-locate the element and click it again
            element = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(items)
            )
            element.click()


