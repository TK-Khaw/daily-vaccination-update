import smtplib, ssl
import os

# Mail service.

EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_PORT = os.environ['EMAIL_PORT']
EMAIL_TLS = os.environ['EMAIL_TLS']
EMAIL_USERNAME = os.environ['EMAIL_USERNAME']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']

#Note, comma-separated list of mails.
EMAIL_RECIPIENT = os.environ['EMAIL_RECIPIENT'].split(',')

def distribute(msg_body):
    try:
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        if EMAIL_TLS == 'True':
            server.starttls(context=ssl.create_default_context())
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)

        for rep in EMAIL_RECIPIENT:
            buf = "From: {}\r\nTo:\r\n".format(EMAIL_USERNAME, rep) 
            buf += "Subject: MALAYSIAN VACCINATION PROGRESS\r\n\r\n"
            buf += msg_body

            server.sendmail(EMAIL_USERNAME, rep, buf)

    except Exception as ex:
        print('Can\'t connect to SMTP server')
        exit()
    finally:
        server.quit()

