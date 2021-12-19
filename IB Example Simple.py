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

# Class for IB connection
class IBApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    # Listen for realtime bars
    #def realtimeBar(self, reqId, time, open_, high, low, close, volume, wap, count):
        #bot.on_bar_update(reqId, time, open_, high, low, close, volume, wap, count)


# Bot Logic
class Bot:
    ib = None
    def __init__(self):
        # Connect to IB on init
        self.ib = IBApi()
        self.ib.connect("127.0.0.1", 7496, 1)
        ib_thread = threading.Thread(target=self.run_loop, daemon=True)
        ib_thread.start()
        time.sleep(1)
        symbol = input("Input the symbol you want to trade: ")
        contract = Contract()
        contract.symbol = symbol.upper()
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"
        #Request market data
        self.ib.reqRealTimeBars(0, contract, 5, "TRADES", 1, [])


    # Listen to socket in a separate thread
    def run_loop(self):
        self.ib.run()

    # Pass realtime bar data back to bot object
    def on_bar_update(self, reqId, time, open_, high, low, close, volume, wap, count):
        print(close)

# Start Bot
bot = Bot()
