from bot.client import get_client

client = get_client()

try:
    response = client.futures_change_leverage(
        symbol="BTCUSDT",
        leverage=10
    )

    print(response)

except Exception as e:
    print("ERROR:", e)