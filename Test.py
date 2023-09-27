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

try:
    DaftHomePage.open()
    DaftHomePage.click_on_accept_all()
    DaftHomePage.click_on_for_sale()
    SearchPage.add_location()
    SearchPage.click_filters()
    SearchPage.apply_keyword_filter()
    SearchPage.click_search_results()
    ResultPage.select_first_item()
    AdPage.key_word_present()

finally:
    driver.quit()
