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

    newurl = 'https://m.xinshubao.net/12/12710/1017376.html'
    f = open('./text1','a')
    while True:

        url = newurl
        html = requests.get(url)
        messall = BeautifulSoup(html.text,"html.parser")
        mess = messall.find('div',id='nr_title')
        f.write(mess.text)
        mess = messall.find('div',id='nr1')
        f.write(mess.text)
    
        messa = messall.find('a',text='下一章')
        messa = str(messa)
        messa = messa.replace('\n', '')
        url = re.findall(r'<a href="(.*?)">',messa)
        newurl = url[0]
        if newurl == 'https://m.xinshubao.net/12/12710/10309272.html':
            print "第一部分下载完成！"
            break
        print newurl
    f.close()

def downImg2():

    newurl = 'https://m.xinshubao.net/12/12710/10309272.html'
    f = open('./text2','a')
    while True:

        url = newurl
        html = requests.get(url)
        messall = BeautifulSoup(html.text,"html.parser")
        mess = messall.find('div',id='nr_title')
        f.write(mess.text)
        mess = messall.find('div',id='nr1')
        f.write(mess.text)
    
        messa = messall.find('a',text='下一章')
        messa = str(messa)
        messa = messa.replace('\n', '')
        url = re.findall(r'<a href="(.*?)">',messa)
        newurl = url[0]
        if newurl == 'https://m.xinshubao.net/shuku/0/monthvisit-0-1.html':
            print "全部下载完成！"
            break
        print newurl
    f.close()

if  __name__ == "__main__":
  
    t1=threading.Thread(target=downImg1,args=())
    t1.start()
 
    t2=threading.Thread(target=downImg2,args=())
    t2.start()
    
 
