def get_urls(stock_exchange, ticker):
    se = stock_exchange.lower()
    if se == "nasdaq":
        base_url = f"https://stockanalysis.com/stocks/{ticker}"
    elif se in ["vse", "rse", "tal"]:
        base_url = f"https://stockanalysis.com/quote/{stock_exchange}/{ticker}"
    else:
        raise ValueError(f"Unsupported stock exchange: {stock_exchange}")
    
    return {
        "INCOME_URL": f"{base_url}/financials/?p=quarterly",
        "RATIOS_URL": f"{base_url}/financials/ratios/?p=quarterly",
        "CF_URL": f"{base_url}/financials/cash-flow-statement/?p=quarterly",
        "BALANCE_URL": f"{base_url}/financials/balance-sheet/?p=quarterly",
        "ANN_INCOME_URL": f"{base_url}/financials/",
        "ANN_CF_URL": f"{base_url}/financials/cash-flow-statement/",
        "ANN_BALANCE_URL": f"{base_url}/financials/balance-sheet/",
        "TTM_INCOME_URL": f"{base_url}/financials/?p=trailing",
        "TTM_CF_URL": f"{base_url}/financials/cash-flow-statement/?p=trailing",
        "TTM_BALANCE_URL": f"{base_url}/financials/balance-sheet/?p=trailing",
        "STATISTICS_URL": f"{base_url}/statistics"
    }