# -*- coding:utf-8 -*-
#   Description: ---
#        Author: Lynn
#         Email: lgang219@gmail.com
#        Create: 2018-10-05 18:12:37
# Last Modified: 2018-10-05 18:20:51
#

import requests
import json
import pymysql

def get_update():
    json_tmp = json.loads(get_html())
    conn = pymysql.connect('127.0.0.1', port=3306, user='root', password='cqmygpython2', db='bdpan', charset='utf8')
    cursor = conn.cursor()

    for i in json_tmp['movies']:
        try:
            cursor.execute(i)
            conn.commit()
        except:
            conn.rollback()
    cursor.close()
    conn.close()

def get_html():
    url = 'http://120.79.170.122/getmovie'
    html_text = ''
    try:
        r = requests.get(url)
        html_text = r.text
    except:
        html_text = ''
    return html_text

def main():
    get_update()

main()