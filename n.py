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

while(True):
	try:
		browser.get('https://cas.tamu.edu/cas/login?service=https://howdy.tamu.edu/uPortal/Login&renew=true')

		user=browser.find_element_by_css_selector('#username')
		user.send_keys(auth.username)
		password=browser.find_element_by_css_selector('#password')
		password.send_keys(auth.password)

		login=browser.find_element_by_class_name('thinking-anim')
		login.click()

		rec=browser.find_element_by_xpath("//*[@id='tabLink_u42l1s10']")
		rec.click()  
		class_link = browser.find_element_by_partial_link_text('Search Class')
		class_link.click()
		browser.switch_to_frame(browser.find_element_by_tag_name("iframe"))
		sub=browser.find_element_by_xpath("/html/body/div[3]/form/input[2]")
		sub.click()

		cs=browser.find_element_by_xpath("//*[@id='subj_id']/option[45]")
		cs.click()

		search=browser.find_element_by_xpath("//*[@id='courseBtnDiv']/input[2]")
		search.click()

		aa=browser.find_element_by_xpath("/html/body/div[3]/table[1]/tbody/tr[40]/td[4]/form/input[30]")
		aa.click()

		value = browser.find_element_by_xpath("/html/body/div[3]/form/table/tbody/tr[4]/td[13]")
		
		
		if(int(value.text) >= 0):
			message = client.api.account.messages.create(to="+19793243647", \
                                             from_="+19799852518",  \
                                             body="Hello AI course vachesindi bhayya")
			sleep(30)
		
	except:
		pass
