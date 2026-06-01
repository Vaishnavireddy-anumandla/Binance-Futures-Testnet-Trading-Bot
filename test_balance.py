from bot.client import get_client

client = get_client()

try:
    balances = client.futures_account_balance()

    print("\nFUTURES BALANCES\n")

    for item in balances:
        if float(item["balance"]) > 0:
            print(item)

except Exception as e:
    print("ERROR:", e)