import pytest
from selenium import webdriver



@pytest.mark.sanity
def test_facebookhomepage(setup):
    #logger.info("**************** Title verification Page***************")
    driver = setup

    driver.get("http://www.facebook.com")

    ptitle=driver.title
    print(ptitle)



