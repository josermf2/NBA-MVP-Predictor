import requests
import time
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
import time

years = range(1991,2024)

base_url = "https://www.basketball-reference.com/awards/awards_{}.html"

for year in years:
    url = base_url.format(year)
    data = requests.get(url)

    with open("mvps/{}.html".format(year), "w+") as f:
        f.write(data.text)
    
    print("Got mvps year {}".format(year))

    time.sleep(5)

team_stats_url = "https://www.basketball-reference.com/leagues/NBA_{}_standings.html"

for year in years:
    url = team_stats_url.format(year)

    data = requests.get(url)

    with open("teams/{}.html".format(year), "w+") as f:
        f.write(data.text)

    print("Got team stats year {}".format(year))

    time.sleep(5)

driver = webdriver.Firefox(options=options)

player_stats_url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html"

for year in years:
    url = player_stats_url.format(year)
    
    driver.get(url)
    driver.execute_script("window.scrollTo(1,10000)")
    
    with open("players/{}.html".format(year), "w+") as f:
        f.write(driver.page_source)
    
    time.sleep(10)
