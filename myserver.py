"""This is a small webserver that will handle GET requests


This implements GET (not POST) as well as translate txt files into Spanish 
"""
__author__ =  'Eli Katz'
__version__=  '6.9'


import time
import BaseHTTPServer
import os
from urllib2 import urlopen
from urllib import urlencode
import sys

CONFIG_FILE = 'config.txt'
HOST_NAME = ''
ROOT = ''
 
class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """Handler responds to various server requests. This only implements GET
    I borrowed part of this code from the python.org tutorial on 
    GET requests
    """
    def do_GET(self):
        """GET request"""
        try:
            #We do not care for asp and neither should you!
            if (self.path.endswith(".html") or self.path.endswith(".php")):
                """First if looks for a file with html or php following"""
                self.send_response(200)
                f = open(ROOT + self.path)
                self.wfile.write(f.read())
                file.close()    
            elif self.path.endswith(".txt"):
                """Otherwise we look for a text file to translate"""
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write("<h1>This is translated to Spanish</h1><br>")
                f = open(ROOT + self.path)
                for line in f:
                    self.wfile.write(translate(line) + "<br>")
                f.close() 
            else:
                """Last attempt would be to find an index.html file"""
                self.send_response(200)
                f = open(ROOT + self.path + "index.html") 
                self.wfile.write(f.read())
                f.close()
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)
            
def translate(line):
    """Splits the sentence into words which is easier to translate"""
    words = line.split(' ')
    sentence = ""
    for word in words:
        sentence = sentence +  " " +  perWord(word)
    return sentence
            
def perWord(line):
    """This function was borrowed from a Google API Tutorial
        It can be modified to translate to any language that google supports
        Keep in mind that after 3-4 tries Google will block you from using the service
        Probably because I make the call by word instead of entire file.
    """
    lang1= 'en'
    lang2= 'es'
    langpair='%s|%s'%(lang1,lang2)
    text=' '.join(line)
    base_url='http://ajax.googleapis.com/ajax/services/language/translate?'
    params=urlencode( (('v',1.0),
                       ('q',text),
                       ('langpair',langpair),) )
    url=base_url+params
    content=urlopen(url).read()
    start_idx=content.find('"translatedText":"')+18
    translation=content[start_idx:]
    end_idx=translation.find('"}, "')
    translation=translation[:end_idx]
    return translation
                          
def main():
    """The main function opens the config file to read in a root and port"""
    try:
        f = open(CONFIG_FILE, 'r')
        global ROOT 
        ROOT = f.readline().rstrip('\n')
        PORT = int(f.readline().rstrip('\n'))
        server_class = BaseHTTPServer.HTTPServer
        httpd = server_class((HOST_NAME, PORT), MyHandler)
        print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.socket.close()
            print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT)
    except:
        print "File Not Found Error"               
    
if __name__ == '__main__':
    main()
