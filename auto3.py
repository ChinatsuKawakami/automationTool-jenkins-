#!/bin/bash -ex
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import lxml.html


#def main():
driver=webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

# Set the size of window
driver.maximize_window()

# Access Google Chrome
driver.get('http://google.com')

# take the Screen shot
#driver.save_screenshot('')

# Show the title
print('title of the page : '+driver.title)

# Get the HTML source
#root = lxml.html.fromstring(driver.page_source)

# get the link
#print('-------------------------------------------')
#show_text = root.cssselect('#topicsfb > div.topicsindex > ul.emphasis > li:nth-child(1) > a')[0].text_content())
#print(show_text)

# enter "key word" in textbox to search it
input_box = driver.find_element_by_id('lst-ib')
input_box.send_keys('jenkins')
# push enter key
input_box.send_keys(Keys.ENTER)

# click one of the result


#jenkins_url='/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=1&amp;cad=rja&amp;uact=8&amp;ved=0ahUKEwjFktvwu_3UAhWr5oMKHRoSAIAQFggiMAA&amp;url=https%3A%2F%2Fjenkins.io%2F&amp;usg=AFQjCNHwOJU-lmtmG89TB7bVdt1VJu8R8A'
#input_box.find_element(By.LINK_TEXT('Images')).click()
#elements = driver.find_element_by_tag_name('h3')
#for element in elements:
#    if element.text == "Jenkins":
 #       element.click()
#jenk = input_box.find_element_by_class_name('r')
#element =input_box.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[2]/a')
element =input_box.find_element_by_class_name('hdtb-mitem hdtb-msel hdtb-imb')
element.click()
# wait 5 sec
time.sleep(5)
#take the screen shot
input_box.save_screenshot('@C:/Users/chinatsu/PycharmProjects/automation/02_screenshot.png')

driver.close()



#if __name__ == '__main__':
 #   main()

#Open the browser
#import webbrowser
#new = 2;
#webbrowser.open(url,new=new);

