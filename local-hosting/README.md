# Local hosting with dynamic DNS

* Port forwarding on your router
* Test with the provided dummy\_server.py  
canyouseeme.org 
* Create an account for dynamic dns - I chose no-ip since it's the (only?) with a free tier and I am a cheap bastard  
DynDns: 25$ per year, free 2-week trial but requires credit card  
EasyDns: supports authentication tokens instead of password
* Use a client for dynamic dns: ```$ brew install ddclient``` and follow the instructions for launchctl (change conf file name).  
I used the no-ip client as I don't like having the password in plain text on the confif file.  
(didn't find any option for auth token or ssh key)

