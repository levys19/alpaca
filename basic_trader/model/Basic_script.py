import alpaca_trade_api as tradeapi
import os


api = tradeapi.REST(api_version='v2')
account = api.get_account()
print(account.status)
print(account)

api.submit_order(symbol = 'SPY', qty = 1, side = 'buy', type='market', time_in_force='day', limit_price=None, stop_price=None, client_order_id=None, order_class=None, take_profit=None, stop_loss=None)
print(account)
