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

    newurl = 'http://www.99tvs.com'
    
    while True:

        url = newurl
        html = requests.get(url)
        messall = BeautifulSoup(html.text,"html.parser")
        mess = messall.find('div',class_="mainleft")
        mess = str(mess)
        urllist = re.findall(r'<h2><a href="(.*?)" rel',mess)
        #messlist = mess.findall('div',class_="article")
        #print url[0]
        for url in urllist:
            html = requests.get(url)
            messall = BeautifulSoup(html.text,"html.parser")
            mess = messall.find('div',class_="panel-body")
            mess = str(mess)
            text = re.findall(r'<a href="(.*?)" rel',mess)
            name = re.findall(r'>(.*?)</a>',mess)
            #name = str(name[0])
            print name[0]
            print text[0]
            with open('./text', 'a') as f:
                print(f.write(name[0]+'\r\n'))
                print(f.write(text[0]+'\r\n\r\n')) 
            
        mess = messall.find('div',class_="navigation container")  
        mess = str(mess)  
        newurl = re.findall(r'<a href=(.*?)" class="next">',mess)
        print newurl
        if newurl == 'http://www.99tvs.com/page/346':
            print "第一部分下载完成！"
            break
        #print newurl
    f.close()



if  __name__ == "__main__":
  
    t1=threading.Thread(target=downImg1,args=())
    t1.start()
 
