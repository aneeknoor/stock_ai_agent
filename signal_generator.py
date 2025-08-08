def generate_signal(df):
    last = df.iloc[-1]
    if last['RSI'] < 30 and last['MACD'] > 0 and last['EMA_20'] > last['EMA_50']:
        return "BUY"
    elif last['RSI'] > 70 and last['MACD'] < 0 and last['EMA_20'] < last['EMA_50']:
        return "SELL"
    else:
        return "HOLD"
