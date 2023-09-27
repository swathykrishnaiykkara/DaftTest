from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DaftHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.daft.ie/'

    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def click_on_accept_all(self):
        button = self.driver.find_element(By.XPATH,"//button[@onclick='CookieConsent.acceptAll();']")
        button.click()

    def click_on_for_sale(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[span[text()='For Sale']]"))
        )
        for_sale_selector = self.driver.find_element(By.XPATH,"//a[span[text()='For Sale']]")
        for_sale_selector.click()


