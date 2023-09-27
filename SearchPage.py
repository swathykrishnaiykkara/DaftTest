from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def add_location(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, '
                                                  '"CountyAreaFilter__AutosizeInputStyled-gf5jf1-3")]/input'))
        )
        search_input = self.driver.find_element(By.XPATH, '//div[contains(@class, '
                                                          '"CountyAreaFilter__AutosizeInputStyled-gf5jf1-3")]/input')
        search_input.click()
        search_input.send_keys("Dublin")
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//ul[@role='listbox']"))
        )

        first_item = self.driver.find_element(By.XPATH, "//li[@id='location-item-0']")
        first_item.click()

    def click_filters(self):
        filter_click = self.driver.find_element(By.XPATH, "//button[@aria-label='Filters']")
        filter_click.click()

    def apply_keyword_filter(self):

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "keywordtermsModal"))
        )
        keyword_filter = self.driver.find_element(By.ID, "keywordtermsModal")
        keyword_filter.send_keys('garage')

    def click_search_results(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='filters-modal-show-results-button']"))
        )
        button = self.driver.find_element(By.XPATH, "//button[@data-testid='filters-modal-show-results-button']")
        button.click()
