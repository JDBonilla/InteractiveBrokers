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


# Class for IB connection
class IBApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)


# Vars
# Connect to IB on init
ib = IBApi()
ib.connect("127.0.0.1", 7496, 1)
time.sleep(1)
symbol = input("Input the symbol you want to trade: ")
contract = Contract()
contract.symbol = symbol.upper()
contract.secType = "STK"
contract.exchange = "SMART"
contract.currency = "USD"
bars = ib

# convert to pandas dataframe
df = util.df(bars)
print(df)


# Bot Logic
def __init__(self):
    print("ok")
    ib.run(self)
