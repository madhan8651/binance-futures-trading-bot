# Binance Futures Trading Bot

## Overview

A Python CLI application that places BUY and SELL orders on Binance Futures Demo/Testnet (USDT-M).

## Features

* Market Orders
* Limit Orders
* BUY and SELL support
* Input validation
* Logging
* Exception handling
* Modular code structure

## Project Structure

```text
bot_task/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```env
API_KEY=YOUR_API_KEY
API_SECRET=YOUR_API_SECRET
```

## Usage

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 80000
```

## Example Output

```text
===== ORDER SUMMARY =====
Symbol   : BTCUSDT
Side     : BUY
Type     : MARKET
Quantity : 0.001

===== ORDER RESPONSE =====
Order ID      : 15153775496
Status        : NEW
Executed Qty  : 0.0000
Average Price : N/A

✅ Order placed successfully!
```

## Logging

All API requests, responses, and errors are stored in:

```text
logs/trading.log
```

## Error Handling

The application handles:

* Invalid user input
* Missing price for LIMIT orders
* Binance API errors
* Network-related exceptions

## Assumptions

* Binance Futures Demo/Testnet is used.
* API credentials are provided through a `.env` file.
* Quantity and price values comply with Binance trading rules.

## Dependencies

* python-binance
* python-dotenv
