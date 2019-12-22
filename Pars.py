import requests
import datetime
from bs4 import BeautifulSoup

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrodiv78.0.3904.70 Safari/537.36'}

def get_html(url):
    if url:
        r = requests.get(url, headers=headers)
        html = r.text
        return html

def parser_football(html):
    data_matches_online= []
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('div', class_='matches-list')
    matches = table.find_all('a', class_='matches-list-match')
    for i in range(len(matches)):
        match = matches[i].find('div', class_='match-details')
        time = match.find('span', class_='match-time-time')
        date = match.find('span', class_='match-time-date')
        time = str(time.text).strip()
        date = str(date.text).strip()
        teams = match.find('span', class_='match-title')
        team1 = teams.find('span', class_='team team1')
        team2 = teams.find('span', class_='team team2')
        team1 = str(team1.text).strip()
        team2 = str(team2.text).strip()
        tour = matches[i].find('span', class_='match-cat')
        tour = str(tour.text).strip()
        date = time + ' ' + date
        date = datetime.datetime.strptime(date, '%H:%M %d.%m.%Y')
        data_matches_online.append([team1, team2, date, time, tour])
    return data_matches_online


def parser_basketball(html):
    data_matches_online = []
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('div', class_='matches-list')
    matches = table.find_all('a', class_='matches-list-match')
    for i in range(len(matches)):
        match = matches[i].find('div', class_='match-details')
        time = match.find('span', class_='match-time-time')
        date = match.find('span', class_='match-time-date')
        time = str(time.text).strip()
        date = str(date.text).strip()
        teams = match.find('span', class_='match-title')
        team1 = teams.find('span', class_='team team1')
        team2 = teams.find('span', class_='team team2')
        team1 = str(team1.text).strip()
        team2 = str(team2.text).strip()
        date = time + ' ' + date
        date = datetime.datetime.strptime(date, '%H:%M %d.%m.%Y')
        data_matches_online.append([time, date, team1, team2])
    return (data_matches_online)


def get_football():
    url = 'https://www.liveresult.ru/football/England/Premier-League/scheduled/'
    data = parser_football(get_html(url))
    return data

def get_basketball():
    url = 'https://www.liveresult.ru/basketball/Euroleague/results/'
    data = parser_basketball(get_html(url))
    return data
