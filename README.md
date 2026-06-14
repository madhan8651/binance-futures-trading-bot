# Binance Futures Trading Bot

## Overview

A Python CLI application that places BUY and SELL orders on Binance Futures Demo/Testnet (USDT-M).

### Features

* Market Orders
* Limit Orders
* BUY and SELL support
* Input validation
* Logging
* Exception handling
* Modular code structure

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file:

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

## Logging

Logs are stored in:

```text
logs/trading.log
```

## Assumptions

* Binance Futures Demo/Testnet is used.
* API credentials are provided through a `.env` file.
* Quantity and price values comply with Binance rules.
