import requests
from bs4 import BeautifulSoup

# 특정 URL에 접속하는 요청(Request) 객체를 생성합니다.
codes = ['005930','006400','000720','005380']
header = {'User-agent' : 'Mozila/2.0'}   #in case of request aborted
for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    request = requests.get(url, headers=header)
   
    
    html = request.text
    # HTML 소스코드를 파이썬 BeatifulSoup 객체로 변환합니다.
    soup = BeautifulSoup(html, 'html.parser')
    #title = soup.select_one('.lnk_hdline_article')
    price = soup.select_one('#_nowVal').text  # price= string
    price = price.replace(',','')
    print(price)

    