import smtplib

sender = "OpenoceanRPI@gmail.com"
recipient = "Jamiesonjfregeau@gmail.com"
password = "Openocean2019"
subject = "Water Detected"
text = """\

Hello from your autonomous boat,

there has been water detected inside my hull.

I'm slowly sinking. 

Cheers
"""

smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
smtp_server.login(sender, password)
message = "Subject: {}\n\n{}".format(subject, text)
smtp_server.sendmail(sender, recipient, message)
smtp_server.close()




