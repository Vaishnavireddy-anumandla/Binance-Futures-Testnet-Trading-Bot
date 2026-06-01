from bot.client import get_client
from bot.logging_config import logger


def place_order(symbol, side, order_type,
                quantity, price=None):

    client = get_client()

    try:
        # Set leverage before placing order
        client.futures_change_leverage(
            symbol=symbol,
            leverage=10
        )

        logger.info(
            f"Request: {symbol} {side} "
            f"{order_type} qty={quantity} "
            f"price={price}"
        )

        if order_type == "MARKET":

            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":

            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        else:
            raise ValueError(
                "Unsupported order type"
            )

        logger.info(f"Response: {response}")

        return response

    except Exception as e:

        logger.error(str(e))
        raise