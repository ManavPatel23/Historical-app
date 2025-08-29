# Historical Stock Market Analysis Dashboard

A comprehensive historical stock market analysis dashboard built with Streamlit that provides in-depth analysis of stock performance, technical indicators, and market trends.

## Features

- 📊 **Historical Price Analysis** - Detailed price charts and trends
- 📈 **Technical Indicators** - Moving averages, RSI, MACD, and more
- 🔍 **Multi-timeframe Analysis** - Daily, weekly, monthly views
- 📋 **Stock Comparison** - Compare multiple stocks side by side
- 💹 **Portfolio Analysis** - Track portfolio performance
- 📱 **Interactive Charts** - Zoom, pan, and explore data
- 📊 **Statistical Analysis** - Volatility, returns, correlations

## Live Demo

[Your historical analysis app will be deployed here]

## Features Overview

### Technical Analysis
- Moving Averages (SMA, EMA)
- Relative Strength Index (RSI)
- MACD (Moving Average Convergence Divergence)
- Bollinger Bands
- Volume Analysis

### Data Visualization
- Interactive Plotly charts
- Multiple chart types (candlestick, line, bar)
- Customizable timeframes
- Export capabilities

### Portfolio Tools
- Performance tracking
- Risk analysis
- Diversification metrics
- Historical backtesting

## Local Development

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Technologies Used

- **Streamlit** - Web app framework
- **yfinance** - Historical financial data
- **Plotly** - Interactive charts
- **Pandas** - Data analysis and manipulation
- **NumPy** - Numerical computations
- **Matplotlib & Seaborn** - Statistical visualizations

## Project Structure

```
├── app.py                 # Main application
├── ui/
│   ├── layout.py         # UI layout components
│   └── sidebar.py        # Sidebar controls
├── utilities/
│   ├── charts.py         # Chart generation
│   ├── data_fetcher.py   # Data fetching utilities
│   └── technical.py      # Technical analysis functions
└── requirements.txt      # Dependencies
```

## Author

Built with ❤️ for comprehensive stock market analysis
