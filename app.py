import streamlit as st
from ui.sidebar import sidebar_controls
from utilities.data_fetcher import fetch_stock_data
from ui.layout import display_dashboard
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Page Setup
st.set_page_config(
    page_title="Stock Visualization Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown('<h1 class="main-header">📈 Stock Visualization Dashboard</h1>', unsafe_allow_html=True)

# Sidebar input
user_config = sidebar_controls()

if user_config['fetch_data']:
    with st.spinner('Fetching data...'):
        df, info, error_msg = fetch_stock_data(
            stock=user_config['stock'],
            start_date=user_config['start_date'],
            end_date=user_config['end_date'],
            interval=user_config['interval'],
            ma_periods=user_config['ma_periods'] if user_config['show_ma'] else [],
        )

        if error_msg:
            st.error(f"❌ {error_msg}")
        elif df is None or df.empty:
            st.error("❌ No data found for the given parameters.")
        else:
            display_dashboard(
                df = df,
                info = info,
                stock = user_config['stock'],
                start_date = user_config['start_date'],
                end_date = user_config['end_date'],
                chart_type = user_config['chart_type'],
                show_ma = user_config['show_ma'],
                ma_periods = user_config['ma_periods'],
                show_volume = user_config['show_volume']
            )
else:
    st.info("Configure your settings in the sidebar and click 'Fetch Data' to view stock prices.")



