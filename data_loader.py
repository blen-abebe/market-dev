#fetch stock data
import yfinance as yf
data = yf.download("AAPL", start="2023-01-01", end="2025-05-20")
print(data.head())  # View first few rows