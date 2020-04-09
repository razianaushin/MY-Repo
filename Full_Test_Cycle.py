# -- coding: utf-8 --
from selenium import webdriver
import time
email = 'razia.naushin12@gmail.com'
password = '12345678'

#this name was set during registration
name = "Test"

#create driver
driver = webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()

#open url 
driver.get("https://report.wugo.io/login")
#time.sleep(5)

#get element to fill email address in email field
driver.find_element_by_id("email").send_keys(email)
#time.sleep(5)

#get element to fill password in password field
driver.find_element_by_id("password").send_keys(password)
#time.sleep(3)

#click on the Login button
driver.find_element_by_class_name('btn-primary').click()
#time.sleep(5)

#find element "Amazon Reports"
el =  driver.find_elements_by_class_name("card-checkbox")
for i in el:
	el = i.find_elements_by_class_name("check-card-heading")
	for j in el:
		print(j.text)
		if j.text == "Amazon Reports":
			i.click()	
	#time.sleep(3)


#find element "Google Trends Reports"
el =  driver.find_elements_by_class_name("card-checkbox")
for i in el:
	el = i.find_elements_by_class_name("check-card-heading")
	for j in el:
		print(j.text)
		if j.text == "Google Trends Reports":
			i.click()
	#time.sleep(3)
	
	
#find element "Instagram Keywords Reports"
el =  driver.find_elements_by_class_name("card-checkbox")
for i in el:
	el = i.find_elements_by_class_name("check-card-heading")
	for j in el:
		print(j.text)
		if j.text == "Instagram Keywords Reports":
			i.click()
	#time.sleep(3)	


#find element "Sales Report Generator"
el =  driver.find_elements_by_class_name("card-checkbox")
for i in el:
	el = i.find_elements_by_class_name("check-card-heading")
	for j in el:
		print(j.text)
		if j.text == "Sales Report Generator":
			i.click()
	#time.sleep(3)
	
#scroll page
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(5)

#click on the next
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div[4]/button').click()
time.sleep(3)

#choose Amazon Report example (All Check box)
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div[1]/div/div[1]/div/div').click()

#scroll page
driver.execute_script("window.scrollTo(0, 200)")
time.sleep(3)

#choose report example (Multiple)
#driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div[2]/div[1]/ul/li/label').click()
#driver.execute_script("window.scrollTo(0, 200)")
#time.sleep(2)

#driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div[2]/div[2]/ul/li/div[1]').click()
#driver.execute_script("window.scrollTo(0, 200)")
#time.sleep(2)


#click on the next
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/button[1]').click()
time.sleep(3)

#choose Google Report example (All Check box)
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div[1]/div/div[1]/div/div').click()

#scroll page
driver.execute_script("window.scrollTo(0, 200)")
time.sleep(3)

#click on the next
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div[2]/button').click()
time.sleep(3)

#choose Instagram Report example (All Check box)
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div[1]/div/div[1]/div/div').click()

#scroll page
driver.execute_script("window.scrollTo(0, 200)")
time.sleep(3)

#click on the next
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/button[1]').click()
time.sleep(3)

#choose Sales Presentation Report example (All Check box)
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div[1]/div/div[1]/div/div').click()

#scroll page
driver.execute_script("window.scrollTo(0, 200)")
time.sleep(3)

#click on the next
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div[2]/button').click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[1]/div/div[1]/button[1]').click()
time.sleep(2)
driver.find_element_by_id('input-112').click()
driver.find_element_by_id('input-112').send_keys("Demo")
driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div/div[3]/button[2]/span').click()
time.sleep(3)

#click on the Action
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div[2]/table/tbody/tr[1]/td[7]/div/button').click()
#time.sleep(3)

#close the browser	
#driver.close()
			
			
			
			
			
			
			