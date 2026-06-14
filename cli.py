import argparse

from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Demo Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading symbol (e.g. BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        help="BUY or SELL"
    )

    parser.add_argument(
        "--type",
        required=True,
        help="MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        help="Price (required for LIMIT orders)"
    )

    args = parser.parse_args()

    try:

        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        client = BinanceClient().get_client()
        order_manager = OrderManager(client)

        print("\n===== ORDER SUMMARY =====")
        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {quantity}")

        if order_type == "MARKET":

            response = order_manager.market_order(
                symbol,
                side,
                quantity
            )

        else:

            if not args.price:
                raise ValueError(
                    "Price is required for LIMIT orders"
                )

            response = order_manager.limit_order(
                symbol,
                side,
                quantity,
                args.price
            )

        print("\n===== ORDER RESPONSE =====")
        print("Order ID      :", response.get("orderId"))
        print("Status        :", response.get("status"))
        print("Executed Qty  :", response.get("executedQty"))
        print("Average Price :", response.get("avgPrice", "N/A"))

        print("\n✅ Order placed successfully!")

    except ValueError as e:

        print("\n❌ Validation Error")
        print(str(e))

    except Exception as e:

        print("\n❌ API / Network Error")
        print(str(e))


if __name__ == "__main__":
    main()