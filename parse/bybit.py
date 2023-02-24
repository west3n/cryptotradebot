from pybit import usdt_perpetual


def connect_bybit(stat):
    session_auth = usdt_perpetual.HTTP(
        endpoint="https://api.bybit.com",
        api_key=stat[0],
        api_secret=stat[1]
    )
    values = ["ADA", "BTC", "EOS", "USDT", "SOL", "BIT", "MANA", "ETH", "XRP", "DOT", "LTC"]
    lol=''
    for x in values:
        result = session_auth.get_wallet_balance(coin=x)
        wallet_balance = result["result"][x]["wallet_balance"]
        lol += f"{x} : {wallet_balance}\n"
    open_orders = session_auth.get_active_order(symbol="BTCUSDT")
    try:
        tp = open_orders["result"]["data"]['take_profit']
    except TypeError:
        tp = "Нет операций"
    try:
        sl = open_orders["result"]["data"]['stop_loss']
    except TypeError:
        sl = "Нет операций"
    return lol, tp, sl


def close_bybit(stat):
    session_auth = usdt_perpetual.HTTP(
        endpoint="https://api.bybit.com",
        api_key=stat[0],
        api_secret=stat[1]
    )
    cancel_all_orders = session_auth.cancel_all_active_orders(symbol="BTCUSDT")
    try:
        cao = cancel_all_orders['result']
    except:
        cao = 'Нет открытых ордеров'

    return cao
