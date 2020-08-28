

from flask import Flask
from flask import jsonify
from flask import request
import json
import requests

from flask_cors import CORS
app = Flask(__name__)
CORS(app)
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


@app.route("/dfor",methods=['GET'])
def D4mail():
    email=request.args.get("email")
    message=request.args.get("message")
    
    subject="Client Message"
    body=message
    receiver="services@dfordevelopers.com"
    recipient = receiver.split(",")
    sender = 'services@dfordevelopers.com'
    msg = MIMEText("Message text")
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    html = body
    html_part = MIMEText(html, 'html')
    msg.attach(html_part)

    server = smtplib.SMTP_SSL('smtpout.asia.secureserver.net', 465)
    server.login(sender, 'Password123!')
    server.sendmail(sender, recipient, msg.as_string())
    server.quit()
    
    ## message to the client
    subject="We Got Your Response"
    body="We will contact you  shortly : D4Developers.com"
    receiver=email
    recipient = receiver.split(",")
    sender = 'services@dfordevelopers.com'
    msg = MIMEText("Message text")
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    html = body
    html_part = MIMEText(html, 'html')
    msg.attach(html_part)

    server = smtplib.SMTP_SSL('smtpout.asia.secureserver.net', 465)
    server.login(sender, 'Password123!')
    server.sendmail(sender, recipient, msg.as_string())
    server.quit()

    response={"response":"Success"}

    return jsonify(response)


@app.route("/boxsides",methods=['GET'])
def boxsidesMail():
    response={}
    email=request.args.get("email")
    message=request.args.get("message")
    
    subject="Client Message"
    body=message
    receiver='vikas.r.kumar.9@gmail.com'
    recipient = receiver.split(",")
    sender = 'vikas@boxsides.com'
    msg = MIMEText("Message text")
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    html = body
    html_part = MIMEText(html, 'html')
    msg.attach(html_part)

    server = smtplib.SMTP_SSL('smtp.zoho.com',465)
    server.login(sender, 'dBD4xEJWxuzG')
    server.sendmail(sender, recipient, msg.as_string())
    server.quit()
    
    ## message to the client
    subject="We Got Your Response"
    body="We will contact you  shortly : D4Developers.com"
    receiver=email
    recipient = receiver.split(",")
    sender = 'vikas@boxsides.com'
    msg = MIMEText("Message text")
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    html = body
    html_part = MIMEText(html, 'html')
    msg.attach(html_part)

    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)
    server.login(sender, 'dBD4xEJWxuzG')
    server.sendmail(sender, recipient, msg.as_string())
    server.quit()

    response={"response":"Success"}

    return jsonify(response)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)   



