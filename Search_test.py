import time
import pytest

from selenium import webdriver
from DaftHomePage import DaftHomePage
from SearchPage import SearchPage
from ResultPage import ResultPage
from AdPage import AdPage

driver = webdriver.Chrome()
DaftHomePage = DaftHomePage(driver)
SearchPage = SearchPage(driver)
ResultPage = ResultPage(driver)
AdPage = AdPage(driver)


def test():
    DaftHomePage.open()
    DaftHomePage.click_on_accept_all()
    DaftHomePage.click_on_for_sale()
    SearchPage.add_location()
    SearchPage.click_filters()
    SearchPage.apply_keyword_filter()
    SearchPage.click_search_results()
    time.sleep(5)
    ResultPage.select_first_item()
    text_to_check = AdPage.key_word_present()
    assert 'garage' in text_to_check, "The word 'garage' is not found"
    driver.quit()
