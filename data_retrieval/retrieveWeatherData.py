#!/usr/bin/python
import re
import argparse
import urllib2
from bs4 import BeautifulSoup

def getData(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, "lxml")

    temp = soup.find("div", class_="report_text temperature")
    temp = str(temp)
    temp = re.findall(r"\-?\d+", temp)

    skies = soup.find("div", class_="report_text light_text")
    skies = str(skies.string)

    wind = soup.find("div", class_="col-md-7 col-xs-6")
    wind = str(wind)
    start = wind.find("Wind")+6
    end = start+2
    wind=wind[start:end]

    text = soup.find("div", class_="weather_forecastdiv marbot")
    text = str(text.find("p"))
    text = BeautifulSoup(text, "lxml").text

    print "Short forecast: ", skies
    print "Temperature (Celsius): ", temp[0]
    print "Wind speed (mph): ", wind
    print "Long forecast: ", text


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("city", help="name of the city to get weather data for")
    args = parser.parse_args()

    city = args.city

    cities = \
    {
        'London':'https://www.worldweatheronline.com/london-weather-text/city-of-london-greater-london/gb.aspx',
        'Melbourne':'https://www.worldweatheronline.com/melbourne-weather-text/victoria/au.aspx',
        'Miami':'https://www.worldweatheronline.com/miami-weather-text/florida/us.aspx',
        'Moscow':'https://www.worldweatheronline.com/moscow-weather-text/moscow-city/ru.aspx',
        'NewYork':'https://www.worldweatheronline.com/new-york-weather-text/new-york/us.aspx',
        'Rio':'https://www.worldweatheronline.com/rio-weather-text/rio-de-janeiro/br.aspx',
        'SanFran':'https://www.worldweatheronline.com/san-francisco-weather-text/california/us.aspx',
        'Toronto':'https://www.worldweatheronline.com/toronto-weather-text/ontario/ca.aspx',
        'Trondheim':'https://www.worldweatheronline.com/trondheim-weather-text/sor-trondelag/no.aspx'
    }
    url = cities.get(city)

    getData(url)
