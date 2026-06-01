import argparse

from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type
)


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:

        side = validate_side(args.side)
        order_type = validate_order_type(args.type)

        if order_type == "LIMIT" and args.price is None:
            raise ValueError(
                "Price required for LIMIT order"
            )

        print("\nORDER REQUEST")
        print("-" * 30)

        print(f"Symbol : {args.symbol}")
        print(f"Side   : {side}")
        print(f"Type   : {order_type}")
        print(f"Qty    : {args.quantity}")

        if args.price:
            print(f"Price  : {args.price}")

        response = place_order(
            args.symbol,
            side,
            order_type,
            args.quantity,
            args.price
        )

        print("\nORDER RESPONSE")
        print("-" * 30)

        print(
            f"Order ID      : "
            f"{response.get('orderId')}"
        )

        print(
            f"Status        : "
            f"{response.get('status')}"
        )

        print(
            f"Executed Qty  : "
            f"{response.get('executedQty')}"
        )

        print(
            f"Average Price : "
            f"{response.get('avgPrice')}"
        )

        print("\nSUCCESS")

    except Exception as e:

        print(f"\nFAILED: {e}")


if __name__ == "__main__":
    main()