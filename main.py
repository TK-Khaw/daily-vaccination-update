from importlib import import_module
import pkgutil
import os
import sys
import csv
import requests

# Comma-separated flag to enable and disable analysers and distributors.
DVU_ANALYSERS=os.environ.get('DVU_ANALYSERS', '').split(',')
DVU_DISTRIBUTORS=os.environ.get('DVU_DISTRIBUTORS', '').split(',')

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
    if '' in DVU_ANALYSERS or name in DVU_ANALYSERS:
        msg_body = msg_body + import_module('analyser.' + name).compute(my_fifo)
        msg_body = msg_body + '\n'
        msg_body = msg_body + '\n'

print(msg_body)

for _,name,_ in pkgutil.walk_packages(path=[
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'distributor'
    )
    ]):
    if '' in DVU_DISTRIBUTORS or name in DVU_DISTRIBUTORS:
        import_module('distributor.' + name).distribute(msg_body)

print('Done')
