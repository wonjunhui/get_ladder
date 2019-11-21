from selenium import webdriver
import pandas as pd
import time
from bs4 import BeautifulSoup
import csv
# import pymysql
# import config

def get_data(event, context):

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    # options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    # 혹은 options.add_argument("--disable-gpu")
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

    driver = webdriver.Chrome('./chromedriver-2', options=options)

    driver.get('http://ntry.com/scores/named_ladder/main.php')
    driver.implicitly_wait(3)

    a=1
    try:
        while True:
            driver.find_element_by_xpath('//*[@id="more-btn"]').click()
            time.sleep(0.5)
            print('click '+ str(a))
            a = a+1
    except Exception as e:
        print('end')
    # //*[@id="stats-list"]
    table = driver.find_element_by_xpath('//*[@id="round-history"]')
    print(table)
    body = table.find_elements_by_css_selector('tr')
    arr = []
    for a in body:
        arr.append(a.text.split('\n')[0])
        # print('--------')
    # 날짜/회차	시간	시작	줄수	결과
    # .tsv 쓰기
    f = open('test.csv', 'a', encoding='utf8', newline='')
    wr = csv.writer(f, delimiter=',')
    wr.writerow(['날짜','회차','시간','시작','줄수','결과'])
    for d in arr:
        g = d.split(' ')
        date = [b for b in g[0]]
        wr.writerow(['-'.join((g[0].split('-'))[0:3]),g[0].split('-')[3],g[1],g[2],g[3],g[4]])
    f.close()
except Exception as e:
    print(str(e))
    driver.quit()




def get_df():
    df = pd.read_csv('test.csv')
    # print(df)
    st = df['날짜/회차'][0]
    ar = (st.split('-'))
    print('-'.join(ar[0:3]))
    print(ar[3])
    # df[df['날짜/회차'] == ]

def insert_ladder(DATE,COUNT,TIME,START_POINT,LINE,RESULT):
    db = pymysql.connect(host=config.DATABASE_CONFIG_LADDER['host'], port=config.DATABASE_CONFIG_LADDER['port'], user=config.DATABASE_CONFIG_LADDER['user'], passwd=config.DATABASE_CONFIG_LADDER['password'], db=config.DATABASE_CONFIG_LADDER['dbname'], charset=config.DATABASE_CONFIG_LADDER['charset'])
    curs = db.cursor()
    sql = """insert into LADDER_INFO(DATE,COUNT,TIME,START_POINT,LINE,RESULT) values(%s,%s,%s,NOW())"""
    curs.execute(sql,(DATE,COUNT,TIME,START_POINT,LINE,RESULT))
    # print(URI)
    db.commit()
    db.close()



if __name__ == '__main__':
    get_data('','')
    # get_df()