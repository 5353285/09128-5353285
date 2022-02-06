import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from time import sleep

chrome_driver.find_element_by_id("addbutton").click()
time.sleep(5)

output_str = chrome_driver.find_element_by_name("li6").text
sys.stderr.write(output_str)

time.sleep(2)
chrome_driver.close()


def test_lambdatest1_2():
    chrome_driver = webdriver.Chrome()

    chrome_driver.get('https://www.google.com/')
    chrome_driver.maximize_window()

    title = "Google"
    assert title == chrome_driver.title

    search_text = "LambdaTest"
    search_box = chrome_driver.find_element_by_xpath("//input[@name='q']")
    search_box.send_keys(search_text)

    time.sleep(5)

    search_box.send_keys(Keys.ARROW_DOWN)
    search_box.send_keys(Keys.ARROW_UP)
    time.sleep(2)
    search_box.send_keys(Keys.RETURN)

    time.sleep(5