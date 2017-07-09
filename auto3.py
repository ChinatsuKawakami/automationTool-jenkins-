#!/bin/bash -ex
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#import lxml.html


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

click_jenkins = input_box.get
jenkins_url = 'https://jenkins.io/'
input_box.find_element_by_link_text("Jenkins").send_keys('\n')






# take the screen shot
#input_box.save_screenshot('@C:\Program Files (x86)\Jenkins\01_screenshot.png')

#if __name__ == '__main__':
 #   main()

#Open the browser
#import webbrowser
#new = 2;
#webbrowser.open(url,new=new);

