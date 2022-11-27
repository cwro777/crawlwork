import requests
from bs4 import BeautifulSoup

# 특정 URL에 접속하는 요청(Request) 객체를 생성합니다.
request = requests.get('https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90')
#in case of request aborted
# header = {'User-agent' : 'Mozila/2.0'}
# request = requests.get('http://www.naver.com', headers = header)
# 접속한 이후의 웹 사이트 소스코드를 추출합니다.
html = request.text
# HTML 소스코드를 파이썬 BeatifulSoup 객체로 변환합니다.
soup = BeautifulSoup(html, 'html.parser')
#title = soup.select_one('.lnk_hdline_article')
titles = soup.select('.news_tit') # id=#, class = .
#print(titles) # title list
for title in titles:
    s_title = title.get_text()
    url = title.attrs['href']
    print(s_title, url, '\n')
    

# trip()) #strip 빈공간 제거
#news = soup.select('.cjs_news_a_cds_link_editn_link')
# news = soup.find_all('div', attrs={'class': 'cjs_t'})

# print(news.get_text.strip())
# for new in news:
    
#     links = new.findAll()

#news = soup.find("p",attrs={"class":"cjs_news_a_cds_link_editn_link"}).get_text()
#print(news.text.strip())
subjects = []
# <a> 태그를 포함하는 요소를 추출합니다.
#links = soup.select('td > a')
#cast = soup.find("p",attrs={"class":"summary"}).get_text()
#div = soup.find('div',attrs={"clss": "shop_title"}).get_text() 
#print(div)
# lis = soup.findAll('li', {"clss": "event_item"})
# for li in lis:
#     links = li.findAll('em')
    
#     for link in links:
#         subject = link.text
#         subjects.append(subject)
#         print("em")
#         print(subject)
        
#cast = soup.find("p",attrs={"class":"summary"}).get_text()
#links = soup.select('em.title').get_text()
#print(div)


