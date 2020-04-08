# -- coding: utf-8 --
from selenium import webdriver
import time
email = 'razia.naushin12@gmail.com'
password = '12345678'

#this name was set during registration
name = "Test"

#create driver
driver = webdriver.Chrome(executable_path="./chromedriver")

#open url 
driver.get("https://report.wugo.io/login")
time.sleep(5)

#get element to fill email address in email field
driver.find_element_by_id("email").send_keys(email)
time.sleep(5)

#get element to fill password in password field
driver.find_element_by_id("password").send_keys(password)
time.sleep(3)

#click on the Login button
driver.find_element_by_class_name('btn-primary').click()
time.sleep(5)


#find element google slide
el =  driver.find_elements_by_class_name("card-checkbox")
for i in el:
	el = i.find_elements_by_class_name("check-card-heading")
	for j in el:
		print(j.text)
		if j.text == "Sales Report Generator":
			i.click()

#scroll page
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(5)

#click on the next
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div[4]/button').click()
time.sleep(5)

#choose report example
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div[2]/div[1]/div[1]/ul/li/label').click()
driver.execute_script("window.scrollTo(0, 200)")
time.sleep(2)

#click on the next
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div[2]/button').click()
time.sleep(3)

#click on the dropdown
driver.find_element_by_xpath('//*[@id="app"]/div[1]/main/div/div/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div[1]/div[1]').click()
time.sleep(3)

#choose element 20
driver.find_element_by_id('list-item-72-2').click()

#check if opened reports are less then selected count
el = driver.find_element_by_xpath('//*[@id="app"]/div[1]/main/div/div/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div[1]/div[1]/div')
count = el.text
el = driver.find_elements_by_tag_name("tbody")
for i in el:
	el = i.find_elements_by_tag_name('tr')
	n = 0
	for j in el:
		n += 1
if n <= int(count):
	print("Selected count is: " + str(count))
	print("Open reports count is: " + str(n))
	print("PASS")
else:
	print("FAIL")
	