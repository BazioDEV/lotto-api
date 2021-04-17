from __future__ import absolute_import, unicode_literals
from time import sleep
from .models import *
from celery import shared_task
from bs4 import BeautifulSoup
import requests

@shared_task
def hannoi_lotto_create():
    print('Fetching Hanoi data...')
    req = requests.get('https://www.ruay.info/%e0%b8%95%e0%b8%a3%e0%b8%a7%e0%b8%88%e0%b8%ab%e0%b8%a7%e0%b8%a2%e0%b8%ae%e0%b8%b2%e0%b8%99%e0%b8%ad%e0%b8%a2/')
    bs = BeautifulSoup(req.content, 'html.parser')
    title = bs.find_all('strong')[1].get_text()
    date = bs.find_all('span')[15].get_text()[24:35]
    Four = bs.find_all('b')[3].get_text()
    Three = bs.find_all('b')[4].get_text()
    Two = bs.find_all('b')[5].get_text()

    hannoi_lotto.objects.create(
        title=title,
        Four=Four,
        Three=Three,
        Two=Two,
        date=date
    )
    print('Data have been create')
    sleep(3)
    
@shared_task
def hannoi_lotto_update():
    print('Updating Hanoi data...')
    req = requests.get('https://www.ruay.info/%e0%b8%95%e0%b8%a3%e0%b8%a7%e0%b8%88%e0%b8%ab%e0%b8%a7%e0%b8%a2%e0%b8%ae%e0%b8%b2%e0%b8%99%e0%b8%ad%e0%b8%a2/')
    bs = BeautifulSoup(req.content, 'html.parser')
    title = bs.find_all('strong')[1].get_text()
    date = bs.find_all('span')[15].get_text()[24:35]
    Four = bs.find_all('b')[3].get_text()
    Three = bs.find_all('b')[4].get_text()
    Two = bs.find_all('b')[5].get_text()

    data = ({'title':title, 'Four':Four, 'Three':Three, 'Two':Two, 'date':date})
    hannoi_lotto.objects.filter(data=data).update(**data)
    
hannoi_lotto_create()
if True:
    sleep(3)
    hannoi_lotto_update()

@shared_task
def hannoi_vip_create():
    print('Creating Hanoi VIP data...')
    req = requests.get('https://www.ruay.info/%e0%b8%95%e0%b8%a3%e0%b8%a7%e0%b8%88%e0%b8%ab%e0%b8%a7%e0%b8%a2%e0%b8%ae%e0%b8%b2%e0%b8%99%e0%b8%ad%e0%b8%a2vip/')
    bs = BeautifulSoup(req.content, 'html.parser')
    title = bs.find_all('strong')[1].get_text()
    date = bs.find_all('span')[15].get_text()[26:35]
    Four = bs.find_all('b')[0].get_text()
    Three = bs.find_all('b')[1].get_text()
    Two = bs.find_all('b')[2].get_text()

    data = ({'title': title, 'Four': Four, 'Three': Three, 'Two': Two, 'date': date})

    print(data)

    hannoi_vip.objects.create(
        title=title,
        Four=Four,
        Three=Three,
        Two=Two,
        date=date
    )
    print('Data have been create')
    sleep(3)
    
@shared_task
def hannoi_vip_update():
    print('Updating Hanoi VIP data...')
    req = requests.get('https://www.ruay.info/%e0%b8%95%e0%b8%a3%e0%b8%a7%e0%b8%88%e0%b8%ab%e0%b8%a7%e0%b8%a2%e0%b8%ae%e0%b8%b2%e0%b8%99%e0%b8%ad%e0%b8%a2vip/')
    bs = BeautifulSoup(req.content, 'html.parser')
    title = bs.find_all('strong')[1].get_text()
    date = bs.find_all('span')[15].get_text()[26:35]
    Four = bs.find_all('b')[0].get_text()
    Three = bs.find_all('b')[1].get_text()
    Two = bs.find_all('b')[2].get_text()

    data = ({'title':title, 'Four':Four, 'Three':Three, 'Two':Two, 'date':date})
    hannoi_vip.objects.all().update(**data)
    
hannoi_vip_create()
if True:
    sleep(3)
    hannoi_vip_update()

@shared_task
def hannoi_special_create():
    print('Creating Hanoi SPECIAL data...')
    req = requests.get('https://www.ruay.at/%E0%B8%95%E0%B8%A3%E0%B8%A7%E0%B8%88%E0%B8%AB%E0%B8%A7%E0%B8%A2%E0%B8%AE%E0%B8%B2%E0%B8%99%E0%B8%AD%E0%B8%A2%E0%B8%9E%E0%B8%B4%E0%B9%80%E0%B8%A8%E0%B8%A9/')
    bs = BeautifulSoup(req.content, 'html.parser')
    title = bs.find_all('strong')[1].get_text()
    date = bs.find_all('span')[6].get_text()[28:56]
    Four = bs.find_all('b')[0].get_text()
    Three = bs.find_all('b')[1].get_text()
    Two = bs.find_all('b')[2].get_text()

    data = ({'title': title, 'Four': Four, 'Three': Three, 'Two': Two, 'date': date})

    print(data)

    hannoi_special.objects.create(
        title=title,
        Four=Four,
        Three=Three,
        Two=Two,
        date=date
    )
    print('Data have been create')
    sleep(3)
    
@shared_task
def hannoi_special_update():
    print('Updating Hanoi SPECIAL data...')
    req = requests.get('https://www.ruay.at/%E0%B8%95%E0%B8%A3%E0%B8%A7%E0%B8%88%E0%B8%AB%E0%B8%A7%E0%B8%A2%E0%B8%AE%E0%B8%B2%E0%B8%99%E0%B8%AD%E0%B8%A2%E0%B8%9E%E0%B8%B4%E0%B9%80%E0%B8%A8%E0%B8%A9/')
    bs = BeautifulSoup(req.content, 'html.parser')
    title = bs.find_all('strong')[1].get_text()
    date = bs.find_all('span')[6].get_text()[28:56]
    Four = bs.find_all('b')[0].get_text()
    Three = bs.find_all('b')[1].get_text()
    Two = bs.find_all('b')[2].get_text()

    data = ({'title':title, 'Four':Four, 'Three':Three, 'Two':Two, 'date':date})
    hannoi_special.objects.all().update(**data)
    
hannoi_special_create()
if True:
    sleep(3)
    hannoi_special_update()
    
    