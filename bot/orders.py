from bot.logging_config import logger

class OrderManager:

    def __init__(self, client):
        self.client = client

    def market_order(self, symbol, side, quantity):

        logger.info(
            f"MARKET ORDER | Symbol={symbol} Side={side} Quantity={quantity}"
        )

        response = self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(response)

        return response

    def limit_order(
        self,
        symbol,
        side,
        quantity,
        price
    ):

        logger.info(
            f"LIMIT ORDER | Symbol={symbol} Side={side} Quantity={quantity} Price={price}"
        )

        response = self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(response)

        return response
    