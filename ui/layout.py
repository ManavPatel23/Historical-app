import streamlit as st
from utilities.charts import create_candlestick_chart, create_line_chart, create_ohlc_chart

def display_dashboard(df, info, stock, chart_type, show_ma, ma_periods, show_volume, start_date, end_date):
    # Defensive: Check if df is valid
    if df is None or df.empty:
        st.error("❌ Dataframe is empty. Cannot display dashboard.")
        return

    required_cols = ['Close', 'High', 'Low', 'Volume']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        st.error(f"❌ Missing required columns in data: {', '.join(missing_cols)}")
        return

    # name = info.get('longName', stock)
    # st.success(f"📊 Data fetched successfully for {name} ({stock})")

    # Display metrics
    col1, col2, col3, col4 = st.columns(4)
    try:
        col1.metric("Latest Price", f"₹{df['Close'].iloc[-1]:.2f}")
        col2.metric("High", f"₹{df['High'].max():.2f}")
        col3.metric("Low", f"₹{df['Low'].min():.2f}")
        col4.metric("Volume Avg", f"{df['Volume'].mean():,.0f}")
    except Exception as e:
        st.warning(f"⚠️ Unable to compute some metrics: {e}")

    # Chart rendering
    try:
        if chart_type == "Candlestick":
            st.plotly_chart(create_candlestick_chart(df, ma_periods, show_volume, stock), use_container_width=True)
        elif chart_type == "Line Chart":
            st.plotly_chart(create_line_chart(df, ma_periods, show_volume, stock), use_container_width=True)
        elif chart_type == "OHLC":
            st.plotly_chart(create_ohlc_chart(df, show_volume, stock), use_container_width=True)
        else:
            st.warning("Unknown chart type selected.")
    except Exception as e:
        st.error(f"❌ Error rendering chart: {e}")

    # Raw data
    st.subheader("📋 Raw Data")
    st.dataframe(df.round(2))

    # CSV download
    try:
        csv = df.to_csv()
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name=f"{stock}_{start_date}_{end_date}.csv",
            mime="text/csv"
        )
    except Exception as e:
        st.warning(f"⚠️ Error generating CSV: {e}")
