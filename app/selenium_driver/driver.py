from app.selenium_driver.locators import *
from app.gmail_api import gmail

import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
import re

# run selenium packages
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc

class Base(object):
    """ Initialize a selenium object """

    def __init__(self, driver):
        self.driver = driver
        self.in_process = False
    

    def sleep(self, seconds):
        time.sleep(seconds)

class MexcDriver(Base):
    """ mexc driver runs on mexc.com"""

    """ close pop-up adds if having """
    def close_adds(self):
        try:
            add_locator = LoginLocator.adds
            b,c = add_locator
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((b,c)))
            add_closed = 0
            while self.driver.find_element(*LoginLocator.adds) != []:
                self.driver.find_element(*LoginLocator.adds).click()
                time.sleep(0.5)
                add_closed += 1
                print(f"Closed {add_closed} adds")
        except (NoSuchElementException,ElementNotInteractableException) as e:
            print(f"Error in: close_adds \nDescription: {e}")
            return f"Error in: close_adds \nDescription: {e}"
        
    """ processing the login step """
    def login(self, email, password):

        time.sleep(1)
        self.driver.find_element(*LoginLocator.email_input_box).send_keys(email)
        time.sleep(1)
        self.driver.find_element(*LoginLocator.next_btn).click()

        # A puzzle authentication step will occur, solve it manually to pass this step

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((LoginLocator.password[0],LoginLocator.password[1]))).send_keys(password)

        self.driver.find_element(*LoginLocator.login).click()


    
    def fill_code_boxs(self, code):
        code_boxs = self.driver.find_element(*LoginLocator.code_boxs).find_elements(By.TAG_NAME, "input")
        for i in range(len(code_boxs)):
            code_boxs[i].send_keys(code[i])
        print("fill_code-boxs function: executed successfully.")
        return None
    
    def close_ainti_phising(self):
        try:
            self.driver.find_element(*LoginLocator.anti_phising_warning).click()
            time.sleep(6)
            self.driver.find_element(*LoginLocator.warning_btn).click()
            time.sleep(3)
            self.driver.find_element(*LoginLocator.next_warning_btn).click()
            time.sleep(1)
            self.driver.find_element(*LoginLocator.right_warning).click()
        except NoSuchElementException as e:
            return None
        

    def open_future(self):
        # self.close_adds()
        self.driver.find_element(*FutureLocator.future_btn).click()

    def set_leverage(self, amount):
        if amount > 200:
            amount = 200
        while int(self.driver.find_element(*FutureLocator.current_leverage).text[0:-1]) != amount:
            self.driver.find_element(*FutureLocator.open_levarage_btn).click()
            self.driver.find_element(*FutureLocator.leverage_input).clear()
            self.driver.find_element(*FutureLocator.leverage_input).send_keys(str(amount))
            time.sleep(1)
            self.driver.find_element(*FutureLocator.confirm_levarage_btn).click()
            time.sleep(1)

    def get_available_amount(self) -> float:
        amount = self.driver.find_element(*FutureLocator.available_amount).text
        amount = re.findall(r'\d+\b', amount)
        amount = float(".".join(amount))

        print( "------------------------------\n"
            f"Available amount: {amount} USDT\n"
            "------------------------------\n"
            )
        return amount
    


def run_driver():
    basedir_drivers = os.path.dirname(os.path.abspath("Drivers_120\chromedriver.exe"))
    DRIVER_PATH = os.path.join(basedir_drivers,'chromedriver.exe')

    basedir_chrome = os.path.dirname(os.path.abspath("Chrome_120\chrome.exe"))
    CHROME_PATH = os.path.join(basedir_chrome,'chrome.exe')

    options = webdriver.ChromeOptions()
    service = Service(DRIVER_PATH)
    options.binary_location = (CHROME_PATH)
    

    # # main driver execution
    driver = uc.Chrome(version_main=120, service=service, options=options)
    main = MexcDriver(driver=driver)
    main.driver.get("https://www.mexc.com/login?previous=https%3A%2F%2Ffutures.mexc.com%2Fexchange%2FBTC_USDT")
    # main.driver.get("https://futures.mexc.co/exchange/BTC_USDT")
    main.driver.maximize_window()
    # main.close_adds()

    email = 'your mexc email'
    password = 'your mexc password'
    main.login(email, password)

    
    time.sleep(10)
    code = gmail.get_email_code()
    # time.sleep(1000)
    main.fill_code_boxs(code)

    time.sleep(5)
    main.close_ainti_phising()

    # main.close_adds()
    time.sleep(25)
    main.get_available_amount()
    
    main.start_trading_future()



