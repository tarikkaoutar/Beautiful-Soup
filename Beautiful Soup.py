from bs4 import BeautifulSoup
import requests
import pandas as pd
titles = []
locations = []
prices = []
Areas = []
Rooms = []
for page in range(1,20):
    # https://www.pararius.com/apartments/amsterdam/page-4
    URL = f"https://www.pararius.com/apartments/amsterdam/page-{page}"
    # print(URL)
    reslut = requests.get(URL)
    page = reslut.text
    # print(page)
    soup = BeautifulSoup(page,'lxml') 
    # print(soup.prettify())
    # title_name , Location_name , Price , Area , Rooms 
    title_name = soup.find_all('h2',class_="listing-search-item__title")
    Location_name = soup.find_all('div',class_="listing-search-item__sub-title")
    Price = soup.find_all('div',class_="listing-search-item__price")
    Area_name = soup.find_all('li',class_="illustrated-features__item illustrated-features__item--surface-area")
    Room_name = soup.find_all('li',class_="illustrated-features__item illustrated-features__item--number-of-rooms")
    # for loop
    for i in range(len(title_name)):
        titles.append(title_name[i].text.replace('\n', ''))
        locations.append(Location_name[i].text.replace('\n', ''))
        prices.append(Price[i].text.replace('\n', ''))
        Areas.append(Area_name[i].text.replace('\n', ''))
        Rooms.append(Room_name[i].text.replace('\n', ''))
    #file 
    housing_list = pd.DataFrame({"title":titles,"location":locations,"price":prices,"area":Areas,"rooms":Rooms})
    print(housing_list)
    housing_list.to_csv('housing.csv')



