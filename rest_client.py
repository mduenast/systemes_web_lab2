#!/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding-utf8 :

import sys
import urllib2
from bs4 import BeautifulSoup

api_key = None
class WeatherClient(object):
    """
        docstring for WeatherClient
    """
    url_base = "http://api.wunderground.com/api/"
    url_service = {"almanac" : "/almanac/q/CA/"}
    def __init__(self,api_key):
        super(WeatherClient,self).__init__()
        self.api_key = api_key

    def almanac(self,location):
        # baixar-se la pagina web
        #"http://api.wunderground.com/api/53f287832b555a2e/almanac/q/CA/Madrid.json"
        url = WeatherClient.url_base + self.api_key + \
         WeatherClient.url_service["almanac"] + location + ".xml"
        f = urllib2.urlopen(url)
        response = f.read()
        f.close()
        # llegir-la
        soup = BeautifulSoup(response,"lxml")
        maximes = soup.find("temp_high")
        normal= maximes.find("normal").find("c").text
        record = maximes.find("record").find("c").text

        minimes = soup.find("temp_low")
        normal2= minimes.find("normal").find("c").text
        record2 = minimes.find("record").find("c").text

        # retornar els resultats
        return {"maximes" : (int(normal),int(record) ), \
        "minimes" : ( int(normal2), int(record2) ) }

if __name__ == "__main__":
    if not api_key:
        try:
            api_key = sys.argv[1]
        except IndexError:
            print "Api Key must be in CLI option"
    wc = WeatherClient(api_key)
    resultat = wc.almanac("Lleida")
    print resultat
