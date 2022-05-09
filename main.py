'''
This version of code deploy to a Docker container
'''
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

def get_urls():
    file = open('usa_urls.txt', 'r')
    for line in file.readlines():
        usa_list.append(line)

usa_list = []
get_urls()

def run_program():
    outputFile = open(f"output/{str(datetime.now()).split('.')[0].replace(' ', 'T').replace(':', '-')}.txt", "w", encoding="utf-8")
    listingsPool = []

    for link in usa_list:
        URL = f"{link.strip()}/d/gigs/search/ggg"
        try:
            page = requests.get(URL)
        except Exception as e:
            print(f'GET request error - {link}')
            pass
        # print(page) --> <Response [200]>
        soup = BeautifulSoup(page.content, 'html.parser')
        listings = soup.find_all('li', class_="result-row")
        for listing in listings:
            tempPool = []
            listingTitle = listing.find('a', class_="result-title").text
            listingURL = listing.find('a', class_="result-image")['href']
            tempPool.append(listingTitle)
            tempPool.append(listingURL)
            listingsPool.append(tempPool)
            outputFile.write(f'{str(tempPool)}\n')

    outputFile.close()

while True:
    run_program()
    time.sleep(10800)
