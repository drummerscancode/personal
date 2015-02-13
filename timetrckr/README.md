$ brew install sleepwatcher  
Follow instructions for launchptd...  
$ chmod 755 <path_to_script>  
$ /usr/local/sbin/sleepwatcher -s|-w ". <path_to_script>" & 

### TODO
* Remove the -n that gets printed maybe with printf instead of echo
* Set it up in login/logout, sleep/wake. Check if restart works as well.
