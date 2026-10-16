from src.data_loader import download_prices, clean_prices
from src.metrics import get_log_returns, risk_summary
from src.portfolio import Portfolio

# 1. Data
prices = clean_prices(download_prices())
returns = get_log_returns(prices)
returns.to_csv("data/processed/log_returns.csv")

# 2. Risk summary
summary = risk_summary(prices, returns)
summary.to_csv("data/processed/risk_summary.csv")
print(summary.round(4))

# 3. Portfolio simulation (stocks only, no index)
stocks = returns.drop(columns="^NSEI")
pf = Portfolio(stocks)
sim = pf.simulate()
sim.to_csv("data/processed/portfolio_simulation.csv", index=False)

best = sim.loc[sim["Sharpe"].idxmax()]
print("\nBest Sharpe portfolio:")
print(best.round(4))