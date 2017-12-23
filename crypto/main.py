import matplotlib.pyplot as plt
import time
from crypto_compare_api import live_price, minute_price_historical
from constants import FULL_EXHANGE_LIST, WORK_ECHANGE_LIST
from crypto_compare_api import ret_exchange_list

if __name__=="__main__":

    #symbol_id_dict = {symb: int(d['Id']) for symb, d in data.items()}
    #while(1):
        # ret_exchange_list(['Bitstamp'])
    with open('bitstamp2.txt', 'w') as btsf:
        btsf.write(minute_price_historical('BTC', 'USD', 100, 1, exchange='Bitstamp').to_string())
    with open('coinbase2.txt', 'w') as cnbsf:
        cnbsf.write(minute_price_historical('BTC', 'USD', 100, 1, exchange='Coinbase').to_string())
        # data = [live_price('BTC', ['USD'], exchange='LiveCoin')]
        # print data
        #time.sleep(0.1)
