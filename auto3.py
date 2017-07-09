#!/bin/bash -ex
from selenium import webdriver
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

driver.get('http://google.com')


#Open the browser
#import webbrowser
#new = 2;
#webbrowser.open(url,new=new);

