from selenium import webdriver

driver = webdriver.Firefox()

driver.get('http://www.google.com')
driver.find_element_by_name('q').send_keys('testing with selenium webdriver and python')
driver.find_element_by_name('btnK').click()