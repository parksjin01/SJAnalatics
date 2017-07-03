#-*- encoding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium import webdriver
import time

def table_to_array(node, no_header=0):
    table = []
    table_contents = node.find_elements_by_tag_name('tr')
    if no_header:
        table_contents = table_contents[:-1]
    for line in table_contents:
        tmp = []
        for value in line.find_elements_by_tag_name('td'):
            tmp.append(value.text)
        table.append(tmp)
    return table


def webdriver_select_class(driver, option_class, value):
    el = driver.find_element_by_class_name(option_class)
    for option in el.find_elements_by_tag_name('option'):
        if option.text == value:
            option.click()  # select() in earlier versions of webdriver
            break

def webdriver_select_id(driver, option_id, value):
    el = driver.find_element_by_id(option_id)
    for option in el.find_elements_by_tag_name('option'):
        if option.text == value:
            option.click()  # select() in earlier versions of webdriver
            break

def webdriver_input_id(driver, input_id, value):
    el = driver.find_element_by_id(input_id)
    el.clear()
    el.send_keys(value)

def Recommandation(num):
    Chrome_Driver = "/Users/Knight/Desktop/2017 오픈소스 대회/chromedriver"
    driver = webdriver.Chrome(executable_path=Chrome_Driver)
    try:
        driver.get("https://www.google.com/finance?ei=fctZWZjQNpGI0gTkxr-YBw#stockscreener")
        webdriver_select_class(driver, 'id-regionselect', 'Korea')
        webdriver_select_id(driver, 'exchangeselect', 'Korea Exchange (KRX)')
        time.sleep(3)
        webdriver_input_id(driver, 'Price52WeekPercChange_left', '0.5')
        driver.get_screenshot_as_png()
        page = driver.find_element_by_class_name('id-searchresults')
        result = table_to_array(page)
    finally:
        driver.close()
    return result[:-1]