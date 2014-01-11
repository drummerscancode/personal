#! /usr/bin/python
from twisted.web import server, resource
from twisted.internet import reactor
import subprocess
import sys
import os
import signal

class HelloResource(resource.Resource):
	"""
	mplayer -cookies -cookies-file /tmp/cookie.txt $(youtube-dl -g --cookies /tmp/cookie.txt "http://www.youtube.com/watch?v=kww0WXcH74o")
	"""   
	isLeaf = True
	yt_dl = {} #
	player = {} #
	base_url = 'http://www.youtube.com/watch?v='
    
	def render_GET(self, request):
		""" copy the play_url method from __init__.py
		"""
		print(request.args)
		param = request.args['v'][0]
		request.setHeader("content-type", "text/plain")

		while self.player and self.player.poll() == None:
			print('killing previous video')
			os.killpg(self.player.pid, signal.SIGTERM)
			print(self.player.poll())
	
		self.yt_dl = subprocess.Popen(['youtube-dl', '-g', self.base_url + param], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
		(yt_url, err) = self.yt_dl.communicate()
		if self.yt_dl.returncode != 0:
			return('Something\'s wrong with the retrieval of the url ' + sys.stderr.write(err))
			#raise RuntimeError('Error getting URL ' + param)
		
		self.player = subprocess.Popen(
            ['omxplayer','-ohdmi', yt_url.decode('UTF-8').strip()],
            stdout = subprocess.PIPE, stderr = subprocess.PIPE, preexec_fn=os.setsid)

		print(self.player.poll())
		return "I play " + param + "\n"
	

reactor.listenTCP(8080, server.Site(HelloResource()))
reactor.run()


