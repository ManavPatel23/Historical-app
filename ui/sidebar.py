import streamlit as st
from datetime import date, timedelta

def sidebar_controls():
    st.sidebar.header("📈🈲 Stock Data Options 🈯️📉")

    popular_stocks = {
        "Reliance Industries": "RELIANCE.NS",
        "HDFC Bank": "HDFCBANK.NS",
        "Tata Consultancy Services": "TCS.NS",
        "State Bank of India": "SBIN.NS",
        "Adani Power Limited": "ADANIPOWER.NS",
        "Tata Steel Limited": "TATASTEEL.NS",
        "BSE Limited": "BSE.NS",
        "PVR Inox Limited": "PVRINOX.NS",
        "Larsen & Toubro": "LT.NS",
        "ICICI Bank": "ICICIBANK.NS",
        "Kotak Mahindra Bank Limited": "KOTAKBANK.NS"
    }

    selection_method = st.sidebar.radio(
        "Select Stock Method:",
        ["Choose from Popular Stocks", "Enter Custom Symbol"]
    )

    if selection_method == "Choose from Popular Stocks":
        stock_name = st.sidebar.selectbox("Select Stock:", list(popular_stocks.keys()))
        stock = popular_stocks[stock_name]
        st.sidebar.info(f"Selected: {stock}")
    else:
        stock = st.sidebar.text_input(
            "Enter Stock Symbol",
            value="RELIANCE.NS",
            help="Use .NS for NSE, .BO for BSE"
        )

    period_options = {
        "Custom": None,
        "1 Day": 1,
        "3 Days": 2,
        "1 Week": 7,
        "2 Weeks": 14,
        "1 Months": 30,
        "3 Months": 90,
        "6 Months": 180,
        "1 Year": 365,
        "2 Years": 730
    }

    selected_period = st.sidebar.selectbox("Time Period:", list(period_options.keys()), index=1)
    if selected_period == "Custom":
        end_date = date.today()
        start_date = st.sidebar.date_input("Start Date", value=end_date - timedelta(days=90))
        end_date = st.sidebar.date_input("End Date", value=end_date)
    else:
        end_date = date.today()
        start_date = end_date - timedelta(days=period_options[selected_period])

    interval_category = st.sidebar.selectbox("Category:", ["Intraday", "Daily/Weekly", "Monthly"], index=1)
    interval_map = {
        "Intraday": [("1m", "1 minute"), ("5m", "5 minutes"), ("15m", "15 minutes"), ("30m", "30 minutes"), ("1h", "1 hour")],
        "Daily/Weekly": [("1d", "1 day"), ("5d", "5 days"), ("1wk", "1 week")],
        "Monthly": [("1mo", "1 month"), ("3mo", "3 months")]
    }
    intervals = interval_map[interval_category]
    interval = st.sidebar.selectbox("Interval", [i[0] for i in intervals], format_func=lambda x: dict(intervals)[x])

    chart_type = st.sidebar.selectbox("Chart Type", ["Candlestick", "Line Chart", "OHLC"])

    show_ma = st.sidebar.checkbox("Moving Averages", value=True)
    ma_periods = st.sidebar.multiselect("MA Periods", [5, 10, 20, 50, 100, 200], default=[20, 50]) if show_ma else []

    show_volume = st.sidebar.checkbox("Volume", value=True)

    auto_refresh = st.sidebar.checkbox("Auto-refresh")
    if auto_refresh:
        import time
        time.sleep(10)  # every 10 seconds
        fetch_data = True
    else:
        fetch_data = st.sidebar.button("📊 Fetch Data", type="primary")

    return {
        "stock": stock,
        "start_date": start_date,
        "end_date": end_date,
        "interval": interval,
        "chart_type": chart_type,
        "show_ma": show_ma,
        "ma_periods": ma_periods,
        "show_volume": show_volume,
        "fetch_data": fetch_data
    }



