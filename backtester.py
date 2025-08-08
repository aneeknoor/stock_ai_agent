import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

def simulate_signals(df, signal_func):
    results = []
    for i in range(50, len(df) - 1):
        window = df.iloc[:i+1]
        signal = signal_func(window)
        entry_price = df.iloc[i]['Close']
        next_price = df.iloc[i+1]['Close']
        pnl = next_price - entry_price if signal == "BUY" else entry_price - next_price if signal == "SELL" else 0
        correct = (pnl > 0) if signal in ["BUY", "SELL"] else None
        results.append({
            "Date": df.index[i],
            "Signal": signal,
            "Entry": entry_price,
            "Next Close": next_price,
            "PnL": pnl,
            "Correct": correct
        })
    return pd.DataFrame(results)

def plot_cumulative_returns(results_df):
    results_df['CumReturn'] = results_df['PnL'].cumsum()
    fig, ax = plt.subplots()
    results_df.set_index('Date')['CumReturn'].plot(ax=ax, title="Cumulative Return")
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    return base64.b64encode(buf.read()).decode()
