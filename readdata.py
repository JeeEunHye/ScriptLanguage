# -*- coding: cp949 -*-
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse

Data = None

def LoadXMLFromFile():
    global Data
    url = "http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEgytListInfoInqire?serviceKey=uiHZLqJ3xI1D%2B6DAcB5SF3mJL5rcFqCqo628wClXgoesJSMUUVqGPZJqgMiIzvErTq6%2BwQRFcr27%2BuVERdvuIQ%3D%3D&pageNo=1&startPage=1&numOfRows=408&pageSize=408"
    savename = 'data.xml'

    data = urllib.request.urlopen(url).read()
    text = data.decode('utf-8')

    req.urlretrieve(url, savename)

    xml = open(savename, "r", encoding="utf-8").read()
    Data = BeautifulSoup(xml, "html.parser")
    return Data

def PrintDataList():
    global Data
    for location in Data.find_all("item"):
        print("기관명     : ", location.dutyname.string)
        print("주소       : ", location.dutyaddr.string)
        print("분류명     : ", location.dutyemclsname.string)
        print("분류       : ", location.dutyemcls.string)
        print("대표전화   : ", location.dutytel1.string)
        try:
            print("응급전화   : ", location.dutytel3.string)
        except:
            print("")

        print("")
        print("")

def SearchDataName(keyword):
    global Data
    for location in Data.find_all("item"):
        if keyword in location.dutyname.string:
            print("기관명     : ", location.dutyname.string)
            print("주소       : ", location.dutyaddr.string)
            print("분류명     : ", location.dutyemclsname.string)
            print("분류       : ", location.dutyemcls.string)
            print("대표전화   : ", location.dutytel1.text)
            try:
                print("응급전화   : ", location.dutytel3.string)
            except:
                print("")
            print("")
            print("")

def SearchDataAddress(keyword):
    global Data
    for location in Data.find_all("item"):
        if keyword in location.dutyaddr.string:
            print("기관명     : ", location.dutyname.string)
            print("주소       : ", location.dutyaddr.string)
            print("분류명     : ", location.dutyemclsname.string)
            print("분류       : ", location.dutyemcls.string)
            print("대표전화   : ", location.dutytel1.text)
            try:
                print("응급전화   : ", location.dutytel3.string)
            except:
                print("")
            print("")
            print("")