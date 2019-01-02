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
            for data in source_list:
                if '_type' in data and data['_type'] == 'bond':
                    source = data
                    break
            if '_source' in source:
                raw = source['_source']
            else:
                return None
            if 'tagcode' in raw:
                print(search_info, raw['tagcode'])
                return raw['tagcode']
            else:
                print('invalid parse rule')
                return None
    except Exception as e:
        print("the reason of error is {}".format(e))

if __name__ == "__main__":
    search_info = "深圳前海联捷商业保理有限公司关于公开发行前海联捷2018年度第一期兴捷供应链应付账款资产支持票据"
    getWindCode(search_info)

