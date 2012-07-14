#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Joseph
@email:liseor@gmail.com
Created on 2012-7-15
'''
import urllib2
import socket
import cookielib
import mimetypes
socket.setdefaulttimeout(7)

def uploadfile(fields, files):
    BOUNDARY = '----------267402204411258'
    CRLF = '\r\n'
    L = []
    for (key, value) in fields:
        print key
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"' % key)
        L.append('')
        L.append(value)
    for (key, filename, value) in files:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename))
        L.append('Content-Type: %s' % mimetypes.guess_type(filename)[0] or 'application/octet-stream')
        L.append('')
        L.append(value)
        
    L.append('--' + BOUNDARY + '--')
    L.append('')
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    return content_type, body


if __name__ == '__main__':    
    cjFile = 'cookie.txt'
    cj = cookielib.MozillaCookieJar(cjFile)
    
    try:
        cj.load(ignore_discard=True, ignore_expires=True)
    except Exception as what:
        print what
        cj.save(cjFile,ignore_discard=True, ignore_expires=True)
        
    cookieHandler = urllib2.HTTPCookieProcessor(cj)
    httpHandler = urllib2.HTTPHandler(debuglevel =1)
    
    opener = urllib2.build_opener(httpHandler,cookieHandler)
    
    #install global urllib2
    urllib2.install_opener(opener)
    try:
        url = "http://127.0.0.1/session.php"
        
        ifile = "test.gif"
        imgdata= file(ifile,"rb")
        files=[
               ('file[]',imgdata.name,imgdata.read()),
               ('file[]',imgdata.name,imgdata.read())               
               ]
        
        fields =[('test','eee')]
        
        content_type, upload_data = uploadfile(fields, files)
        
        Header={
                "User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",                
                }
        request = urllib2.Request(url,upload_data,Header)
        
        request.add_header('Content-Type', content_type)
        request.add_header('Content-Length', str(len(upload_data)))
                           
        request.get_method = lambda: 'POST' # or 'DELETE'
        res = urllib2.urlopen(request,timeout=5)        
    except urllib2.HTTPError as e:
        print e
        print e.code
        print e.read()
        print e.info()
    except urllib2.URLError as e:
        print e
        print e.reason      
    except Exception as what:
        pass
        print what
    else:
        print "*"*40
        print res.read()
        print "*"*40
        print res.info()
        print "*"*40
        print res.geturl()
        print res.code
        for row in cj:
            print row.name,row.value
        cj.save(cjFile,ignore_discard=True, ignore_expires=True)