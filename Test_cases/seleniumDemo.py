import time

from selenium import webdriver
import pytest

class Test_seleniumDemo:

    driver = webdriver.Chrome()
    # driver.get("http://www.google.com")
    # gtitle = driver.title
    # print(gtitle)

    @pytest.mark.smoke
    def test_openapplication(self):
        self.driver.get("http://tutorialsninja.com/demo")
        try:
            time.sleep(5)
        except:
            self.driver.implicitly_wait(5)

        self.driver.maximize_window()
        title=self.driver.title
        print(title)
        time.sleep(10)

        self.driver.find_element_by_xpath("//a[contains(text(),'Apple Cinema 30')]").click()

        new_title=self.driver.title
        print(new_title)
        self.driver.quit()
