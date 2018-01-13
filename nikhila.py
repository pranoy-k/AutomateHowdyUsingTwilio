from selenium import webdriver
import time
import auth
from time import sleep
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC8d1cc3f74f25a80deab06b057553d097"
auth_token = "1ae8e9dd7feb0c5ce9ebf683fc8f330a"
client = Client(account_sid, auth_token)

browser = webdriver.Firefox()

count = 0
while(True):
    try:
        browser.get('https://cas.tamu.edu/cas/login?service=https://howdy.tamu.edu/uPortal/Login&renew=true')

        user=browser.find_element_by_css_selector('#username')
        user.send_keys(auth.username)
        password=browser.find_element_by_css_selector('#password')
        password.send_keys(auth.password)

        login=browser.find_element_by_class_name('thinking-anim')
        login.click()

        rec = browser.find_element_by_css_selector("#tabLink_u42l1s10 > span:nth-child(1)")
        # rec=browser.find_element_by_xpath("//*[@id='tabLink_u42l1s10']")
        rec.click()  
        class_link = browser.find_element_by_partial_link_text('Search Class')
        class_link.click()
        browser.switch_to_frame(browser.find_element_by_tag_name("iframe"))
        
        browser.find_element_by_css_selector(".pagebodydiv > form:nth-child(1) > input:nth-child(5)").click()

        browser.find_element_by_css_selector("#subj_id > option:nth-child(54)").click()
        
        browser.find_element_by_css_selector("#courseBtnDiv > input:nth-child(2)").click()
        
        browser.find_element_by_css_selector(".datadisplaytable > tbody:nth-child(1) > tr:nth-child(69) > td:nth-child(4) > form:nth-child(1) > input:nth-child(30)").click()
        
        value = browser.find_element_by_css_selector(".datadisplaytable > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(13)")
        if(int(value.text) > 0):
            message = client.api.account.messages.create(to="+19793243647", \
                                             from_="+19799852518",  \
                                             body="Hello Nikhila 601 course")
        value = browser.find_element_by_css_selector(".datadisplaytable > tbody:nth-child(2) > tr:nth-child(7) > td:nth-child(13)")
        if(int(value.text) > 0):
            message = client.api.account.messages.create(to="+19793243647", \
                                             from_="+19799852518",  \
                                             body="Hello Nikhila 601 course")
        value = browser.find_element_by_css_selector(".datadisplaytable > tbody:nth-child(2) > tr:nth-child(9) > td:nth-child(13)")
        if(int(value.text) > 0):
            message = client.api.account.messages.create(to="+19793243647", \
                                             from_="+19799852518",  \
                                             body="Hello Nikhila 601 course")

        sleep(10)
        value = None
        print(count)
        count+=1
    except:
        print("Exception Pranoy")
        pass