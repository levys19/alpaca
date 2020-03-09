import logging
from alpaca_trade_api import StreamConn
conn = StreamConn()

@conn.on(r'^account_updates$')
async def on_account_updates(conn, channel, account):
    logging.debug('account', account)

@conn.on(r'^trade_updates$')
async def on_status(conn, channel, data):
    logging.debug('trade updates', data)

@conn.on(r'^AM$')
async def on_minute_bars(conn, channel, bar):
    logging.debug('bars', bar)

@conn.on(r'^A$')
async def on_second_bars(conn, channel, bar):
    logging.debug('bars', bar)

# blocks forever
conn.run(['account_updates', 'A.*', 'trade_updates'])
