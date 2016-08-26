import urllib2
import simplejson

url = "https://api.twitter.com/1.1/search/tweets.json"

if __name__ == "__main__":
    req = urllib2.Request(url)
    opener = urllib2.build-opener()
    f = opener.open(req)
    json = simplejson.load(f)