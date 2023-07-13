from SeleniumDriver import SeleniumDriver
from EPADataBrowser import EPADataBrowser

def main():
    """"
    # ask user for data_for_year if blank then use 2008
    # ask user for pollutant if blank then use PM2.5
    # ask user for state if blank then use North Carolina
    # ask user for site if blank then use All Sites
    """
    data_for_year = input("Enter the year for which you want to download the data: ")
    pollutant = input("Enter the pollutant for which you want to download the data: ")
    state = input("Enter the state for which you want to download the data: ")
    site = input("Enter the site for which you want to download the data: ")

    if (data_for_year == ""):
        data_for_year = 2008
    if (pollutant == ""):
        pollutant = "PM2.5"
    if (state == ""):
        state = "North Carolina"
    if (site == ""):
        site = "All Sites"

    epa_url = "https://www.epa.gov/outdoor-air-quality-data/download-daily-data"
    epa_driver = SeleniumDriver(url=epa_url, endless_scroll=False)
    epa_driver.get()

    epa_data_scraper = EPADataBrowser(epa_driver.driver)
    download_sucess = epa_data_scraper.complete_form_and_submit(data_for_year, pollutant, state, site)
    if (download_sucess):
        epa_driver.close()

if __name__ == "__main__":
    main()


    

