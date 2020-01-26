from bs4 import BeautifulSoup
import requests
def get_url(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.content, "html.parser")
    return soup

url = "https://search.daum.net/search?w=social&m=web&sort_type=socialweb&nil_search=btn&DA=NTB&enc=utf8&q=감자"
soup = get_url(url)
div_list = soup.findAll("div",{"class":"box_con"})
for list in div_list:
    title = list.find("div",{"class":"wrap_tit"}).text
    print(title)