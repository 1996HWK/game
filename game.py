from urllib.request import urlretrieve,Request
import pygame
import time
import requests
from bs4 import BeautifulSoup
import os
from multiprocessing import Process
def GetIamg(url):
    PhotoName = []
    PhotoUrl=[]
    html=requests.get(url=url)
    html=BeautifulSoup(html.content,"lxml")
    print(html.select("article"))
        # print(a.find_all("a")[0].find("img").attrs["alt"])
        # PhotoName.append(a.find_all("a")[0].find("img").attrs["alt"])
        # PhotoUrl.append(a.find_all("a")[0].find("img").attrs["src"])
    return PhotoUrl,PhotoName
def SaveUrl(url):
    PhotoUrl, PhotoName=GetIamg(url)
    # if not os.path.exists('image'):
    #     os.makedirs('image')
    # for x in range(len(PhotoUrl)):
    #     try:
    #         pic = requests.get(PhotoUrl[x], timeout=5)  # 超时异常判断 5秒超时
    #     except requests.exceptions.ConnectionError:
    #         print('当前图片无法下载')
    #         continue
    #     file_name = "image\\"+PhotoName[x]+".jpg"  # 拼接图片名
    #     # 将图片存入本地
    #     fp = open(file_name, 'wb')
    #     fp.write(pic.content)  # 写入图片
    #     fp.close()
    #     time.sleep(1)
if __name__=="__main__":
    urls=["https://www.pexels.com/photo/sea-beach-water-wave-67385/","https://www.pexels.com/photo/group-of-people-raise-their-hands-on-stadium-976866/","https://www.pexels.com/photo/blur-close-up-female-field-583124/"]
    GetIamg(urls[0])
    print("获取结束")

