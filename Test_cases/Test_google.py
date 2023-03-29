import pytest
import allure
from selenium import webdriver
@allure.description("validates on google")
@allure.severity(severity_level="CRITICAL")
@pytest.mark.regression
def test_google():
    #self.logger.info("**************** Title verification Page***************")
   # driver = setup
    driver=webdriver.chrome()
    driver.get("http://www.google.com")
    gtitle=driver.title
    print(gtitle)