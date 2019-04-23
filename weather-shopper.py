from selenium import webdriver 
import re


driver = webdriver.Chrome()

driver.get('http://weathershopper.pythonanywhere.com/moisturizer')
print (driver.title)

#get the moisturizers list 
moisturisers = driver.find_elements_by_xpath("//div[contains(@class,'text-center col-4')]")

for moisturiser in moisturisers:
    name =  moisturiser.find_element_by_xpath("p[contains(@class,'font-weight-bold top-space-10')]").text   
    price = moisturiser.find_element_by_xpath("p[contains(text(),'Price')]") 
    price = price.split('Price:')[-1].strip()
    price = price.split('Rs.')[-1].strip()
    #price = re.findall(r'\b\d+\b', price)
    price = int(price)
     
    if 'aloe' in name:
        if price < 100000:            
            aloe_min = moisturiser              
    if 'almond' in name:
        if price <  100000:
            almond_min = moisturiser                       

aloe_min.find_element_by_xpath("button[text()='Add']").click()
almond_min.find_element_by_xpath("button[text()='Add']").click()

driver.find_element_by_xpath("//span[@id='cart']").click()

driver.quit()