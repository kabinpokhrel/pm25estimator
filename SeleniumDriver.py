# File: SeleniumDriver.py
import time, os 
from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
from requests_html import HTML

def get_driver_binary_path_macbook():
    filePath = os.path.join(os.path.dirname(__file__), 'chromedriver_mac64/chromedriver')
    return filePath

def get_user_agent():
    return UserAgent(verify_ssl=False).random
@dataclass
class SeleniumDriver:
    url: str
    endless_scroll: bool = False
    endless_scroll_time: int = 5
    driver: WebDriver = None
    html_obj : HTML = None

    def get_driver(self):
        if self.driver is None:
            user_agent = get_user_agent()
            options = webdriver.ChromeOptions()
            #options.add_argument("--no-sandbox")
            #options.add_argument("--headless")
            #options.add_argument(f"user-agent={user_agent}")    
            serviceObj = Service(get_driver_binary_path_macbook())
            self.driver = webdriver.Chrome(options=options, service=serviceObj)
        return self.driver

    def get(self):
        driver = self.get_driver()
        time.sleep(2)
        driver.get(self.url)
        self.perform_endless_scroll(driver=driver)
        # return driver.page_source
    
    def close(self):
        if self.driver is not None:
            self.driver.close()
    
    def perform_endless_scroll(self, driver=None):
        if driver is None:
            return
        if self.endless_scroll:
            #driver.execute_script
            current_height = driver.execute_script("return document.body.scrollHeight")
            while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(self.endless_scroll_time)
                iter_height = driver.execute_script("return document.body.scrollHeight")
                if current_height == iter_height:
                    break
                current_height = iter_height


    def wait_until_page_is_loaded(self, driver=None):
        """ This method will wait until the page is loaded. """
        if driver is None:
            return False
        page_state = driver.execute_script('return document.readyState;')
        return page_state == 'complete'

    



        