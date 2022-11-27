import requests
from bs4 import BeautifulSoup

header = {'User-agent' : 'Mozila/2.0'}
request = requests.get('http://www.naver.com', headers = header)
#in case of request aborted

# 접속한 이후의 웹 사이트 소스코드를 추출합니다.
html = request.text
# HTML 소스코드를 파이썬 BeatifulSoup 객체로 변환합니다.
#soup = BeautifulSoup(html, 'html.parser')
soup = BeautifulSoup(html, 'lxml')
#title = soup.select_one('.lnk_hdline_article')
# sh_title = soup.select_one('div.shop_title').text 
#print(sh_title)
#sh_items = soup.select_one('.goodsItem_z01003')
#gr_item = soup.select_one('div.group_event')
#class가 event_item인 li tag  li.event_item
#items = soup.select('div#show_wrap div#contents div.group_event ul.list_event li.event_item')
items = soup.select('div.group_event ul.list_event li.event_item')
#items = soup.select_one('ul.list_event')

print('shop item = ', len(items))
for item in items:
    shop = item.select_one('a em.title').text
    print(shop)

#data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
#items = soup.find("ul",attrs={"class":"list_event"}).get_text()
#item = soup.find("em",attrs={"class":"title"}).get_text()
# items = soup.find("ul", attrs={"class":"list_event}).find_all("li")
#     for row in items:
#         columns = row.find("em").get_text()               
#         print(columns)
        
        
# data_results.append(data)

# price = price.replace(',','')
# print(price)

    