from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By


class Test_automation:

    # def __init__(self):
    #     driver=webdriver.Chrome()
    #



    @pytest.fixture()
    def setup(self):
        driver=webdriver.Chrome()
        self.driver=driver
        return driver

    # @pytest.mark.sanity
    # def test_login_application(self):
    #     driver = webdriver.Chrome()
    #     driver.get("http://183.82.103.245/nareshit/login.php")
    #     time.sleep(5)
    #     driver.find_element(By.XPATH,"//input[@name='txtUserName']").send_keys("admin")
    #
    #     driver.find_element(By.XPATH,"//input[@name='txtPassword']").send_keys("admin")
    #
    #     driver.find_element(By.NAME,"Submit").click()
    #
    #     driver.implicitly_wait(5)
    #

    @pytest.mark.sanity
    def test_login_application(self,setup):

        self.driver.get("http://183.82.103.245/nareshit/login.php")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@name='txtUserName']").send_keys("admin")

        self.driver.find_element(By.XPATH, "//input[@name='txtPassword']").send_keys("admin")

        self.driver.find_element(By.NAME, "Submit").click()

        self.driver.implicitly_wait(5)

        self.driver.find_element_by_link_text("Help").click()

        print(self.driver.title)


        self.driver.switch_to_frame(0)

        self.driver.find_element(By.XPATH,"//input[@class='plainbtn'][@value='Add']")




    # driver.quit()