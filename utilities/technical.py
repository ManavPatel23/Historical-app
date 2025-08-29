import pandas as pd

def clean_dataframe(df):
    if df is None or df.empty:
        return df

    # Flatten MultiIndex columns if present
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [col[0] for col in df.columns]  # keep only the field name

    df = df.reset_index()

    # Set 'Date' or 'Datetime' as index
    if 'Date' in df.columns:
        df.set_index('Date', inplace=True)
    elif 'Datetime' in df.columns:
        df.set_index('Datetime', inplace=True)

    return df

def calculate_indicators(df, ma_periods):
    if df is None or df.empty or 'Close' not in df.columns:
        return df
    for period in ma_periods:
        df[f'MA_{period}'] = df['Close'].rolling(window=period).mean()
    df['Daily_Return'] = df['Close'].pct_change()
    return df
