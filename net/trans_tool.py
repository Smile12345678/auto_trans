#/usr/bin/env python
#coding=utf8
import http.client
import hashlib
import urllib
import random
import json

appid = '20151113000005349'
secretKey = 'osubCEzlGjzvw8qdQc41'

def transLanguage(q, fromLang, toLang):
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = q
    fromLang = fromLang
    toLang = toLang
    salt = random.randint(32768, 65536)

    sign = appid+q+str(salt)+secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode())
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        #response是HTTPResponse对象
        response = httpClient.getresponse()
        temp = response.read().decode()
        js = json.loads(temp)
        return js["trans_result"][0]["dst"]
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()

def transToZh(q):
    temp = transLanguage(q, "auto", "zh")
    return temp

def transToEn(q):
    temp = transLanguage(q, "auto", "en")
    return temp

def transToJp(q):
    temp = transLanguage(q, "auto", "jp")
    return temp