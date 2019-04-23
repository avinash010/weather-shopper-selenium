"""
Sample script to solve the moisturizer problem.

Find the least expensive mositurizers with Almond and Aloe in name
"""

from selenium import webdriver
import time 

# Create an instance of Firefox WebDriver
browser = webdriver.Chrome()

#navigate
browser.get('http://weathershopper.pythonanywhere.com/moisturizer')
print browser.title

moisturisers = browser.find_elements_by_xpath("//div[contains(@class,'text-center col-4')]")
aloe_min_element = None 
almond_min_element = None 
aloe_min_price = 100000
almond_min_price = 100000 

#Find the least expensive aloe and almond moisturizer
for moisturiser in moisturisers:
     name =  moisturiser.find_element_by_xpath("p[contains(@class,'font-weight-bold top-space-10')]")
     name = name.text.lower()
     price = moisturiser.find_element_by_xpath("p[contains(text(),'Price')]")
     price = price.text 
     price = price.split('Price:')[-1].strip()
     price = price.split('Rs.')[-1].strip()
     print price 
     price = int(price)
     
     if 'aloe' in name:
          if price < aloe_min_price:
               aloe_min_element = moisturiser
               aloe_min_price = price 
     if 'almond' in name:
          if price <  almond_min_price:
               almond_min_element = moisturiser
               almond_min_price = price 
               
print 'Almond min: ',almond_min_price
print 'Aloe min: ',aloe_min_price
aloe_min_element.find_element_by_xpath("button[text()='Add']").click()
almond_min_element.find_element_by_xpath("button[text()='Add']").click()

#click add to cart button
browser.find_element_by_xpath("//button[contains(@class,'nav-link')]").click()

time.sleep(5)

browser.quit()
