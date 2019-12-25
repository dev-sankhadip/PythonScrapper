import requests
from bs4 import BeautifulSoup
import time


def crawl():
    URL = "https://www.chitkara.edu.in/"

    page = requests.get(URL)

    soup = BeautifulSoup(page.content,'html.parser')

    # save scrapped data to a html file
    file=open('scrape.html','w')
    file.write(str(soup))
    file.close()

    # start scrapping the page
    # print webpage title
    print(soup.title.string)

    # get any tag content by id
    print(soup.find(id='menu-item-29072').string)

    # get all div tag and print them usng for loop
    div_tags=soup.find_all('div')
    for div_tag in div_tags:
            print(div_tag)

    # get all a tag and print their href attr value
    a_tags=soup.find_all('a')
    for a_tag in a_tags:
        print(a_tag.get('href'))

    # get parent element of any tag
    tags=soup.find_all('a')
    for tag in tags:
        print("Parent is ",tag.find_parent())

crawl()