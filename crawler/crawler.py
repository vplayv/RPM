from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import datetime
import csv
import re
import requests
import time
import pathlib
import os
from multiprocessing import Pool, Manager, Lock
import multiprocessing
from functools import partial
from itertools import repeat
import validators

def my_mkdir():
    filepath = "./" + datetime.datetime.now().strftime("%y%m%d")
    pathlib.Path(filepath).mkdir(parents=True, exist_ok=True)
    with open('./resources/current_date.txt', 'w') as f:
        f.write('{}'.format(datetime.datetime.now().strftime("%y%m%d")))
    f.close()

def driver_wait(browser, time, by, name):
    WebDriverWait(browser, time).until(
        EC.presence_of_element_located((by, name))
    )

def get_current_date():
    current_date = ''
    with open('./resources/current_date.txt', 'r') as f:
        current_date = f.read(6)
    f.close()

    # print(current_date)
    return current_date

def get_amazon_link():
    urls = []
    with open('./resources/amazon_link.txt', 'r') as f:
        urls = f.readlines()
    urls = [url.rstrip('\n') for url in urls]
    f.close()
    return urls

def get_browser_options():
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_setting_values': {'cookies': 1,
                                                        'images': 2,
                                                        'javascript': 1,
                                                        'plugins': 2,
                                                        'popups': 2,
                                                        'geolocation': 2,
                                                        'notifications': 2,
                                                        'auto_select_certificate': 2,
                                                        'fullscreen': 1,
                                                        'mouselock': 2,
                                                        'mixed_script': 2,
                                                        'media_stream': 2,
                                                        'media_stream_mic': 2,
                                                        'media_stream_camera': 2,
                                                        'protocol_handlers': 2,
                                                        'ppapi_broker': 2,
                                                        'automatic_downloads': 2,
                                                        'midi_sysex': 2,
                                                        'push_messaging': 2,
                                                        'ssl_cert_decisions': 2,
                                                        'metro_switch_to_desktop': 2,
                                                        'protected_media_identifier': 2,
                                                        'app_banner': 2,
                                                        'site_engagement': 2,
                                                        'durable_storage': 2}}
    options.add_experimental_option("detach", True)
    options.add_experimental_option('prefs', prefs)
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")

    driver_path = './resources/chromedriver'  # driver path
    browser = webdriver.Chrome(chrome_options=options, executable_path=driver_path)  # Chrome driver
    url_header = "https://www.amazon.in"
    return browser, url_header