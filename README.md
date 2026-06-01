# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based command-line trading bot that interacts with the Binance Futures Testnet (USDT-M). It allows users to place MARKET and LIMIT orders for both BUY and SELL sides through a simple CLI interface.

The application is designed with a modular structure, input validation, logging, and exception handling to ensure reliability and maintainability.

---

## Features

* Place MARKET orders
* Place LIMIT orders
* Support for BUY and SELL orders
* Binance Futures Testnet integration
* Command-line interface using argparse
* Input validation
* Request and response logging
* Error handling for API and network issues
* Modular and reusable code structure

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## Requirements

* Python 3.10+
* Binance Futures Testnet Account
* Binance Testnet API Key and Secret

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd trading_bot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root directory:

```env
BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key
```

---

## Usage

### Place a MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

Example Output:

```text
ORDER REQUEST
------------------------------
Symbol : BTCUSDT
Side   : BUY
Type   : MARKET
Qty    : 0.001

ORDER RESPONSE
------------------------------
Order ID      : 13679638971
Status        : NEW
Executed Qty  : 0.0000
Average Price : 0.00

SUCCESS
```

---

### Place a LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 200000
```

Example Output:

```text
ORDER REQUEST
------------------------------
Symbol : BTCUSDT
Side   : SELL
Type   : LIMIT
Qty    : 0.001
Price  : 200000

ORDER RESPONSE
------------------------------
Order ID      : 13679741269
Status        : NEW
Executed Qty  : 0.0000
Average Price : 0.00

SUCCESS
```

---

## Logging

All requests, responses, and errors are logged to:

```text
logs/trading_bot.log
```

Example:

```text
INFO - Request: BTCUSDT BUY MARKET qty=0.001
INFO - Response: {...}

INFO - Request: BTCUSDT SELL LIMIT qty=0.001 price=200000.0
INFO - Response: {...}
```

---

## Error Handling

The application handles:

* Invalid order side
* Invalid order type
* Missing LIMIT order price
* Binance API errors
* Network failures
* Authentication issues

---

## Dependencies

```text
python-binance
python-dotenv
```

---

## Assumptions

* User has a Binance Futures Testnet account.
* Valid API credentials are configured.
* Testnet funds are available in the Futures wallet.
* Orders are executed only on the Binance Futures Testnet environment.

---

## Author

Python Trading Bot Internship Assignment Submission
