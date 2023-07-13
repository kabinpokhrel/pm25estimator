import time
from dataclasses import dataclass
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

@dataclass
class EPADataBrowser:
    driver: WebDriver = None
    download_success: bool = False
    def __init__(self, driver):
        self.driver = driver
        self.download_success = False

    def wait_until_page_is_loaded(self):
        """ This method will wait until the page is loaded. """
        if self.driver is None:
            return False
        else:
            time.sleep(2)
            return True
        
    def complete_form_and_submit(self, data_for_year=2008, pollutant="PM2.5", state="North Carolina", site="All Sites"):
        # Select the pollutant
        pollutant_select = self.driver.find_element(By.ID, "poll")
        pollutant_select.click()
        time.sleep(3)
        pollutant_option = self.driver.find_element(By.XPATH, f"//option[text()='{pollutant}']")
        pollutant_option.click()
        #wait for ajax response
        time.sleep(2)
        # Select the year
        year_select = self.driver.find_element(By.ID,"year")
        year_select.click()
        time.sleep(2)
        year_option = self.driver.find_element(By.XPATH,f"//option[text()='{data_for_year}']")
        year_option.click()
        #wait for ajax response
        time.sleep(2)
        # Select the state
        state_select = self.driver.find_element(By.ID,"state")
        state_select.click()
        state_option = self.driver.find_element(By.XPATH,f"//option[text()='{state}']")
        state_option.click()
        #wait for ajax response
        time.sleep(2)
        # Select the site
        site_select = self.driver.find_element(By.ID,"site")
        site_select.click()
        site_option = self.driver.find_element(By.XPATH,f"//option[text()='{site}']")
        site_option.click()
        #wait for ajax response
        time.sleep(2)
        # Click the submit button
        submit_button = self.driver.find_element(By.XPATH,"//input[@value='Get Data']")
        submit_button.click()
        #wait for ajax response
        time.sleep(5)

        # wait until the results div is visible
        results_div = self.driver.find_element(By.ID,"results")
        while results_div.is_displayed() is False:
            time.sleep(1)
        #wait for ajax response
        time.sleep(2)

        # Get the download link
        download_link = self.driver.find_element(By.XPATH,"//a[text()='Download CSV (spreadsheet)']")
        self.download_link = download_link.get_attribute("href")
        download_link.click()
        #wait for ajax response
        time.sleep(2)
        self.download_success = True
        return self.download_success

    