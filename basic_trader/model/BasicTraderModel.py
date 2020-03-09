import alpaca_trade_api as tradeapi

class BasicTraderModel:

    def __init__(self):
        api = tradeapi.REST('<key_id>', '<secret_key>', api_version='v2')



     # or use ENV Vars shown below
    account = api.get_account()
    api.list_positions()
