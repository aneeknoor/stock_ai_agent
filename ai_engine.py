import os
from dotenv import load_dotenv
import openai

load_dotenv()  # Loads from .env

openai.api_key = os.getenv("OPENAI_API_KEY")

# Optional: check if it's loaded
if not openai.api_key:
    print("❌ OPENAI_API_KEY not set.")
else:
    print("✅ API key loaded successfully.")


def explain_analysis(ticker, signal, sentiment, rsi, macd, ema_diff, price):
    prompt = f"""
You are a financial analyst. Here is the data for stock {ticker}:

- Current Price: ${price:.2f}
- Signal: {signal}
- RSI: {rsi:.2f}
- MACD: {macd:.2f}
- EMA Gap (20 EMA - 50 EMA): {ema_diff:.2f}
- Sentiment Score: {sentiment:.2f}

Explain the reasoning behind the signal and what an investor should consider. Also, provide a short-term forecast (next 5–10 days) and risk outlook.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']
