import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage

strFrom = 'nadjituan@gmail.com'
strTo = 'riyomossiba@gmail.com'
cc= 'arezki.m.nadji96@gmail.com'
# Create the root message 

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'test message'
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
msgRoot['Cc'] =cc
msgRoot.preamble = 'Multi-part message in MIME format.'

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('Alternative plain text message.')
msgAlternative.attach(msgText)

msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>KPI-DATA!', 'html')
msgAlternative.attach(msgText)

#Attach Image 
fp = open('foo.jpg', 'rb') #Read image 
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

import smtplib
smtp = smtplib.SMTP('smtp.gmail.com',587)
smtp.ehlo()
smtp.starttls()
smtp.ehlo()
smtp.login('nadjituan@gmail.com', 'NadjiTuanParis8') #Username and Password of Account
smtp.sendmail(strFrom, strTo, msgRoot.as_string())
smtp.quit()
