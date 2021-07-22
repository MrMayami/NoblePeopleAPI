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
    mLiveRadioDB = json.dumps(mData)
    

    return mLiveRadioDB



def catSearching(mLink):
    catArray = []
    try:
        cats = mLink.find_all('a', {"rel":"category tag"})
        cat = ''.join(cats.findAll(text=True))
        for cat in cats:
            catArray.append(cat)
    except requests.exceptions.Timeout:
        print("Connection Timeout.... Trying again....")
        cats = mLink.find('a', {"rel":"category tag"})
        catArray.append(cat)
    except requests.exceptions.TooManyRedirects:
        print("Too many Redirects...")
    except requests.exceptions.RequestException as e:
        print(e)
        raise SystemExit(e)
    except requests.exceptions.HTTPError as err:
        print(err)
        raise SystemExit(err)
    except requests.exceptions.ConnectionError:
        pass

    return catArray

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
    

    return mLiveTVDB

def LiveUpComing():
    req = requests.get('https://noblepeople.co.uk/show-schedule/', headers={'User-Agent': 'Chrome', 'Accept-Encoding': 'identity', 'Content-Type': 'text/html'})
    soup = BeautifulSoup(req.text, 'html5lib')
    mAllLink = soup.find_all('div', {"class":"qt-part-archive-item"})
    # print(mAllLink)
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

    mLiveUpComing = json.dumps(mData)
    

    return mLiveUpComing

def mArticle(url):
    req = requests.get(url, headers={'User-Agent': 'Chrome', 'Accept-Encoding': 'identity', 'Content-Type': 'text/html'})
    soup = BeautifulSoup(req.text, 'html5lib')
    mArticles = soup.find_all('div', {"dir":"auto"})
    
    resArray = []
    for mArticle in mArticles:
        res = ''.join(mArticle.findAll(text=True))
        resArray.append(res)

    return resArray

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
        article = mArticle(articleLink)
        # print(article)
        mData = {
            "cat" : cat.contents[0],
            "title" : title,
            "img" : img,
            "date" : date,
            "author" : author,
            "articleWebLink" : articleLink,
            "article" : article
            }

        mDataArray.append(mData)
    
    mMagDB = json.dumps(mDataArray)
    

    return mMagDB

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
        article = mArticle(articleLink)
        # print(article)
        mData = {
            "cat" : cat.contents[0],
            "title" : title,
            "img" : img,
            "date" : date,
            "author" : author,
            "articleWebLink" : articleLink,
            "article" : article
            }

        mDataArray.append(mData)
    mNewsDB = json.dumps(mDataArray)
    
    return mNewsDB

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