import logging
from datetime import datetime

import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA


def main():

    # Step 1: Data Collection
    ticker = "AAPL"
    data = yf.download(ticker, start="2021-01-01", end=datetime.now())

    # Step 2: Data Preprocessing
    data = data["Close"].dropna()

    # Step 3: Model Selection
    p = 5  # lag order
    d = 1  # degree of differencing
    q = 0  # order of moving average

    # Step 4: Model Training
    model = ARIMA(data, order=(p, d, q))
    model_fit = model.fit()

    # Step 5: Forecasting
    forecast = model_fit.forecast(steps=7)

    # Log scores
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info(f"Scores: {forecast}")


if __name__ == "__main__":
    main()
