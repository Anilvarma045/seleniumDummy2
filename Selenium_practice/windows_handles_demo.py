from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@name='Myname']").click()
print(driver.title)

# 1 . store the current window id in a variable
p=driver.current_window_handle

# 2 . store the all child windows id's in variables using window_handles
cwd=driver.window_handles

#3 . iterating the windows handling until the matching to required window

for w in cwd:                   # run with in the loop to for comparison
    if(w!=p):                   # if iterating window not equal to current window perform switch operation
        driver.switch_to.window(w)


"""     
SUMMERY:

requirement: when we switched to another window by clicking link then we should come back to orginal window
methods:
    1. current_window_handle()  : it capture the id of the current window: later we come to this 
    2. window_handles:   it will retreave  all the open windows by driver and store the id in a variable as a list
    3. switch_to.window(w): by using this we can switch operation between window. take the argument as a window id

"""