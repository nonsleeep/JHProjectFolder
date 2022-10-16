import requests
from bs4 import BeautifulSoup

base_url ="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="

keyword = input("순위가 궁금한 유럽리그를 입력하세요.")

search_url = base_url + keyword + "순위"
r = requests.get(search_url)
# requests 모듈의 get 함수 --> url 주소의 페이지를 서버에 요청하여 응답받고 --> 이를 r에 정보를 저장

# .text에 html 소스가 담겨있음
soup = BeautifulSoup(r.text, "html.parser")

# items = soup.select("#teamRankTabPanel_0 > div > div.scroll > table > tbody > tr:nth-child(1)")
# select에서는 .이 class 정보를 가져옴, 중간에 존재하는 빈칸도 .으로 채워주기!!
# 한 개만 찾을 때는 select_one사용, 전부 찾을때는 select

for i in range(10) :
    tags = soup.select("#teamRankTabPanel_0 > div > div.scroll > table > tbody > tr:nth-child("+str(i)+")")
    for item in tags :
        print("순위    팀 이름  경기 수/승점/승/무/패/득점/실점/득실차  ")
        print(f"{item.text}")
