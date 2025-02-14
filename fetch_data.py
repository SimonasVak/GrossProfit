import requests
from bs4 import BeautifulSoup
from url_generator import get_urls

def fetch_stock_data(url, keywords):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from {url}: {response.status_code}")
    
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    if not table:
        return []

    rows = []
    for row in table.find_all("tr"):
        cells = [cell.get_text(strip=True) for cell in row.find_all(["th", "td"])]
        if any(keyword in cells for keyword in keywords):
            rows.append(cells[:18])
    return rows

def fetch_chart_data(url, keywords):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from {url}: {response.status_code}")
    
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    if not table:
        return []

    rows = []
    for row in table.find_all("tr"):
        cells = [cell.get_text(strip=True) for cell in row.find_all(["th", "td"])]
        if any(keyword in cells for keyword in keywords):
            rows.append(cells[:30])
    return rows

def fetch_margin_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from {url}: {response.status_code}")
    
    soup = BeautifulSoup(response.text, "html.parser")
    h2_tag = soup.find("h2", text="Margins")
    if h2_tag:
        table = h2_tag.find_next("table")
        if table:
            rows = []
            for row in table.find_all("tr"):
                cells = [cell.get_text(strip=True) for cell in row.find_all("td")]
                if cells:
                    rows.append(cells)
            return rows
    print("Margins section not found.")
    return []

def fetch_dividend_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from {url}: {response.status_code}")
    
    soup = BeautifulSoup(response.text, "html.parser")
    h2_tag = soup.find("h2", text="Dividends & Yields")
    if h2_tag:
        table = h2_tag.find_next("table")
        if table:
            rows = []
            for row in table.find_all("tr"):
                cells = [cell.get_text(strip=True) for cell in row.find_all("td")]
                if cells:
                    rows.append(cells)
            return rows
    print("Dividends section not found.")
    return []

def fetch_ttm_data(url, filter_columns=None):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from {url}: {response.status_code}")
    
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    if not table:
        print("No table found on the page!")
        return []
    
    rows = []
    for row in table.find_all("tr"):
        cells = [cell.get_text(strip=True) for cell in row.find_all(["th", "td"])]
        if filter_columns and not any(col in cells for col in filter_columns):
            continue
        # Select columns 0, 1, 5, 9, 13, 17 (or empty string if missing)
        selected_cells = [cells[i] if i < len(cells) else "" for i in [0, 1, 5, 9, 13, 17]]
        rows.append(selected_cells)
    
    print("Fetched TTM Data:")
    for r in rows:
        print(r)
    return rows

def fetch_ann_data(url, filter_columns=None):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from {url}: {response.status_code}")
    
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    if not table:
        print("No table found on the page!")
        return []
    
    rows = []
    for row in table.find_all("tr"):
        cells = [cell.get_text(strip=True) for cell in row.find_all(["th", "td"])]
        if filter_columns and not any(col in cells for col in filter_columns):
            continue
        # For annual data we use a different column set: [0, 2, 3, 4, 5, 6]
        selected_cells = [cells[i] if i < len(cells) else "" for i in [0, 1, 2, 3, 4, 5, 6]]
        rows.append(selected_cells)
    
    print("Fetched Annual Data:")
    for r in rows:
        print(r)
    return rows

def fetch_eps_data(url, filter_columns=None):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from {url}: {response.status_code}")
    
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    if not table:
        print("No table found on the page!")
        return []
    
    rows = []
    for row in table.find_all("tr"):
        cells = [cell.get_text(strip=True) for cell in row.find_all(["th", "td"])]
        if filter_columns and not any(col in cells for col in filter_columns):
            continue
        # For annual data we use a different column set: [0, 2, 3, 4, 5, 6]
        selected_cells = [cells[i] if i < len(cells) else "" for i in [0, 2]]
        rows.append(selected_cells)
    
    print("Fetched Annual Data:")
    for r in rows:
        print(r)
    return rows

# Other fetch functions remain the same as in your original code...
# (fetch_margin_data, fetch_dividend_data, fetch_ttm_data, fetch_ann_data, fetch_eps_data)

def fetch_all_data(ticker, stock_exchange):
    urls = get_urls(stock_exchange, ticker)
    
    try:
        data = {
            'quarterly_income_data': fetch_stock_data(urls["INCOME_URL"], [
                "Revenue", "Net Income", "Gross Profit", "Operating Income", "Revenue Growth (YoY)",
                "Net Income Growth", "Shares Outstanding (Basic)", "EBITDA", "Fiscal Quarter",
                "Basic Shares Outstanding", "EPS (Basic)"
            ]),
            'quarterly_balance_data': fetch_stock_data(urls["BALANCE_URL"], [
                "Total Assets", "Total Liabilities", "Fiscal Quarter", "Shareholders' Equity",
                "Total Current Liabilities"
            ]),
            'quarterly_cashflow_data': fetch_stock_data(urls["CF_URL"], [
                "Net Income", "Operating Cash Flow", "Capital Expenditures", "Investing Cash Flow",
                "Financing Cash Flow", "Free Cash Flow", "Fiscal Quarter"
            ]),
            'ttm_income_data': fetch_ttm_data(urls["TTM_INCOME_URL"], [
                "Revenue", "Net Income", "Gross Profit", "Operating Income", "Revenue Growth (YoY)",
                "Net Income Growth", "Shares Outstanding (Basic)", "EBITDA", "Fiscal Quarter",
                "Basic Shares Outstanding", "EPS (Basic)"
            ]),
            'ttm_balance_data': fetch_ttm_data(urls["TTM_BALANCE_URL"], [
                "Total Assets", "Total Liabilities", "Fiscal Quarter", "Shareholders' Equity",
                "Total Current Liabilities"
            ]),
            'ttm_cashflow_data': fetch_ttm_data(urls["TTM_CF_URL"], [
                "Net Income", "Operating Cash Flow", "Capital Expenditures", "Investing Cash Flow",
                "Financing Cash Flow", "Free Cash Flow", "Fiscal Quarter"
            ]),
            'quarterly_ratios_data': fetch_stock_data(urls["RATIOS_URL"], [
                "PE Ratio", "Forward PE", "PS Ratio", "PB Ratio", "P/FCF Ratio", "EV/EBITDA",
                "DEBT / Equity Ratio", "Debt / FCF Ratio", "Quick Ratio", "Current Ratio",
                "Return on Equity (ROE)", "Return on Assets (ROA)", "Return on Capital (ROIC)",
                "Fiscal Quarter"
            ]),
            'annual_income_data': fetch_ann_data(urls["ANN_INCOME_URL"], [
                "Revenue", "Net Income", "Gross Profit", "Operating Income", "Revenue Growth (YoY)",
                "Net Income Growth", "Shares Outstanding (Basic)", "EBITDA", "Fiscal Year",
                "Basic Shares Outstanding", "EPS (Basic)"
            ]),
            'annual_balance_data': fetch_ann_data(urls["ANN_BALANCE_URL"], [
                "Total Assets", "Total Liabilities", "Fiscal Year", "Shareholders' Equity",
                "Total Current Liabilities", "Total Debt", "Long-Term Leases", "Total Current Liabilities"
            ]),
            'annual_cashflow_data': fetch_ann_data(urls["ANN_CF_URL"], [
                "Net Income", "Operating Cash Flow", "Capital Expenditures", "Investing Cash Flow",
                "Financing Cash Flow", "Free Cash Flow", "Fiscal Year"
            ]),
            'margins_data': fetch_margin_data(urls["STATISTICS_URL"]),
            'dividend_data': fetch_dividend_data(urls["STATISTICS_URL"]),
            'revenue_data': fetch_chart_data(urls["INCOME_URL"], ["Revenue"]),
            'eps_data': fetch_eps_data(urls["ANN_INCOME_URL"], ["EPS (Basic)"]),
            'income_data': fetch_chart_data(urls["INCOME_URL"], ["Net Income"]),
            'gross_profit_data': fetch_chart_data(urls["INCOME_URL"], ["Gross Profit"]),
            'operating_income_data': fetch_chart_data(urls["INCOME_URL"], ["Operating Income"]),
            'capex_data': fetch_chart_data(urls["CF_URL"], ["Capital Expenditures"]),
            'fcf_data': fetch_chart_data(urls["CF_URL"], ["Free Cash Flow"]),
            'operatingcf_data': fetch_chart_data(urls["CF_URL"], ["Operating Cash Flow"]),
            'quick_ratio_data': fetch_chart_data(urls["RATIOS_URL"], ["Quick Ratio"]),
            'pe_ratio_data': fetch_chart_data(urls["RATIOS_URL"], ["PE Ratio"]),
            'current_ratio_data': fetch_chart_data(urls["RATIOS_URL"], ["Current Ratio"]),
            'debtequity_ratio_data': fetch_chart_data(urls["RATIOS_URL"], ["Debt / Equity Ratio"]),
            'debtfcf_ratio_data': fetch_chart_data(urls["RATIOS_URL"], ["Debt / FCF Ratio"]),
            'assets_data': fetch_chart_data(urls["BALANCE_URL"], ["Total Assets", "Total Liabilities", "Shareholders' Equity"]),
            'ltl_data': fetch_chart_data(urls["BALANCE_URL"], ["Long-Term Leases", "Total Current Liabilities", "Total Debt", "Fiscal Quarter"]),

            # Add all other data fetching calls here similar to your original main() function
            # Each piece of data should be added to this dictionary
        }
        
        return data
        
    except Exception as e:
        raise Exception(f"Error fetching stock data: {str(e)}")