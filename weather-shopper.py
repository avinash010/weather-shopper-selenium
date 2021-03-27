"""
Sample script to test weather shopper application.
Get the least expensive mositurizers with Almond and Aloe in their product name
"""

from selenium import webdriver
import time 

# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()

# Navigate to weatheshopper main page 
driver.get('http://weathershopper.pythonanywhere.com/')

# Click on Buy moisturizer button and check if the title of page is proper
driver.find_element_by_xpath("//button[text()='Buy moisturizers']").click()
print(driver.title)
assert driver.title == "The Best Moisturizers in the World!"

# Get all moisturizer element
moisturizers = driver.find_elements_by_xpath("//div[contains(@class,'text-center col-4')]")
aloe_min_price = 999999
almond_min_price = 999999
aloe_min_price_element = None 
almond_min_price_element = None
time.sleep(10)
# Find the least expensive aloe vera and almond moisturizer
for moisturizer in moisturizers:
     name =  moisturizer.find_element_by_xpath("p[contains(@class,'font-weight-bold top-space-10')]")
     name = name.text.lower()
     price = moisturizer.find_element_by_xpath("p[contains(text(),'Price')]")
     price = price.text 
     price = price.split('Price:')[-1].strip()
     price = price.split('Rs.')[-1].strip()
     price = int(price)
     
     if 'aloe' in name:
          if price < aloe_min_price:
               aloe_min_price_element = moisturizer
               aloe_min_price = price 
     if 'almond' in name:
          if price <  almond_min_price:
               almond_min_price_element = moisturizer
               almond_min_price = price 
               
print ('Almond min: ',almond_min_price)
print ('Aloe min: ',aloe_min_price)

# Add min price product to cart
aloe_min_price_element.find_element_by_xpath("button[text()='Add']").click()
almond_min_price_element.find_element_by_xpath("button[text()='Add']").click()

# Go to cart link
driver.find_element_by_xpath("//button[contains(@class,'nav-link')]").click()

time.sleep(5)

# Quit driver
driver.quit()
