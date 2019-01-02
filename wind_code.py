#!/usr/bin/python3
#-*- coding:utf-8 -*-
import requests
import json


#获取wind代码
def getWindCode(search_info):
    url = 'http://125.215.147.40/WindSearch/WindSearch/handler/SearchHandler.ashx'
    header = {
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/605.1.15 (KHTML, like Gecko)',
        'content-type':'application/json;charset=utf-8'
    }
    paramters = {
        'index':'newsearchresult',
        'version':'1',
        'pageindex':'1',
        'pageNum':'25',
        'key':search_info,
        'dimension':'',
        'mtype':'',
        'type':'-2',
        'newsflg':'0',
        'btflg':'-1',
        'rtflg':'0',
        'userTypes':'',
        'range':'0',
        'sp':'title',
        'wind.sessionid':'6fa0c0e5acbd43038876f0a286fa8ab6', # you should change the session_id when the response code is not 200
        'fileds':'title,windcode,spell,fullspell,tagcode,areacode,keyword,content,abstract',
        'sort':'_score desc,publishdate desc',
        'suggest':'0',
        'suggestfields':'title,windcode,spell,fullspell,tagcode,areacode,section,keyword,author,content',
        'd':'205641',
        'rppright':'1'
    }

    html = requests.get(url=url,params=paramters,headers=header)
    try:
        first_res = json.loads(html.text.strip())
        second_res = json.loads(first_res['dataor'])
        source_list = second_res['hits']['hits']
        if len(source_list) > 0:
            source = source_list[0]
            raw = source['_source']
            print(search_info, raw['tagcode'])
            return raw['tagcode']
    except Exception as e:
        print("the reason of error is {}".format(e))

if __name__ == "__main__":
    search_info = "福建省晋江城市建设投资开发集团有限责任公司2017年度第三期永续票据"
    getWindCode(search_info)

