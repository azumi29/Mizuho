import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import datetime	

r = requests.get('https://www.mizuhobank.co.jp/rate_fee/rate_interest.html')
mat = [] 
soup = BeautifulSoup(r.content, 'html.parser')
# table = soup.select_one('table[summary="外貨普通預金金利・為替相場"]')
table = soup.find('table', {'class':'type1 js-market'}).tbody
#   結果　<tbody>
#　　　  <tr>
#        <th class="tbgGray02 noBorderL left" headers="th1 th2"></th>
#        <td class="alnRight" headers="th1 th2"></td>
#        </tr>
#        </tbody>

print(table)

# r_list = []
# tbody = table.select('tbody')
# tbs = tbody.tr.select('th')


# theadの解析
# r = []  # 保存先の行
# thead = table.find('thead')  # theadタグを探す
# ths = thead.tr.find_all('th')
# for th in ths:  # thead -> trからthタグを探す
    # r.append(th.text)  # thタグのテキストを保存

# url_list = []
# for i in elems:
#     elem_list.append(i.text)
#     url_list.append(i.attrs['href'])

# df_title_url = pd.DataFrame({'Title':elem_list, 'URL':url_list})
# print(df_title_url)

# df_title_url.to_csv('Qiita_csv03.csv',encoding='shift jis')


# elems = soup.select('.type1 js-market thead')

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