from bs4.element import SoupStrainer
from flask import Flask, json, jsonify
from flask_restful import Resource, Api
from bs4 import BeautifulSoup
import requests
import lxml
import html5lib
import time


app = Flask(__name__)
api = Api(app)

def LiveRadio():
    req = requests.get('https://noblepeople.co.uk/live-radio/', headers={'User-Agent': 'Chrome', 'Accept-Encoding': 'identity', 'Content-Type': 'text/html'})
    soup = BeautifulSoup(req.text, 'html5lib')
    mAllLink = soup.find_all('a')
    for mLink in mAllLink:
        mLiveRadioURL = mLink.get('data-playtrack')
        if mLiveRadioURL != None:
            mData = {
                "streaming" : mLiveRadioURL.strip(),
                "title" : mLink.get('data-title'),
                "img" : mLink.get('data-background'),
                "host" : "Noble People",
                "station" : "Noble FM"
            }

    return jsonify(mData)

def LiveTV():
    req = requests.get('https://noblepeople.co.uk/noble-tv/', headers={'User-Agent': 'Chrome', 'Accept-Encoding': 'identity', 'Content-Type': 'text/html'})
    soup = BeautifulSoup(req.text, 'html5lib')
    mAllLink = soup.find_all('iframe')
    for mLink in mAllLink:
        mLiveTVURL = mLink.get('src')
        if mLiveTVURL != None:
            mData = {
                "streaming" : mLiveTVURL,
                "title" : "You're watching Noble People TV"
            }
    mLiveTVDB = json.dumps(mData)
    

    return jsonify(mData)

def LiveUpComing():
    req = requests.get('https://noblepeople.co.uk/show-schedule/', headers={'User-Agent': 'Chrome', 'Accept-Encoding': 'identity', 'Content-Type': 'text/html'})
    soup = BeautifulSoup(req.text, 'html5lib')
    mAllLink = soup.find_all('div', {"class":"qt-part-archive-item"})
    # print(mAllLink)
    mDataArray = []
    for mLink in mAllLink:
        title = mLink.find("a", {"class":"qt-text-shadow"})
        if title != None:
            mTitle = title.contents[0]
        date = mLink.find("h5", {"class":"qt-time"})
        if date != None:
            mDate = date.contents[0]
        sponsor = mLink.find("p", {"class":"qt-small qt-ellipsis"})
        if sponsor != None:
            mSponsor = sponsor.contents[0]
        img = mLink.find("div", {"class":"qt-header-bg"})
        if img != None:
            mImg = img["data-bgimage"]

        mData = {
            "title" : mTitle,
            "date" : mDate,
            "sponsor" : mSponsor,
            "img" : mImg
            }
        mDataArray.append(mData)

    return jsonify(mDataArray)   

def LiveMag():
    req = requests.get('https://noblepeople.co.uk/magazine/', headers={'User-Agent': 'Chrome', 'Accept-Encoding': 'identity', 'Content-Type': 'text/html'})
    soup = BeautifulSoup(req.text, 'html5lib')
    mAllLink = soup.find_all('div', {"class": "qt-part-archive-item qt-vertical"})
    # print(mAllLink)
    mDataArray = []
    for mLink in mAllLink:
        # print(mLink)
        cat = mLink.a
        cat['class'] = "qt-catid-7"
        # print(cat.contents[0])
        img = mLink.find("div", {"class":"qt-header-bg"})['data-bgimage']
        # print(img)
        title = mLink.find("a", {"class":"qt-text-shadow"}).contents[0]
        # print(title)
        date =  mLink.find("p", {"class":"qt-date"}).contents[0]
        # print(date)
        author = mLink.find("a", {"rel":"author"}).contents[0]
        # print(author)
        articleLink = mLink.find("a", {"class":"qt-text-shadow"})['href']
        
        # print(article)
        mData = {
            "cat" : cat.contents[0].strip(),
            "title" : title.strip(),
            "img" : img,
            "date" : date,
            "author" : author,
            "articleWebLink" : articleLink
            }

        mDataArray.append(mData)


    return jsonify(mDataArray)

def LiveNews():
    req = requests.get('https://noblepeople.co.uk/news/', headers={'User-Agent': 'Chrome', 'Accept-Encoding': 'identity', 'Content-Type': 'text/html'})
    soup = BeautifulSoup(req.text, 'html5lib')

    mAllLink = soup.find_all('div', {"class": "qt-part-archive-item"})
    # print(mAllLink)
    mDataArray = []
    
    for mLink in mAllLink:
        # print(mLink)
        cat = mLink.a
        cat['rel'] = "category tag"
        # print(cat.contents[0])
        img = mLink.find("div", {"class":"qt-header-bg"})['data-bgimage']
        # print(img)
        title = mLink.find("a", {"class":"qt-text-shadow"}).contents[0]
        # print(title)
        date =  mLink.find("p", {"class":"qt-date"}).contents[0]
        # print(date)
        author = mLink.find("a", {"rel":"author"}).contents[0]
        # print(author)
        articleLink = mLink.find("a", {"class":"qt-text-shadow"})['href']
        
        # Format data
        mCat = cat.contents[0]
        mTitle = title.strip()
        mImg = img.strip()
        mDate = date.strip()
        mAuthor = author.strip()
        mArticleWebLink = articleLink.strip()
        

        mData = {
            "cat" : mCat,
            "title" : mTitle,
            "img" : mImg,
            "date" : mDate,
            "author" : mAuthor,
            "articleWebLink" : mArticleWebLink,
            }

        mDataArray.append(mData)
    
    return jsonify(mDataArray)

class Mag(Resource):
    def get(self):
        res = LiveMag()

        return res

class Upcoming(Resource):
    def get(self):
        res = LiveUpComing()

        return res

class News(Resource):
    def get(self):
        res = LiveNews()

        return res

class TV(Resource):
    def get(self):
        res = LiveTV()

        return res

class Radio(Resource):
    def get(self):
        res = LiveRadio()

        return res

api.add_resource(Radio, '/radio')
api.add_resource(TV, '/tv')
api.add_resource(Mag, '/magazine')
api.add_resource(News, '/news')
api.add_resource(Upcoming, '/upcoming')