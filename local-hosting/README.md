# Local hosting from Mac with dynamic DND

* Port forwarding on your router
* Test with the provided dummy\_server.py
  canyouseeme.org
* Create an account for dynamic dns - I choose no-ip since it's the (only?) with a free tier
  DynDns: 25$ per year, free 2-week trial but requires credit card
  EasyDns: supports authentication tokens instead of password
* Use ddclient with the conf file provided: $ brew install ddclient and follow the instructions for launchctl (change conf file name).
  I use the no-ip client as I don't like having the password in plain text on the conf.
  (didn't find an option for auth token or ssh key)
* Enjoy


## Security Considerations
* (At least) open a non-standard port on your router
* Whitelist certain IPs only.
  Very static: access from phone?
* MAC filters work only for local network.

External hosting more secure?

