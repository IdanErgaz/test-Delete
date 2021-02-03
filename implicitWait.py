from selenium import webdriver


driver=webdriver.Chrome(executable_path="C:\\Projects\\Automation\\Drivers\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element_by_id('Email').send_keys('admin@yourstore.com')
driver.find_element_by_id('Password').send_keys('admin')
driver.find_element_by_css_selector('input[type="submit"]').click()

print('Finish testing...')
driver.quit()



