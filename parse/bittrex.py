from bittrex_api import Bittrex


def bittrex_connect(stat):
    bittrex = Bittrex(
        api_key=stat[0],
        secret_key=stat[1],
        max_request_try_count=1,
        sleep_time=2,
        debug_level=2)
    market_name = 'USDT-BTC'
    open_orders = bittrex.v3.get_open_orders(market_name)
    if not open_orders:
        open_orders = "Нет открытых ордеров"
    try:
        for x in range(0, 10):
            result = f"{bittrex.v3.get_balances()[x].get('currencySymbol')} :" \
                     f" {round(float(bittrex.v3.get_balances()[x].get('total')), 2)}"
            x += 1
            return result, open_orders
    except IndexError:
        result = "Нет данных"
        return result, open_orders


def cancel_all_orders(stat):
    bittrex = Bittrex(
        api_key=stat[0],
        secret_key=stat[1],
        max_request_try_count=1,
        sleep_time=2,
        debug_level=2)
    market_name = 'USDT-BTC'
    open_orders = bittrex.v3.get_open_orders(market_name)
    print(open_orders)
    try:
        for order in open_orders["result"]:
            result = bittrex.v3.cancel_order(order['OrderUuid'])
            if result == "success":
                text = 'Все активные ордеры закрыты'
            else:
                text = 'Не смог закрыть ордеры.'
            return text
    except TypeError:
        text = "Все активные ордеры закрыты"
        return text
