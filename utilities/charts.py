import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_candlestick_chart(df, ma_periods, show_volume, stock_name):
    fig = make_subplots(
        rows=2 if show_volume else 1,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.03,
        row_width=[0.2, 0.7] if show_volume else [1.0]
    )

    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name='Price'), row=1, col=1
    )

    for i, period in enumerate(ma_periods):
        if f'MA_{period}' in df.columns:
            fig.add_trace(go.Scatter(
                x=df.index,
                y=df[f'MA_{period}'],
                mode='lines',
                name=f'MA {period}'), row=1, col=1)

    if show_volume and 'Volume' in df.columns:
        fig.add_trace(go.Bar(x=df.index, y=df['Volume'], name='Volume'), row=2, col=1)

    fig.update_layout(xaxis_rangeslider_visible=False,
                      title = {
                          'text': f"{stock_name} - Candlestick Chart",
                          'x': 0.5,
                          'xanchor': 'center'
                      }
                      )
    return fig

def create_line_chart(df, ma_periods, show_volume, stock_name):
    fig = make_subplots(
        rows=2 if show_volume else 1,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.03,
        row_width=[0.2, 0.7] if show_volume else [1.0]
    )

    # Line chart of Close price
    fig.add_trace(
        go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close Price'),
        row=1, col=1
    )

    # Moving averages
    for i, period in enumerate(ma_periods):
        ma_col = f'MA_{period}'
        if ma_col in df.columns:
            fig.add_trace(
                go.Scatter(x=df.index, y=df[ma_col], mode='lines', name=f'MA {period}'),
                row=1, col=1
            )

    # Volume chart
    if show_volume and 'Volume' in df.columns:
        fig.add_trace(
            go.Bar(x=df.index, y=df['Volume'], name='Volume', marker_color='lightblue'),
            row=2, col=1
        )

    fig.update_layout(
        title={'text': f"{stock_name} - Line Chart", 'x': 0.5, 'xanchor': 'center'},
        xaxis_rangeslider_visible=False
    )

    return fig

def create_ohlc_chart(df, show_volume, stock_name):
    fig = make_subplots(
        rows=2 if show_volume else 1,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.03,
        row_width=[0.2, 0.7] if show_volume else [1.0]
    )

    # OHLC Chart
    fig.add_trace(
        go.Ohlc(
            x=df.index,
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            name='OHLC'
        ),
        row=1, col=1
    )

    # Volume Chart
    if show_volume and 'Volume' in df.columns:
        fig.add_trace(
            go.Bar(
                x=df.index,
                y=df['Volume'],
                name='Volume',
                marker_color='lightblue'
            ),
            row=2, col=1
        )

    fig.update_layout(
        title={'text': f"{stock_name} - OHLC Chart", 'x': 0.5, 'xanchor': 'center'},
        xaxis_rangeslider_visible=False
    )

    return fig

