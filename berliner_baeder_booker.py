import time
from beepy import beep
import requests
from bs4 import BeautifulSoup

baeder_id = input('Enter hall id as number e.g. 49: ')
data_date_ = input('Enter date in YYYY-MM-DD format: ')
data_time_ = input('Enter time in HH:MM 24h format: ')
search_len = input('Enter search duration in minutes: ')
search_len = int(search_len)

base_url = "https://pretix.eu/Baeder/"

URL = base_url + str(baeder_id) + "/"


for i in range(search_len):
    page = requests.get(URL, verify='./pretix-eu-chain.pem')

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id='subevent-list')
    data_elements = results.find_all("td", class_ = 'day has-events')

    for elem in data_elements:
        if elem.find("time", {"datetime": data_date_}):
            for event in elem.find_all('li'):
                if event.find("time", {"datetime": data_time_}):
                    time_event = event
                    break
        
    if time_event.find('a', 'event over'):
        print('This event is over! Please enter another date/time.')
        break
    elif (time_event.find('a', 'event available')):
        print('Found one, hurry!')
        beep(sound='success')
        break
    else:
    #elif (time_event.find('a', 'event soldout')) or (time_event.find('a', 'event soon')) or (time_event.find('a', 'event reserved')) or (time_event.find('a', 'event soon')):
        print('Not available!')
    
    if i == search_len -1:
        print("Search finished! We couldn't find any empty slots during the search period. You can try to search longer.")
        break

    time.sleep(40)