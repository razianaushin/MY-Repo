# -- coding: utf-8 --
from selenium import webdriver
import time
email = 'razia.naushin12@gmail.com'
password = '12345678'
#this name was set during registration
name = "Test"

#create driver
driver = webdriver.Chrome(executable_path="./chromedriver")

#open url "gmail.com"
driver.get("https://report.wugo.io/login")



# get element to fill email address in email field
driver.find_element_by_id("email").send_keys(email)

# get element to fill password in email field
driver.find_element_by_id("password").send_keys(password)

#click on the submit button
driver.find_element_by_class_name('btn-primary').click()