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
time.sleep(3)

#click on the Login button
driver.find_element_by_class_name('btn-primary').click()
time.sleep(3)

#get element to fill email address in email field
driver.find_element_by_id("email").send_keys(email)
time.sleep(5)

#click on the Login button
driver.find_element_by_class_name('btn-primary').click()
time.sleep(3)

#get element to fill password in password field
driver.find_element_by_id("password").send_keys(password)
time.sleep(3)

#check remember me box


#click on the Login button
driver.find_element_by_class_name('btn-primary').click()
time.sleep(5)

#close the browser
driver.close()