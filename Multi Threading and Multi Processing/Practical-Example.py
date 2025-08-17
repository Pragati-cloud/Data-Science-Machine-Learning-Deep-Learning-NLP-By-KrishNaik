# multi treading for I/O bound tasks - web scrapping (It ofter involves numerous network requests to fetch web pages. it spend a lot of time waiting for the response from servers) multitreading can significantly improve performance.

import threading
import requests
from bs4 import BeautifulSoup

urls=['https://www.udemy.com/?utm_source=aff-campaign&utm_medium=udemyads&LSNPUBID=wizKxmN8no4&ranMID=47907&ranEAID=wizKxmN8no4&ranSiteID=wizKxmN8no4-VOnmQkuAFJPf0QyxsKATXw&gad_source=1&gad_campaignid=22388734312&gbraid=0AAAAApACmIN7wgaOX88ShWrPQsClVWg9I&gclid=Cj0KCQjw-4XFBhCBARIsAAdNOksAl3nVVmjA-gCho6_KeGpvDgrugh51-WZOvfbBb08DxbqB9-qglG0aAkLHEALw_wcB','https://www.udemy.com/course/machinelearning/?couponCode=KEEPLEARNING','https://www.udemy.com/course/python-for-data-science-and-machine-learning-bootcamp/?couponCode=KEEPLEARNING']

def fetch_content(url):
  response= requests.get(url)
  soup = BeautifulSoup(response.content,'html.parser')
  print(f'Fetched {len(soup.text)} character from {url}')


threads=[]

for url in urls:
  thread= threading.Thread(target=fetch_content,args=(url,))
  threads.append(thread)
  thread.start()

for thread in threads:
  thread.join()

print('all web pages fetched')