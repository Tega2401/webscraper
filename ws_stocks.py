import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time
import os 
from smtplib import SMTP, SMTP_SSL
import imghdr 
import pync
import os




def send(): 

    pync.notify('Check your stocks', title='Morning Portfolio Summary')


# def get_info():

tickers = { 
    'company': 'SQ', 
    'market': ':NYSE', 
    


}

    

page = requests.get('https://www.google.com/finance/quote/' + str(tickers['company', 'c']) + str(tickers['market'])).text


soup = BeautifulSoup(page, 'html.parser')

numbers = soup.find_all('div', {'class': 'uptEI'})

news = soup.find_all('div', {'class': 'yY3Lee' })

data = pd.DataFrame(columns = ['Previous Close', 'Volume', 'Days Range'])

news_column = pd.DataFrame(columns = ['News'])

for artist in numbers: 
    name = artist.find_all('div', {'class': 'M2CUtd'})
    previous_close = name[0].text
    days_range = name[1].text
    volume = name[4].text
    data = data.append({'Previous Close': previous_close, 'Volume': volume, 'Days Range': days_range }, ignore_index=True)

for article in news: 
    ne = article.find_all('div', {'class': 'AoCdqe'})
    news_single = ne[0].text

    news_column = news_column.append({'News': news_single}, ignore_index=True )


print(data)
print(news_column)

# schedule.every().day.at('08:00').do(get_info)
# schedule.every().day.at('08:03').do(send)


# while True: 
#     schedule.run_pending()
#     time.sleep(1)


