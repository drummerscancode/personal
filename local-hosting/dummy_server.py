#! /usr/bin/python
from twisted.web import server, resource
from twisted.internet import reactor
import subprocess
import sys
import os
import signal

"""
    Usage: python server.py
    Dependencies: 
        youtube-dl (upgrade to the latest with $ youtube-dl -U)
        omxplayer       
"""
print 'welcome'

class HelloResource(resource.Resource):
    def __init__(self):
        print "created new index page"
        resource.Resource.__init__(self)
    
    def render_GET(self, request):
        print 'inside get'  
        return "<html>INDEX PAGE</html>"

class Main(resource.Resource):
    def getChild(self, name, request):
        print "trying to get main"
        return HelloResource()  

root = Main()
site = server.Site(root)
reactor.listenTCP(8080, site)
reactor.run()


