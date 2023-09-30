from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdPage:
    def __init__(self, driver):
        self.driver = driver

    def key_word_present(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@aria-label = 'Back']")))
        div_element = self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="description"]')
        div_text = div_element.text
        return div_text




