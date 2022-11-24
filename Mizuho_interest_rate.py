from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
import csv

driver = webdriver.Chrome('C:/WebDriver/bin/chromedriver_win32 (5)/chromedriver.exe')
target_url = 'https://www.mizuhobank.co.jp/rate_fee/rate_interest.html'
driver.get(target_url)  
sleep(10)
print('動作確認')
html = driver.page_source

mat = [] 
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', {'class':'type1 js-market'}).tbody

# 外貨名のリスト
r_list = []
ths = table.select('th')
for th in ths: 
    r_list.append(th.text)  

# 金利のリスト
url_list = []
tds = table.select('td')
for td in tds: 
    url_list.append(td.text)  

df_title_url = pd.DataFrame({'Title':r_list, 'URL':url_list})
print(df_title_url)

df_title_url.to_csv('Mizuho_csv.csv',encoding='shift jis')


# elems = soup.select('.type1 js-market thead')

# rows = table.find_all('tr')
# for row in rows:
#     print(row.th)  # 外貨名
#     print(row.td)  # 金利

# tableタグを絞り込んでからではなく一気に絞り込もうと思ったら…
# elems = soup.select('tbody')  
#   結果  すべての（他のtableも含む）tbody　
# elems = soup.select('th[class="tbgGray02 noBorderL left"]') 
# 　結果　[<th class="tbgGray02 noBorderL left" headers="th1 th2"></th>, 
#         <th class="tbgGray02 noBorderL left" headers="th1 th2"></th>, 
#         <th class="tbgGray02 noBorderL left" headers="th1 th2"></th>]
# elems = soup.select('[class="tbgGray02 noBorderL left"]')
#   結果　[<th class="tbgGray02 noBorderL left" headers="th1 th2"></th>, 
#         <th class="tbgGray02 noBorderL left" headers="th1 th2"></th>, 
#         <th class="tbgGray02 noBorderL left" headers="th1 th2"></th>]
# elems = soup.select('th[headers="th1 th2"]')
#   結果　[<th class="tbgGray02 noBorderL left" headers="th1 th2"></th>, 
#         <th class="tbgGray02 noBorderL left" headers="th1 th2"></th>, 
#         <th class="tbgGray02 noBorderL left" headers="th1 th2"></th>] 
# elems = soup.select('[headers="th1 th2"]')  結果[]