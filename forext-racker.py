import requests
import time
from datetime import datetime

class ForexTracker:
    def __init__(self, api_key):
        self.api_key = api_key
        self.forex_base_url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

    def get_forex_rate(self, from_currency, to_currency):
        """Fetch the latest forex exchange rate for a given currency pair."""
        url = f"{self.forex_base_url}&from_currency={from_currency}&to_currency={to_currency}&apikey={self.api_key}"
        try:
            response = requests.get(url)
            data = response.json()
            rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
            print(f"Exchange Rate {from_currency}/{to_currency}: {rate}")
            return rate
        except Exception as e:
            print(f"Error fetching forex rate for {from_currency}/{to_currency}: {e}")
            return None

    def track(self, from_currency="USD", to_currency="EUR"):
        """Tracks and prints forex rates with date and time at intervals."""
        while True:
            print("\n--- Real-Time Forex Tracking ---")
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Date and Time: {current_time}")
            forex_rate = self.get_forex_rate(from_currency, to_currency)
            print(f"Current {from_currency}/{to_currency} Rate: {forex_rate}")
            print("-" * 50)
            time.sleep(60)  # Update every minute



if __name__ == "__main__":
    api_key = "708bea20a07fe98ab4851ef25f8e7817"
    tracker = ForexTracker(api_key)
    tracker.track(from_currency="USD", to_currency="EUR")  # Track USD/EUR
