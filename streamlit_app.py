import streamlit as st
from data_fetcher import get_stock_data
from technical_analysis import add_technical_indicators
from sentiment_analysis import get_news_sentiment
from signal_generator import generate_signal
from ai_engine import explain_analysis
from backtester import simulate_signals, plot_cumulative_returns

def main():
    st.title("📈 Stock Analysis AI Agent")
    tickers = st.text_input("Enter tickers (comma-separated)", "AAPL,TSLA")
    period = st.selectbox("Select lookback period", ["1mo", "3mo", "6mo", "1y"], index=1)
    backtest = st.checkbox("Enable Backtest", value=True)

    if st.button("Analyze"):
        for ticker in [t.strip().upper() for t in tickers.split(",")]:
            df = get_stock_data(ticker, period=period)
            df = add_technical_indicators(df)
            sentiment = get_news_sentiment(ticker)
            signal = generate_signal(df)

            last = df.iloc[-1]
            rsi = last['RSI']
            macd = last['MACD']
            ema_diff = last['EMA_20'] - last['EMA_50']
            price = last['Close']

            ai_output = explain_analysis(ticker, signal, sentiment, rsi, macd, ema_diff, price)

            st.subheader(f"{ticker} — {signal}")
            st.write(f"Current Price: ${price:.2f}")
            st.write(f"Sentiment Score: {sentiment:.2f}")
            st.markdown("**AI Explanation:**")
            st.info(ai_output)

            if backtest:
                results = simulate_signals(df, generate_signal)
                st.write(results.tail(10))
                image_b64 = plot_cumulative_returns(results)
                st.image(f"data:image/png;base64,{image_b64}")
