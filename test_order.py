from bot.client import get_client

client = get_client()

try:
    client.futures_change_leverage(
        symbol="BTCUSDT",
        leverage=10
    )

    order = client.futures_create_order(
        symbol="BTCUSDT",
        side="BUY",
        type="MARKET",
        quantity=0.001
    )

    print(order)

except Exception as e:
    print("ERROR:", e)