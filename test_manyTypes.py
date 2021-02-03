import random
import string

import pytest,time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
############################################################
@pytest.mark.sanity
@pytest.mark.regression
def test_setup():
    global driver
    driver=webdriver.Chrome(executable_path="C:/Projects/Automation/Drivers/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(8)
    print("*****Start the FORM test... ******")
@pytest.mark.sanity
def test_Form():
    driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
    driver.find_element_by_id('RESULT_TextField-1').send_keys('Moshe')
    driver.find_element_by_id('RESULT_TextField-2').send_keys('Bar')
    driver.find_element_by_css_selector('input[name="RESULT_TextField-3"]').send_keys('0522444181')
    driver.find_element_by_id('RESULT_TextField-4').send_keys('ISRAEL')
    driver.find_element_by_id('RESULT_TextField-5').send_keys('Rishon')
    driver.find_element_by_css_selector('input[name="RESULT_TextField-6"]').send_keys('pop3@walla.com')
    assert driver.find_element_by_css_selector('input[id="RESULT_RadioButton-7_0"]').is_selected()==False
    driver.find_element_by_xpath('//*[@id="q26"]/table/tbody/tr[1]/td/label').click() #select male gender
    driver.find_element_by_css_selector('label[for="RESULT_CheckBox-8_0"]').click() #select Sunday
    driver.find_element_by_xpath('//*[@id="q15"]/table/tbody/tr[7]/td/label').click() #select saterday
    ddl =Select(driver.find_element_by_css_selector('#RESULT_RadioButton-9'))
    ddl.select_by_value('Radio-1')#select afternoon
    mainTitle=driver.find_element_by_css_selector('div.segment_header').text
    assert mainTitle=="Volunteer Sign Up"
    print('Test ended successfuly!')


def test_hover():
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.find_element_by_id('txtUsername').clear()
    driver.find_element_by_id('txtUsername').send_keys('Admin')
    driver.find_element_by_css_selector('#txtPassword').clear()
    driver.find_element_by_css_selector('#txtPassword').send_keys('admin123')
    driver.find_element_by_css_selector('input.button').click()
    wait=WebDriverWait(driver,10)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.head h1'), 'Dashboard'))
    adminLink=driver.find_element_by_css_selector('a[id="menu_admin_viewAdminModule"]')
    jobLink=driver.find_element_by_css_selector('a[id="menu_admin_Job"]')
    workShiftLnk=driver.find_element_by_css_selector('a[id="menu_admin_workShift"]')
    action=ActionChains(driver)
    action.move_to_element(adminLink).move_to_element(jobLink).click(workShiftLnk).perform()
    # workShiftstitle=driver.find_element_by_xpath('//*[@id="search-results"]/div[1]/h1')
    wait=WebDriverWait(driver,10)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="search-results"]/div[1]/h1'), 'Work Shifts'))
    driver.find_element_by_css_selector('input[id="btnAdd"]').click() #click on Add button
    shiftName=random_generator() + "Idan"
    driver.find_element_by_css_selector('input[name="workShift[name]"]').send_keys(shiftName)
    ddl1 =Select(driver.find_element_by_css_selector('#workShift_workHours_from'))
    ddl1.select_by_value('02:00')#set from hour
    ddl2=Select(driver.find_element_by_id('workShift_workHours_to'))
    ddl2.select_by_value('07:00')
    time.sleep(3)
    assert driver.find_element_by_css_selector('input.time_range_duration').get_attribute('value')=='5'
    driver.find_element_by_xpath('//*[@id="workShift_availableEmp"]/option[16]').click()
    # ddl3=Select(driver.find_element_by_id('workShift_workHours_from'))
    # ddl3.select_by_visible_text('Alice Duval')
    driver.find_element_by_id('btnAssignEmployee').click() #click on add button
    time.sleep(1)
    driver.find_element_by_id('btnSave').click()
    pageElement=driver.find_element_by_css_selector('div[id="content"]').text
    if "Successfully Saved" in pageElement:
        print('Shift was added successfully...')
        assert True
    else:
        print("Shift was NOT created!!!!")
        assert False

    status= searchCustomerByName(shiftName)
    assert status ==True

def test_rightClick():
    print('testing Right click...')
    driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
    button=driver.find_element_by_css_selector('span.context-menu-one')
    copyOption=driver.find_element_by_xpath('/html/body/ul/li[3]')
    ActionChains(driver).context_click(button).perform()
    copyOption.click()
    assert driver.switch_to_alert().text=='clicked: copy'
    time.sleep(4)
    driver.switch_to_alert().accept()

def test_DoubleClick():
    driver.get('http://testautomationpractice.blogspot.com/')
    time.sleep(2)
    button=driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/button')
    ActionChains(driver).double_click(button).perform()
    time.sleep(3)
    field2=driver.find_element_by_css_selector('input[id="field2"]').get_attribute('value')
    assert field2=='Hello World!'

def test_scroll2Element():
    targetElement=driver.find_element_by_xpath('//*[@id="HTML8"]/h2')
    driver.execute_script("arguments[0].scrollIntoView();", targetElement)
    assert targetElement.text == 'Tooltips'
    time.sleep(2)

def test_checkStyle():
    driver.get('http://testautomationpractice.blogspot.com/')
    driver.switch_to.frame('frame-one1434677811')
    # middleEle=driver.find_element_by_css_selector('fauxcolumn-center-outer')
    ele1=driver.find_element_by_css_selector('input[id="FSsubmit"]')
    button=driver.find_element_by_xpath('//*[@id="FSsubmit"]')
    print(ele1.value_of_css_property('color'))
    if ele1.value_of_css_property('background-color')=='rgba(51, 51, 51, 1)':
        print('The coloe test Passed!')
        assert True
    else:
        print('The color is wrong!!! test FAILED!')
        driver.get_screenshot_as_file('.\\screen1.png')
        assert False
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # time.sleep(3)
    # driver.execute_script("window.scrollTo")
    # driver.execute_script("arguments[0].scrollIntoView();", ele1)
    # action=ActionChains(driver)
    # action.move_to_element(ele1).context_click().perform()
    # time.sleep(5)
    # assert ele1.value_of_css_property('background-color')=='rgba(66, 141, 179, 1)'
@pytest.mark.regression
def test_sendKeys():
    driver.get('http://testautomationpractice.blogspot.com/')
    driver.switch_to.frame('frame-one1434677811')

    driver.find_element_by_id('RESULT_TextField-1').send_keys('Idan007')
    time.sleep(2)
    driver.find_element_by_id('RESULT_TextField-1').send_keys(Keys.TAB)
    driver.find_element_by_id('RESULT_TextField-2').send_keys(Keys.TAB)
    time.sleep(5)
    print('Testing using TAB key Passed!!!!')


@pytest.mark.regression
def test_search_string_in_file():#search strings in log file
    file_path='.\\myFile.txt'
    resFile='.\\resFile.txt'
    myFile =open(file_path, 'r')
    lines=myFile.readlines()
    targets=['Fatal', 'Issue']
    results=[]
    for line in lines:  # lines is a list with each item representing a line of the file
        for string in targets:
            if string.casefold() in line:  # Using casefold() to disable the case sensitive!!!
                print(line)
                results.append(line)
                print(results)

    resultsFile=open(resFile, 'w')
    resultsFile.write('These are the results:\n')
    resultsFile.write('*******************************\n')
    resultsFile.writelines(results)

@pytest.mark.sanity
@pytest.mark.regression
def test_tearDown():
    driver.quit()
    print('*******************Finish the test**************')

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def getNoOfRows():
    return len(driver.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr'))

def getNoOfColumns(self):
    return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

def searchCustomerByName(Name):
    flag=False
    for r in range(1,getNoOfRows()+1):
      table=driver.find_element_by_xpath('//*[@id="resultTable"]/tbody')
      name=table.find_element_by_xpath("//table[@id='resultTable']/tbody/tr["+str(r)+"]/td[2]").text
      if name == Name:
          flag = True
          break
    return flag