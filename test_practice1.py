import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
######################################################################
@pytest.mark.regression
@pytest.mark.sanity
def test_setUp():
    print('Starting a new test...')
    global driver
    driver = webdriver.Chrome(executable_path="C:/Projects/Automation/Drivers/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(8)
    driver.get('https://opensource-demo.orangehrmlive.com/')

@pytest.mark.regression
def test_login():
    driver.find_element_by_css_selector('input[name="txtUsername"]').clear()
    driver.find_element_by_css_selector('input[name="txtUsername"]').send_keys('Admin')
    driver.find_element_by_css_selector('input[name="txtPassword"]').clear()
    driver.find_element_by_css_selector('input[name="txtPassword"]').send_keys('admin123')
    driver.find_element_by_id('btnLogin').click()
    wait=WebDriverWait(driver,10)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.head'), "Dashboard"))
    driver.find_element_by_css_selector('a[id="welcome"]').click()
    driver.find_element_by_link_text('Logout').click()
    wait.until(EC.text_to_be_present_in_element((By.ID, 'logInPanelHeading'), 'LOGIN Panel'))
    time.sleep(3)

@pytest.mark.sanity
def test_hover():
    driver.find_element_by_css_selector('input[name="txtUsername"]').clear()
    driver.find_element_by_css_selector('input[name="txtUsername"]').send_keys('Admin')
    driver.find_element_by_css_selector('input[name="txtPassword"]').clear()
    driver.find_element_by_css_selector('input[name="txtPassword"]').send_keys('admin123')
    driver.find_element_by_id('btnLogin').click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.head'), "Dashboard"))
    timeElement=driver.find_element_by_id('menu_time_viewTimeModule')
    attendence=driver.find_element_by_id('menu_attendance_Attendance')
    myRecords=driver.find_element_by_id('menu_attendance_viewMyAttendanceRecord')
    action=ActionChains(driver)
    action.move_to_element(timeElement).move_to_element(attendence).click(myRecords).perform()
    time.sleep(5)
#just adding a comment- commit and check auto test running
@pytest.mark.regression
@pytest.mark.sanity

def test_tearDown():
    print('Finish runing the test!')
    driver.quit()
