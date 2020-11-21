import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

msg = MIMEMultipart()

inf = '{"Login": "motriy981@ukr.net", "pass": "5bWIrJijDegEKbHx", "Text": "Hello friend", "topic": "Привітання", "Users": "dimonpokemonxd@gmail.com"}'
startInformation = json.loads(inf)

password = startInformation["pass"]
message = startInformation["Text"]
msg['Subject'] = startInformation["topic"]
msg['From'] = startInformation["Login"]
msg['To'] = startInformation["Users"]

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP_SSL('smtp.ukr.net', 465)
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

print("successfully sent email to %s:" % (msg['To']))




