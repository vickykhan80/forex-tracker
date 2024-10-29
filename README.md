# forex-tracker
A Python program that fetches real-time forex exchange rates using the Alpha Vantage API. The application tracks currency exchange rates at specified intervals and prints the current rate along with the date and time.
## Features
+ Fetches real-time exchange rates using Alpha Vantage API.
+ Displays exchange rate along with current date and time.
+ Auto-updates the exchange rate every minute.

## Requirements
+ Python
+ Requests Library
+ Alpha Vantage API key
## Setup Instructions
_pkg update && pkg upgrade_

_pkg install python_

_pip install requests_

_git clone https://github.com/vickykhan80/forex-tracker.git_

_cd forex-tracker_

_python forex_tracker.py_

## How to Use
1. **Tracking a Currency Pair**
  + The default currency pair is USD/EUR.
  + The program prints the current exchange rate, date, and time, updating every minute.
2. **Exchange Rate Data**

   + The script fetches data every minute, printing the latest rate for the specified currency pair along with a timestamp.
## License
This project is open-source and available under the MIT License.
## Author
**Vicky Khan**
