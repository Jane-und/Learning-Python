from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import sqlite3
import xlwt


def main():
    baseurl = "https://www.agefans.vip/"

    datalist = getData(baseurl)
    savepath = "/Users/jiangxujie/Desktop/MAPPA.xls"

    saveData(datalist, savepath)


def getData(baseurl):
    datalist = []
    html = askURL(baseurl)
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('a'):
        print(item)
    return datalist




def askURL(url):
    head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36"
    }
    # 用户代理表示告诉豆瓣服务器我们是什么类型的浏览器，本质上是告诉浏览器我们可以接收什么水平的文件内容
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


if __name__ == "__main__":  # 当程序执行时
    main()
    # 调用函数
    # print("爬取完毕")
