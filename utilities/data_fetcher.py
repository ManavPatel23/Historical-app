import yfinance as yf
import pandas as pd
import time
from .technical import calculate_indicators, clean_dataframe

def fetch_stock_data(stock, start_date, end_date, interval, ma_periods, retries=3):
    for attempt in range(retries):
        try:
            df = yf.download(stock, start=start_date, end=end_date, interval=interval, progress=False)

            if df is not None and not df.empty:
                df = clean_dataframe(df)
                df = calculate_indicators(df, ma_periods)

                try:
                    info = yf.Ticker(stock).info
                except Exception as info_error:
                    print(f"[INFO WARNING] Could not fetch stock info for {stock}: {info_error}")
                    info = {"longName": stock}

                return df, info, None

            else:
                return None, None, f"No data found for {stock}"

        except Exception as e:
            error_message = str(e).lower()
            if "rate limit" in error_message or "too many requests" in error_message:
                wait_time = (attempt + 1) * 5
                print(f"[Retry {attempt+1}] Rate limit hit. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                return None, None, f"Error fetching data: {str(e)}"

    return None, None, "❌ Failed after multiple retries due to rate limiting or errors."
