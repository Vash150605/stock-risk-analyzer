import pandas as pd
import yfinance as yf

TICKERS = ["TCS.NS", "HDFCBANK.NS", "RELIANCE.NS", "ITC.NS", "SUNPHARMA.NS", "^NSEI"]


def download_prices(start="2020-01-01", end="2025-01-01"):
    """Download closing prices and save the raw file."""
    prices = yf.download(TICKERS, start=start, end=end)["Close"]
    prices.to_csv("data/raw/prices_raw.csv")
    return prices


def clean_prices(prices):
    """Sort by date, fill small gaps, save the clean file."""
    prices = prices.sort_index().ffill()
    prices.to_csv("data/processed/prices_clean.csv")
    return prices