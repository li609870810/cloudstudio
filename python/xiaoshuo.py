#coding=utf-8
import requests
from bs4 import BeautifulSoup
import os
from multiprocessing import Pool
import sys
import re
import threading

reload(sys)
sys.setdefaultencoding( "utf-8" )

def downImg1():

    newurl = 'http://www.bxwx3.org/txt/52/789886.htm'
    f = open('./text1','a')
    while True:

        url = newurl
        html = requests.get(url)
        messall = BeautifulSoup(html.text,"html.parser")
        mess = messall.find('div',class_="bookname")
        #print mess
        f.write(mess.text)
        mess = messall.find('div',id='zjneirong')
        #print mess
        f.write(mess.text)

        mess = messall.find('div',class_='bottem2')
        mess = str(mess)
        #print mess
        url = re.findall(r'<a href="(.*?)" id="A3">',mess)
        #<a href="http://www.bxwx3.org/txt/52/2455.htm" id="A3">
        #messa = mess.find('a',id='xiaye')
        #newurl = messa.href
        newurl = url[0]
        if newurl == 'http://www.bxwx3.org/txt/52/2912.htm':
            print "第一部分下载完成！"
            break
        print newurl
    f.close()

def downImg2():

    newurl = 'http://www.bxwx3.org/txt/52/2912.htm'
    f = open('./text2','a')
    while True:

        url = newurl
        html = requests.get(url)
        messall = BeautifulSoup(html.text,"html.parser")
        mess = messall.find('div',class_="bookname")
        #print mess
        f.write(mess.text)
        mess = messall.find('div',id='zjneirong')
        #print mess
        f.write(mess.text)

        mess = messall.find('div',class_='bottem2')
        mess = str(mess)
        #print mess
        url = re.findall(r'<a href="(.*?)" id="A3">',mess)
        #<a href="http://www.bxwx3.org/txt/52/2455.htm" id="A3">
        #messa = mess.find('a',id='xiaye')
        #newurl = messa.href
        newurl = url[0]
        if newurl == 'https://www.bxwx3.org/txt/52/3438.htm':
            print "全部下载完成！"
            break
        print newurl
    f.close()

def downImg3():

    newurl = 'http://www.bxwx3.org/txt/52/3438.htm'
    f = open('./text3','a')
    while True:

        url = newurl
        html = requests.get(url)
        messall = BeautifulSoup(html.text,"html.parser")
        mess = messall.find('div',class_="bookname")
        #print mess
        f.write(mess.text)
        mess = messall.find('div',id='zjneirong')
        #print mess
        f.write(mess.text)

        mess = messall.find('div',class_='bottem2')
        mess = str(mess)
        #print mess
        url = re.findall(r'<a href="(.*?)" id="A3">',mess)
        #<a href="http://www.bxwx3.org/txt/52/2455.htm" id="A3">
        #messa = mess.find('a',id='xiaye')
        #newurl = messa.href
        newurl = url[0]
        if newurl == 'https://www.bxwx3.org/txt/52/3777.htm':
            print "全部下载完成！"
            break
        print newurl
    f.close()

if  __name__ == "__main__":
  
    t1=threading.Thread(target=downImg1,args=())
    t1.start()
 
    t2=threading.Thread(target=downImg2,args=())
    t2.start()

    t3=threading.Thread(target=downImg3,args=())
    t3.start()
 
