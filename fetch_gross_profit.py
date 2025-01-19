from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fetch_gross_profit(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}"
    driver = webdriver.Chrome()
    driver.get(url)

    # Click the "Quarterly" button
    quarterly_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Quarterly']"))
    )
    quarterly_button.click()

    # Extract the quarterly data
    quarterly_data = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='column yf-t22klz alt']"))
    ).text

    driver.quit()
    return quarterly_data

if __name__ == "__main__":
    import sys
    ticker = sys.argv[1]
    print(fetch_gross_profit(ticker))
