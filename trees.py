import requests
import flask
import time
import os
from bs4 import BeautifulSoup
def getTotal():
    res = requests.get('https://teamtrees.org/')
    dec = res.content.decode()
    soup = BeautifulSoup(dec,'html.parser')
    total_tag = soup.find_all('div', attrs={'id': 'totalTrees'})
    total = total_tag[0]['data-count']
    treesLeft = (20000000 - int(total))
    return total, treesLeft
def getName():
    theirName = ""
    res = requests.get('https://teamtrees.org/')
    dec = res.content.decode()
    soup = BeautifulSoup(dec, 'html.parser')
    name_tag = soup.find_all('strong', attrs={'class':""}) #media-body pb-3 mb-0 border-bottom border-gray
    name = name_tag[1]
    for each in name:
        theirName += str(each)
    return theirName
def getAmount(): #!!!!!!!!!!THIS CAN GET BACKED UP AND SHOW A AMOUNT FOR THE PERSON BELOW
    theirAmount = ""
    res = requests.get("https://teamtrees.org/")
    dec = res.content.decode()
    soup = BeautifulSoup(dec, 'html.parser')
    amount_tag = soup.find_all('span', attrs={'class':'feed-tree-count badge badge-tier-1 text-uppercase'})
    amount = amount_tag[0]
    for each in amount:
        theirAmount += each
    return theirAmount
def getDescription():
    theirDescription = ""
    res = requests.get("https://teamtrees.org/")
    dec = res.content.decode()
    soup = BeautifulSoup(dec, 'html.parser')
    description_tag = soup.find_all('span', attrs={'class':'d-block medium mb-0'})
    description = description_tag[0]
    for each in description:
        theirDescription += each
    if theirDescription == "":
        theirDescription += "They had no description"
    return theirDescription

while True:
    os.system('cls')
    print("They have planted a total of {} trees\nthey need {} more trees to reach their goal of 20 million!\nTheir latest donation was from {} and he donated {} with the description {}!".format(getTotal()[0],getTotal()[1],getName(),getAmount(),getDescription()))
    time.sleep(5)
