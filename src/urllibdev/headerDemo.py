#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Joseph
@email:liseor@gmail.com
Created on 2012-7-14
'''
import urllib2
import socket
import cookielib
import mimetypes
socket.setdefaulttimeout(7)

class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        pass
    def http_error_302(self, req, fp, code, msg, headers):
        pass

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
    
    opener = urllib2.build_opener(httpHandler,cookieHandler,RedirectHandler)
    
    #install global urllib2
    urllib2.install_opener(opener)
    try:
        url = "http://127.0.0.1/session.php"
        request = urllib2.Request(url)
        request.add_header('User-Agent', 'fake-client')
        request.add_header('Content-Type', 'application/html')
        request.add_header('Accept', 'application/html')
        request.get_method = lambda: 'GET' # or 'DELETE'
        res = urllib2.urlopen(request,timeout=1)        
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
        print res.read(20)
        print "*"*40
        print res.info()
        print "*"*40
        print res.geturl()
        print res.code
        for row in cj:
            print row.name,row.value
        cj.save(cjFile,ignore_discard=True, ignore_expires=True)