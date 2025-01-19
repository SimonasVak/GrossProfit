from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from selenium.webdriver.firefox.service import Service
import time

logging.basicConfig(level=logging.INFO)

def fetch_gross_profit(ticker):
    try:
        url = f"https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}"
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-certificate-errors')
        # options.add_argument('--headless')  # Disable headless mode to see the browser window
        service = Service(executable_path='drivers/geckodriver')
        driver = webdriver.Firefox(service=service, options=options)
        driver.get(url)

        logging.info("Navigated to URL")

        # Accept cookies if the cookies acceptance page appears
        try:
            accept_cookies_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept')]"))
            )
            accept_cookies_button.click()
            logging.info("Accepted cookies")
        except Exception as e:
            logging.info("No cookies acceptance button found")

        # Click the "Quarterly" button using the correct XPath
        logging.info("Attempting to click the Quarterly button")
        quarterly_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//main//section[@class='mainContent yf-cfn520']//section[@class='main yf-cfn520']//article[@class='gridLayout yf-cfn520']//article[@class='yf-m6gtul']//div[@class='toolbars yf-m6gtul']//div[@class='subToolbar yf-m6gtul']//div[@class='tabList l1 tw--mb-1 yf-gfq5ju']//button[@id='tab-quarterly']"))
        )
        quarterly_button.click()
        logging.info("Clicked Quarterly button")

        # Add a delay to ensure the page has enough time to load the quarterly data
        time.sleep(5)

        # Extract the quarterly gross profit data using the correct XPath
        logging.info("Attempting to extract quarterly gross profit data")
        quarterly_data_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/section/section/section/article/article/section/div/div/div[2]/div[3]/div[4]"))
        )
        quarterly_data = quarterly_data_element.text
        logging.info(f"Quarterly data: {quarterly_data}")

        driver.quit()
        return quarterly_data
    except Exception as e:
        logging.error(f"Error fetching gross profit: {e}")
        return None
