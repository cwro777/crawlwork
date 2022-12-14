import requests
from bs4 import BeautifulSoup
import csv

def finance():
    
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?&page="

    
    title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
   

    for page in range(1,5):
        res = requests.get(url + str(page))
        res.raise_for_status
        soup = BeautifulSoup(res.text, "lxml")
        
        data_results = []
        try:
            data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
            for row in data_rows:
                columns = row.find_all("td")
                if len(columns) <= 1 :
                    continue
                data = [column.get_text().strip() for column in columns]
                print(data)
                data_results.append(data)
             
                print(data_results)
        except IndexError:
            pass
        return data_results
    
kospi = finance()

print('주식수=', len(kospi))
print(kospi)

        