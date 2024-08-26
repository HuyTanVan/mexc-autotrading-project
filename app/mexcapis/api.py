from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

import json
import datetime
# from app.mexcapis.urls import *
# internal import
class MexcUrls:
    # test connectivity to the REST API
    ping_url = 'https://api.mexc.com/api/v3/ping'
    # server time 
    time_url = 'https://api.mexc.com/api/v3/time'
    # Kline/Candlestick Data Spot
    klines_url = 'https://api.mexc.com/api/v3/klines'


    # Future urls
    klines_future_url = 'https://contract.mexc.com/api/v1/contract/kline/'

    
    # symbol = symbol of a coin, interval: 1m,5m,15m,30m,1h,2h...., numbers of calling 1/interval
    # not exactly as the price on website.

""" return a current price a perpetual contract """
def get_current_price(symbol):
        url = 'https://contract.mexc.com/api/v1/contract/index_price/'
        headers = {
            'Accepts': 'application/json',
            'X-MEXC-APIKEY': 'mx0aBYs33eIilxBWC5',
        }
        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(f'{url}{symbol.upper()}_USDT')
            data = json.loads(response.text)
            price = data['data'].get('indexPrice')

            print(f"{symbol.upper()}: ${price}")
            return price

        except (ConnectionError, Timeout, TooManyRedirects, KeyError, AttributeError) as e:
            print("Error:", e)
            return None
        
def klines(symbol: str, interval: int, data_request:int):
        data_request = int(data_request)
        mexc_urls = MexcUrls()
        url = mexc_urls.klines_future_url
        headers = {
            'Accepts': 'application/json',
            'X-MEXC-APIKEY': 'mx0aBYs33eIilxBWC5',
        }
        session = Session()
        session.headers.update(headers)

        response = session.get(f'{url}{symbol}_USDT?interval=Min{interval}')
        # response = session.get(f'{url}{symbol}_USDT?interval=Hour{interval}')

        data = json.loads(response.text)
        # desciptions =['Time', 'Open Price', 'Close Price', 'High Price', 'Low Price', 'Volume']
        open_price = data['data'].get('open')
        close_price = data['data'].get('close')
        high_price = data['data'].get('high')
        low_price = data['data'].get('low')
        volume = data['data'].get('vol')
        time = data['data'].get('time')
        for i in range(len(time)):
            t = datetime.datetime.fromtimestamp(time[i])
            time[i] = t
        dict_data =  {  'time': time[len(volume)-data_request::],
                        'open_price': open_price[len(volume)-data_request::],
                        'close_price': close_price[len(volume)-data_request::],
                        'high_price': high_price[len(volume)-data_request::],
                        'low_price': low_price[len(volume)-data_request::],
                        'volume': volume[len(volume)-data_request::]
                        }
        return dict_data

def get_time(symbol: str, interval: int, data_request = None) -> list:
        symbol.upper()
        if data_request == None:
            data_request = 1
        time = klines(symbol, interval, data_request).get('time')
        # time is represented as the format datetime.datetime(year, month, day, hour, minute),
        # using list comprehension to convert datime type into string type
        time = [str(_)[11:] for _ in time]
        print(time)
        return time
""" return a list of volumes as interval.
    currently accept only minute.
"""
def get_volume(symbol: str, interval: int, data_request = None) -> list:
        symbol = symbol.upper()
        # 1m, 15m 30m, 1h, 12h, 24h
        # 1 as default
        if data_request == None:
            data_request = 1

        volume = klines(symbol, interval, data_request).get('volume')
        
        str_volume = "-> ".join([str(v) for v in volume])
        print(f"Symbol: {symbol}\n"
                f"Interval: {interval} minutes\n"
                f"Data request: {data_request}\n"
                f"Volume: {str_volume}\n"
            )
        return volume
""" return a open price of a contract at a specific time period """
def get_open_price(symbol: str, interval: int, data_request = None) -> list:
        # 1m, 15m 30m, 1h, 12h, 24h
        # 1 as default
        if data_request == None:
            data_request = 1
        return klines(symbol, interval, data_request).get('open_price')

""" return a close price of a contract at a specific time period """
def get_close_price(symbol: str, interval: int, data_request = None) -> list:
        # 1m, 15m 30m, 1h, 12h, 24h
        # 1 as default
        if data_request == None:
            data_request = 1
        return klines(symbol, interval, data_request).get('close_price')

""" to check if the previous of the current volume is short or long """
def is_previous_long(symbol: str, interval: int):  
    previous = klines(symbol=symbol, interval=interval, data_request=2)
    return previous.get("open_price")[0] < previous.get("close_price")[0]

""" to check if the current volume is short or long """
def is_current_long(symbol: str, interval: int):
    previous = klines(symbol=symbol, interval=interval, data_request=1)
    return previous.get("open_price") < previous.get("close_price")

