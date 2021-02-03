import pytest,time, jsonpath, json,requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import select
################################################################################
@pytest.yield_fixture()
def setup():
    global driver
    driver=webdriver.Chrome(executable_path="C:\\Projects\\Automation\\Drivers\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.implicitly_wait(6)

    yield
    driver.quit()

def test_login():
    print('Test1 test login...')
    curTitle= driver.title
    assert curTitle =='OrangeHRM'
    driver.find_element(By.ID, 'txtUsername').clear()
    driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
    driver.find_element_by_id('txtPassword').clear()
    driver.find_element_by_id('txtPassword').send_keys('admin123')
    driver.find_element_by_id('btnLogin').click()
    wait=WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div>h1'), 'Dashboard')) #WAIT FOR DASHBOARD TITLE
    driver.find_element_by_id('welcome').click()
    driver.find_element_by_link_text('Logout').click()
    print("login test ended successfully!")

def test_hover():
    print('Test2 test hover')
    curTitle = driver.title
    assert curTitle == 'OrangeHRM'
    driver.find_element(By.ID, 'txtUsername').clear()
    driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
    driver.find_element_by_id('txtPassword').clear()
    driver.find_element_by_id('txtPassword').send_keys('admin123')
    driver.find_element_by_id('btnLogin').click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div>h1'), 'Dashboard'))  # WAIT FOR DASHBOARD TITLE
    adminMenu=driver.find_element_by_id('menu_admin_viewAdminModule')
    job=driver.find_element_by_id('menu_admin_Job')
    # workShift=driver.find_element_by_link_text('Work Shifts')
    workShift=driver.find_element_by_xpath('//*[@id="menu_admin_workShift"]')
    action=ActionChains(driver)
    action.move_to_element(adminMenu).move_to_element(job).click(workShift).perform()
    time.sleep(5)

def test_rightClick():
    print('Test3: start testing the right click ....')
    driver.get('http://swisnl.github.io/jQuery-contextMenu/demo.html')
    button=driver.find_element_by_xpath('/html/body/div/section/div/div/div/p/span')
    quitOption=driver.find_element_by_xpath('/html/body/ul/li[7]/span')
    ActionChains(driver).context_click(button).click(quitOption).perform()
    currentAlertText=driver.switch_to_alert().text
    assert  currentAlertText == 'clicked: quit'
    driver.switch_to_alert().accept()#click accept
    time.sleep(4)


def test_doubleClick():
    print('Test3:start double click testing')
    driver.get('http://testautomationpractice.blogspot.com/')
    field2=driver.find_element_by_id('field2')
    button=driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/button')
    ActionChains(driver).double_click(button).perform()
    allText=driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/p').text
    assert allText=='Double click on button, the text from Field1 will be copied into Field2.'
    assert field2.get_attribute('value') =="Hello World!"
    time.sleep(3)

def testSendKeys():
    print('Test4:start send keys test...')
    driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
    # wait=WebDriverWait(driver, 10)
    # wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="q19"]/div/h1'), 'Volunteer Sign Up'))
    driver.find_element_by_id('RESULT_TextField-1').send_keys('Idan')
    driver.find_element_by_id('RESULT_TextField-1').send_keys(Keys.TAB)
    driver.find_element_by_id('RESULT_TextField-2').send_keys(Keys.TAB)
    time.sleep(3)

def test_radioAndCheckboxes():
    print('Test5: start radio and checkboxes test...')
    driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
    driver.find_element_by_xpath('//*[@id="q26"]/table/tbody/tr[1]/td/label').is_selected()==False #make sure gender it is unselected
    gender=driver.find_element_by_xpath('//*[@id="q26"]/table/tbody/tr[1]/td/label')
    gender.click()
    time.sleep(2)
    genderAfterClick=driver.find_element_by_id('RESULT_RadioButton-7_0').is_selected()
    print('gender is selected:', genderAfterClick) #validate that the male is selected after click
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="q15"]/table/tbody/tr[1]/td/label').click()  #select sunday
    driver.find_element_by_xpath('//*[@id="q15"]/table/tbody/tr[5]/td/label').click() #select wedensday
    driver.get_screenshot_as_file('.\\image1.png')
    time.sleep(2)

def test_ddl():
    print('Test6: start testing the ddl')
    driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
    ddl =Select(driver.find_element_by_id('RESULT_RadioButton-9'))
    ddl.select_by_index('1') #select by index '1' afternoon
    time.sleep(2)
    ddl.select_by_value('Radio-2') #select by value - Evening
    time.sleep(2)



def test_api1_addNewUser(setup):
    # ENV:
    filePath = ".\\addUser.json"
    addStudent_API = "https://reqres.in/api/users"
    print('Test7A: adding a new user by api.....')
    file=open(filePath, 'r')
    input=file.read()
    input_json=json.loads(input)
    respond=requests.post(addStudent_API, input_json)
    print(respond.status_code)
    assert respond.status_code ==201;
    respond_json=json.loads(respond.text)
    jsonpath.jsonpath(respond_json, 'id')
    print(respond_json)
    id= jsonpath.jsonpath(respond_json, 'id')
    print("id:", id[0])
    id1=str(id[0])

    userApi='https://reqres.in/api/users/'+id1
    userRespond=requests.get(userApi)
    print(userRespond.text)









def test_checkstyle():
    print('Test8: check element style...')
    curTitle = driver.title
    assert curTitle == 'OrangeHRM'
    driver.find_element(By.ID, 'txtUsername').clear()
    driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
    driver.find_element_by_id('txtPassword').clear()
    driver.find_element_by_id('txtPassword').send_keys('admin123')
    driver.find_element_by_id('btnLogin').click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div>h1'), 'Dashboard'))  # WAIT FOR DASHBOARD TITLE
    adminMenue=driver.find_element_by_id('menu_admin_viewAdminModule')
    action=ActionChains(driver)
    action.move_to_element(adminMenue)
    assert adminMenue.value_of_css_property('color')=='rgba(93, 93, 93, 1)'
    describeLink=driver.find_element_by_id('Subscriber_link')
    print(describeLink.value_of_css_property('background'))

def test_scrolling():

    print('test9: scrolling...')
    driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
    imgElement=driver.find_element_by_css_selector('.svg')
    time.sleep(1)
    driver.execute_script("arguments[0].scrollIntoView();", imgElement)
    time.sleep(3)




