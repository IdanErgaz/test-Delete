from selenium import webdriver
import time, pytest,re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
######################################################################
def test_setup():
    global driver
    driver=webdriver.Chrome(executable_path="C:\\Projects\\Automation\\Drivers\\chromedriver.exe")
    driver.maximize_window()
    driver.get('http://practice.automationtesting.in/')
    driver.implicitly_wait(15)

def test_shopFilterByPrice():
    driver.find_element_by_link_text('Shop').click()
    assert driver.title=='Products – Automation Practice Site'

    slider = driver.find_element_by_xpath('//*[@id="woocommerce_price_filter-2"]/form/div/div[1]/span[2]')
    time.sleep(3)
    slider_location=slider.location
    print(slider_location)
    move = ActionChains(driver)
    move.drag_and_drop_by_offset(slider,-30,100).perform()  #need to clculate the delta between the current x1 to the desired x2
    time.sleep(3)
    slider_location2=slider.location
    print(slider_location2)
    driver.find_element_by_css_selector('button[type="submit"]').click()
    time.sleep(3)
    prices=driver.find_elements_by_class_name('woocommerce-Price-amount')
    time.sleep(5)
    res = []

    for price in prices:
        op=price.text
        # print(op)
        value = re.sub("[^0-9\.]", "", op)
        #works fine!

    # op=(prices[0].text)
    # value=re.sub("[^0-9\.]", "", op)

        print(value)
        if float(value)>450:
            # print('test fail!!!')
            res.append('fail')
        else:
            # print('Test passed successfully...')
            res.append('pass')
    print(res)
    if 'fail' in res:
        print('test FAIL!!!!!!!!!!!')

    # for price in prices:
    #     print(price.text)
    #     if int(price.text) >450:
    #         print('Filter failed!!!')
    #     else:
    #         print('Filter is OK')
    # slider= driver.find_element_by_xpath('//*[@id="woocommerce_price_filter-2"]/form/div/div[1]/span[2]')
    # move = ActionChains(driver)
    # move.click_and_hold(slider).move_by_offset(86, 0).release().perform()
    # action.drag_and_drop(ele,296,1354).perform()

def test_drag_drop():

    driver.get('https://jqueryui.com/slider/')
    driver.switch_to.frame(0)

    source1 = driver.find_element_by_css_selector('span[class="ui-slider-handle ui-corner-all ui-state-default"]')
    x0=source1.location
    action = ActionChains(driver)
    action.drag_and_drop_by_offset(source1, 100, 100).perform()
    x1=driver.find_element_by_css_selector('span[class="ui-slider-handle ui-corner-all ui-state-default"]').location
    print("x0:", x0, "x1:", x1)
    time.sleep(5)

def test_teardown():
    driver.quit()
