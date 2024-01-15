import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "justin.bigishiro@gmail.com"
password = "bdawhctskdlajzfk"

receiver = "justin.rvd@gmail.com"
my_context = ssl.create_default_context()

message = """\
Subject: Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=my_context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
