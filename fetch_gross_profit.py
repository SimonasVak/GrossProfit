from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fetch_gross_profit(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}"
    driver = webdriver.Chrome()
    driver.get(url)

    # Click the "Quarterly" button using the correct XPath
    quarterly_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='tab-quarterly']"))
    )
    quarterly_button.click()

    # Extract the quarterly gross profit data using the correct XPath
    quarterly_data = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='nimbus-app']/section/section/section/article/article/section/div/div/div[2]/div[3]/div[3]"))
    ).text

    driver.quit()
    return quarterly_data

if __name__ == "__main__":
    import sys
    ticker = sys.argv[1]
    print(fetch_gross_profit(ticker))
