#coding=utf-8
import requests
import re
import os
import threading
 
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
http = 'https://www.602ff.com'
def downImg1():
   
    for page in range(1,45):
        url = http+'/htm/downlist1/'+str(page)+'.htm'
        #print url
        r=requests.get(url,headers=headers)
        r.encoding='utf-8'
        #print r.text.encode('utf-8')
        pattern=re.compile(r'<li><a href="(.*?)" target="_blank"><h3>(.*?)</h3><img src="(.*?)" /><p>',re.S)
        items=re.findall(pattern,r.text)
        #print items
        for item in items:
            #print item[0],item[1],item[2]
            imgname='./1/'+item[1]+'/'+item[1]+".jpg"
            dirname='./1/'+item[1]
            try:
                os.mkdir(dirname)
                imgr=requests.get(item[2],headers=headers)
        
        
                with open(imgname, "wb") as code:
                    code.write(imgr.content)
            except:
                print 'pass'
                continue
            url1=http+item[0]
            #print url1
            r1=requests.get(url1,headers=headers)
            #r1.encoding='utf-8'
            #print r1.text
            pattern1=re.compile(r'href="https.*?=(.*?)"',re.S)
            myitems=re.findall(pattern1,r1.text)
            #print myitems
            for myitem in myitems:
                pass
            url2='https://123456bt.com/download.php?ref='+myitem
            print myitem
            r2=requests.get(url2,headers=headers)
            name=dirname+'/'+myitem+'.torrent'
            try:
                with open(name, "wb") as code:
                    code.write(r2.content)
                    print u'finish write %s'%item[1]
            except:
                continue
def downImg2():
   
    for page in range(1,70):
        url = http+'/htm/downlist3/'+str(page)+'.htm'
        #print url
        r=requests.get(url,headers=headers)
        r.encoding='utf-8'
        #print r.text.encode('utf-8')
        pattern=re.compile(r'<li><a href="(.*?)" target="_blank"><h3>(.*?)</h3><img src="(.*?)" /><p>',re.S)
        items=re.findall(pattern,r.text)
        #print items
        for item in items:
            #print item[0],item[1],item[2]
            imgname='./2/'+item[1]+'/'+item[1]+".jpg"
            dirname='./2/'+item[1]
            try:
                os.mkdir(dirname)
                imgr=requests.get(item[2],headers=headers)            
        
                with open(imgname, "wb") as code:
                    code.write(imgr.content)
            except:
                continue     
            url1=http+item[0]
            #print url1
            r1=requests.get(url1,headers=headers)
            #r1.encoding='utf-8'
            #print r1.text
            pattern1=re.compile(r'href="https.*?=(.*?)"',re.S)
            myitems=re.findall(pattern1,r1.text)
            #print myitems
            for myitem in myitems:
                pass
            url2='https://123456bt.com/download.php?ref='+myitem
            
            r2=requests.get(url2,headers=headers)
            name=dirname+'/'+myitem+'.torrent'
            try:
                with open(name, "wb") as code:
                    code.write(r2.content)
                    print u'finish write %s'%item[1]
            except:
                continue
                
def downImg3():
   
    for page in range(1,64):
        url = http+'/htm/downlist4/'+str(page)+'.htm'
        #print url
        r=requests.get(url,headers=headers)
        r.encoding='utf-8'
        #print r.text.encode('utf-8')
        pattern=re.compile(r'<li><a href="(.*?)" target="_blank"><h3>(.*?)</h3><img src="(.*?)" /><p>',re.S)
        items=re.findall(pattern,r.text)
        #print items
        for item in items:
            #print item[0],item[1],item[2]
            imgname='./3/'+item[1]+'/'+item[1]+".jpg"
            dirname='./3/'+item[1]
            try:
                os.mkdir(dirname)
                imgr=requests.get(item[2],headers=headers)            
        
                with open(imgname, "wb") as code:
                    code.write(imgr.content)
            except IOError,e:
                continue
                 
            url1=http+item[0]
            #print url1
            r1=requests.get(url1,headers=headers)
            #r1.encoding='utf-8'
            #print r1.text
            pattern1=re.compile(r'href="https.*?=(.*?)"',re.S)
            myitems=re.findall(pattern1,r1.text)
            #print myitems
            for myitem in myitems:
                pass
            url2='https://123456bt.com/download.php?ref='+myitem
           
            r2=requests.get(url2,headers=headers)
            name=dirname+'/'+myitem+'.torrent'
            try:
                with open(name, "wb") as code:
                    code.write(r2.content)
                    print u'finish write %s'%item[1]
            except IOError,e:
                continue
 
if  __name__ == "__main__":
 
    for i in range(1,4):
        os.makedirs(str(i))
    t1=threading.Thread(target=downImg1,args=())
    t1.start()
 
    t2=threading.Thread(target=downImg2,args=())
    t2.start()
 
    t3=threading.Thread(target=downImg3,args=())
    t3.start()
