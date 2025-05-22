#fetch stock data
import os
import yfinance as yf
import pandas as pd

# Get absolute path for 'data' folder inside project
DATA_DIR = os.path.join(os.path.dirname(__file__), "..data")

# Ensure the directory exists
os.makedirs(DATA_DIR, exist_ok=True)

def fetch_stock_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)
    return data

if __name__ == "__main__":
    df = fetch_stock_data("AAPL", "2023-01-01", "2025-05-21")
    df.to_csv(os.path.join(DATA_DIR, "apple_stock.csv"))
