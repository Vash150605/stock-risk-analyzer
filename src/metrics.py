import numpy as np


def get_log_returns(prices):
    return np.log(prices / prices.shift(1)).dropna()


def risk_summary(prices, returns):
    """Annual return, volatility, Sharpe, max drawdown, VaR 95%."""
    summary = returns.mean().to_frame("Annual return") * 252
    summary["Annual volatility"] = returns.std() * np.sqrt(252)
    summary["Sharpe ratio"] = summary["Annual return"] / summary["Annual volatility"]

    cum_value = prices / prices.iloc[0]
    summary["Max drawdown"] = (cum_value / cum_value.cummax() - 1).min()
    summary["VaR 95% (daily)"] = returns.apply(lambda r: np.percentile(r, 5))
    return summary