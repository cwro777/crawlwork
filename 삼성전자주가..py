import requests
from bs4 import BeautifulSoup

# 특정 URL에 접속하는 요청(Request) 객체를 생성합니다.
request = requests.get('https://finance.naver.com/item/sise.naver?code=006400')
#in case of request aborted
# header = {'User-agent' : 'Mozila/2.0'}
# request = requests.get('http://www.naver.com', headers = header)
# 접속한 이후의 웹 사이트 소스코드를 추출합니다.
html = request.text
# HTML 소스코드를 파이썬 BeatifulSoup 객체로 변환합니다.
soup = BeautifulSoup(html, 'html.parser')
#title = soup.select_one('.lnk_hdline_article')
price = soup.select_one('#_nowVal').text  # price= string
print(price)
price = price.replace(',','')
print(price)

    