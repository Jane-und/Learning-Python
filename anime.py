from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import sqlite3
import xlwt


def main():
    baseurl = "https://www.agefans.vip/"

    datalist = getData(baseurl)
    savepath = "anime.xls"

    saveData(datalist, savepath)


def getData(baseurl):
    datalist = []
    html = askURL(baseurl)
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('a'):
        print(item)
    return datalist




def askURL(url):
    head = {  
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/..."
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


def saveData(datalist, savepath):
    print("save...")


if __name__ == "__main__": 
    main()
  

