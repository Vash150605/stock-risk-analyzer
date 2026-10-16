import numpy as np
import pandas as pd


class Portfolio:
    def __init__(self, returns):
        self.returns = returns
        self.mu = returns.mean() * 252
        self.cov = returns.cov() * 252
        self.n = returns.shape[1]

    def performance(self, w):
        """Return, volatility and Sharpe for a weights vector."""
        ret = w @ self.mu
        vol = np.sqrt(w @ self.cov @ w)
        return ret, vol, ret / vol

    def simulate(self, n_portfolios=10000, seed=42):
        """Try random weights and return a table of results."""
        np.random.seed(seed)
        rows = []
        for _ in range(n_portfolios):
            w = np.random.random(self.n)
            w = w / w.sum()
            rows.append(list(self.performance(w)) + list(w))
        columns = ["Return", "Volatility", "Sharpe"] + list(self.returns.columns)
        return pd.DataFrame(rows, columns=columns)