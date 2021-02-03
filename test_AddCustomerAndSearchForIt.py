from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import pytest, time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
##############################################################
def test_setup():
    global driver
    driver=webdriver.Chrome(executable_path="C:\\Projects\\Automation\\Drivers\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(8)
    driver.get("https://admin-demo.nopcommerce.com/login")

def test_login():
    webElementEmail=driver.find_element_by_id('Email')
    webElementPassword=driver.find_element_by_id('Password')
    webElemntLoginButton=driver.find_element_by_css_selector('input.button-1')
    webElementEmail.clear()
    webElementPassword.clear()
    webElementEmail.send_keys('admin@yourstore.com')
    webElementPassword.send_keys('admin')
    webElemntLoginButton.click()
    wait=WebDriverWait(driver,10)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.content-header'), 'Dashboard'))


def test_addCustomer():
    driver.find_element_by_link_text('Customers').click()
    driver.find_element_by_xpath('//body/div[3]/div[2]/div[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/span[1]').click()
    driver.find_element_by_css_selector('a.bg-blue').click()
    wait=WebDriverWait(driver,10)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.opened'), 'Customer info'))
    driver.find_element_by_id('Email').send_keys('greek4@walla.com') #set email
    driver.find_element_by_css_selector('input[name="Password"]').send_keys('q1w2e3r4')#set password
    driver.find_element_by_id('FirstName').send_keys('Idan')#set name
    driver.find_element_by_id('LastName').send_keys('Baby')#set username
    driver.find_element_by_xpath('//input[@id="Gender_Male"]').click()#set gender
    driver.find_element_by_id('DateOfBirth').send_keys('1/11/2021')
    driver.find_element_by_id('Company').send_keys('the shark')
    time.sleep(2)
    driver.find_element_by_css_selector('button[name="save"]').click()
    expText=driver.find_element_by_tag_name('body').text
    assert "customer has been added successfully." in expText

def test_customer():
    # driver.find_element_by_link_text('Customers').click()
    # driver.find_element_by_xpath('//body/div[3]/div[2]/div[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/span[1]').click()
    driver.find_element_by_css_selector('input[name="SearchEmail"]').send_keys('greek4@walla.com') #search by email
    driver.find_element_by_css_selector('button#search-customers').click()
    time.sleep(1)
    row=(driver.find_elements_by_xpath("//table[@id='customers-grid']//tbody/tr"))
    rowsNum=len(row)
    print('rowsNum:',rowsNum)
    # colNum=len(driver.find_element_by_xpath('//*[@id="customers-grid"]/tbody/tr/td'))
    table=driver.find_element_by_xpath("//table[@id='customers-grid']")
    for r in range(1, rowsNum+1):
        emailid = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text
        assert emailid =='greek4@walla.com'



def test_teardown():
        driver.quit()
        print("teardown func...")
