from importlib import import_module
import pkgutil
import os
import sys
import csv
import requests

SMS_URL = 'https://api.twilio.com/2010-04-01/Accounts/'
SMS_SID = os.environ['SMS_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
SENDER_NO = os.environ['SENDER_NO']
PHONE_NO = os.environ['PHONE_NO'] 

VAC_MY = os.environ['CITF_DIR'] + '/vaccination/vax_malaysia.csv'
ENTRIES_NO = 100

def populate_fifo(filename):
    fifo = [{} for i in range(ENTRIES_NO)]
    with open(filename, 'r') as f:
        for row in csv.DictReader(f):
            fifo.append(row)
            fifo.pop(0)
    return fifo

if len(sys.argv) != 2:
    print('ERROR: Wrong number of arguments!')
    exit()

msg_body = '\n' 
msg_body += sys.argv[1]
msg_body += '\n' 
msg_body += '\n' 

my_fifo = populate_fifo(VAC_MY) 

for _,name,_ in pkgutil.walk_packages(path=[
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'analyser'
    )
    ]):
    msg_body = msg_body + import_module('analyser.' + name).compute(my_fifo)
    msg_body = msg_body + '\n'
    msg_body = msg_body + '\n'

print(msg_body)

request_body = {
    "From" : SENDER_NO,
    "To" : PHONE_NO,
    "Body" : msg_body
}

response = requests.post(
    ''.join([
        SMS_URL,
        SMS_SID,
        '/Messages.json'
    ]),
    auth = (
        SMS_SID,
        AUTH_TOKEN
    ),
    data = request_body
)

print(response.status_code)
print(response.text)
