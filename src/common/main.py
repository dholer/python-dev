#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Joseph
@email:liseor@gmail.com
Created on 2012-7-15
'''
import re
import sys
import hashlib
import os
import time
import base64

def checkPath(f2,var):
    f1 = os.getcwd()
    hash = hashlib.md5(var).hexdigest().upper() #@UndefinedVariable
    h1 = str(hash[0:2])+"\\"
    h2 = str(hash[2:4])+"\\"
    h3 = str(hash[4:6])+"\\"
    h4 = str(hash[6:])+"\\"
    path = f1+"\\"+f2+"\\"+h1+h2+h3+h4
    if os.path.isdir(path):
        return True
    else:
        return False
    
def makePath(f2,var):
    f1 = os.getcwd()
    hash = hashlib.md5(var).hexdigest().upper() #@UndefinedVariable
    h1 = str(hash[0:2])+"\\"
    h2 = str(hash[2:4])+"\\"
    h3 = str(hash[4:6])+"\\"
    h4 = str(hash[6:])+"\\"
    path = f1+"\\"+f2+"\\"+h1+h2+h3+h4
    if not os.path.isdir(path):
        os.makedirs(path)
def removePath(f2,var):
    f1 = os.getcwd()
    #print f1
    hash = hashlib.md5(var).hexdigest().upper() #@UndefinedVariable
    h1 = str(hash[0:2])+"\\"
    h2 = str(hash[2:4])+"\\"
    h3 = str(hash[4:6])+"\\"
    h4 = str(hash[6:])
    path = f1+"\\"+f2+"\\"+h1+h2+h3+h4
#    print path
    if os.path.isdir(path):
        os.rmdir(path)
def regx_data(regx,html,default,d= False,clean=False,rep=''):
    #print regx
    if re.search(regx, html):
        
        data = re.search(regx, html).group(1)
        if clean:
            print rep
            data = re.sub(clean,rep,data)
        if d:
            print regx
            print data
        return data
    else:
        if d:
            print regx
            print "没有"
        return default
def regx_datas(regx,html,default,d= False,clean=False,rep=''):
    #print regx
    if re.findall(regx, html):
        
        _data = re.findall(regx, html)        
        data = ''
        for r in _data:
           data = "%s|%s" % (r,data)
        if clean:
            data = re.sub(clean,rep,data)
        if d:
            print data   
        return data
    else:             
        return default
    
def regx_datas1(regx,html,default,d= False,clean=False,rep=''):
    #print regx
    if re.findall(regx, html):        
        data = re.findall(regx, html)     
        if d:
            print data   
        return data
    else:             
        return default
def regx_lists(regx,html,default,d= False,clean=False,rep=''):
    #print regx
    if re.findall(regx, html):
        
        _data = re.findall(regx, html)
        
        data = _data
        
        if clean:
            data = re.sub(clean,rep,data)
        if d:
            print data   
        return data
    else:             
        return default
def delete_file_folder(src):
    '''delete files and folders'''
    if os.path.isfile(src):
        try:
            os.remove(src)
        except:
            pass
    elif os.path.isdir(src):
        for item in os.listdir(src):
            itemsrc=os.path.join(src,item)
            delete_file_folder(itemsrc) 
        try:
            os.rmdir(src)
        except:
            pass
#===============================================================================
# .显示被存储为Base64编码字符串的图片的例子 
#1)使用data: URI直接在网页中嵌入. 
#data: URI定义于IETF标准的RFC 2397 
#data: URI的基本使用格式如下： 
#data:[<MIME-type>][;base64|charset=some_charset],<data> 
#mime-type是嵌入数据的mime类型，比如png图片就是image/png。 
#如果后面跟base64，说明后面的data是采用base64方式进行编码的
#data:image/gif;base64,
#===============================================================================
def base64en(s):
     r = base64.b64encode(s)
     return r
def base64de(s):
     r = base64.b64decode(s)
     return r


if __name__ == "__main__":
    import urllib2
    url = "http://img1.baixing.net/m/02bf752c651863cc9dba7be59ab258f5.jpg"
    res=urllib2.urlopen(url)
    data=res.read()
    print base64en(data)
    