# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Create a text/plain message
msg = MIMEText('text')

me = ''
you = ''
msg['Subject'] = 'subject'
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP()
s.connect('smtp.gmail.com', 587)
s.ehlo()
s.starttls() # start tls encryption, call ehlo afterwards
s.ehlo()
s.login(username, password)
s.sendmail(me, you, msg.as_string())
s.quit()
