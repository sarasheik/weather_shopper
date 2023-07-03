from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# Create an instance of Chrome WebDriver
browser = webdriver.Chrome()


#The driver.get method will navigate to a page given by the URL
browser.get('https://weathershopper.pythonanywhere.com/')


#function to find the element temperature in the webpage
def find_temperature():
    temperature = browser.find_element(By.ID,"temperature")
    return int(temperature.text[:-2])


#function to go to sunscreen page
def sunscreen():
        browser.find_element("xpath","//button[text() = 'Buy sunscreens']").click()
        browser.find_element("xpath","//*[contains(text(),'Vishy La Shield Sunscreen spf-30')]/following-sibling::button[text() = 'Add']").click()
        #browser.find_element("xpath","//*[contains(text(),'SPF-50')]/following-sibling::p[contains(text(),%s)]/following-sibling::\
            #button[text() = 'Add']").click()



#function to go to moisturizer page
def moisturizer():
        browser.find_element("xpath","//button[text() = 'Buy moisturizers']").click()
        browser.find_element("xpath","//*[contains(text(),'Emmanuel Aloe Vera Beauty Gel')]/following-sibling::button[text() = 'Add']").click()
        #browser.find_element("xpath","//*[contains(text(),'Aloe')]/following-sibling::p[contains(text(),%s)]/\
            #following-sibling::button[text() = 'Add']").click()


def cart():
        browser.find_element("xpath","//button[contains(text(),'Cart -')]").click()


#check the temperature
temperature = find_temperature()
if temperature >= 40:
        sunscreen()       
        cart()
elif temperature <= 40:
        moisturizer()
        cart()


time.sleep(90)
browser.quit()