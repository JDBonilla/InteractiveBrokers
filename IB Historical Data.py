# Based on Jacob Amaral YT "How To Code A Trading Bot With Interactive" series
# Imports
import ibapi
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
# Symbol and Exchange
from ibapi.contract import Contract
from ibapi.order import *
# To stream real-time data on a different thread as a socket
import threading
import time


# Vars

# Listen to socket in a separate thread
def run_loop(self):
    self.ib.run()


# Pass realtime bar data back to bot object
def on_bar_update(self, reqId, time, open_, high, low, close, volume, wap, count):
    print(close)

# Class for IB connection
class IBApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

# Listen to socket in a separate thread
def run_loop():
     ib.run()


# Bot Logic
def __init__(self):
    # Connect to IB on init
    print('ok')
    self.ib = IBApi()
    self.ib.connect("127.0.0.1", 7496, 1)
    ib_thread = threading.Thread(target=run_loop, daemon=True)
    ib_thread.start()
    time.sleep(1)
    symbol = input("Input the symbol you want to trade: ")
    stock = self.Stock(symbol)
    bars = ib.reqHistoricalData(
        stock, endDateTime='', durationStr='30 D',
        barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)
    # convert to pandas dataframe
    df = self.util.df(bars)
    print(df)
    #contract = Contract()
    #contract.symbol = symbol.upper()
    #contract.secType = "STK"
    #contract.exchange = "SMART"
    #contract.currency = "USD"
    #Request market data
    #.ib.reqRealTimeBars(0, contract, 5, "TRADES", 1, [])





