#! /usr/bin/python
from twisted.web import server, resource
from twisted.internet import reactor
import subprocess
import sys
import os
import signal

"""
Usage: python server.py
"""

port = 8080
print 'welcome to dummy'


class TestResource(resource.Resource):
    def __init__(self):
        print "created new index page"
        resource.Resource.__init__(self)
    
    def render_GET(self, request):
        print 'inside get'  
        return "<html>INDEX PAGE</html>"


class Main(resource.Resource):
    def getChild(self, name, request):
        return TestResource()  


root = Main()
site = server.Site(root)
reactor.listenTCP(port, site)
reactor.run()

