import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
   driver=webdriver.Chrome()
   yield
   driver.quit()
   return driver

############ PY TesT Html Reports   ################################

def pytest_configure(config):
   """
   :type config: here it is we create a meta 0data as configuration.
   """
   config._metadata['project Name']=   'Orange Hrm'
   config._metadata['Module Name']  =  'V.12'
   config._metadata['tester'] = 'Anil_Tester'
   config._metadata['year'] = 2023

# it is hook for delete/modify Enviroment info to Html Reports
@pytest.mark.optionalhook
def pytett_metadata(metadata):
   metadata.pop("JAVA_HOME", None)
   metadata.pop("plugins", None)