#!/usr/bin/python3.6

import pyorient

client = pyorient.OrientDB('localhost', 2424)
session_id = client.connect('root', 'root')

print('Opening the DB: Square')
client.db_open('Square', 'root', 'root')

print('Opening session: ' + str(session_id))

print('Cleaning all users:')
client.command('DELETE VERTEX User')

print('Cleaning all companies:')
client.command('DELETE VERTEX Company')

print('Cleaning all cities:')
client.command('DELETE VERTEX City')

print('Cleaning all Schools:')
client.command('DELETE VERTEX School')

print('Cleaning all ActivityAndDomain:')
client.command('DELETE VERTEX ActivityAndDomain')

print('Cleaning all Skills:')
client.command('DELETE VERTEX Skills')

print('Cleaning all Offer:')
client.command('DELETE VERTEX Offer')

print('Cleaning all Hobbies:')
client.command('DELETE VERTEX Hobbies')

print('Cleaning all Studied:')
client.command('DELETE EDGE Studied')

print('Cleaning all LivesIn:')
client.command('DELETE EDGE LivesIn')

print('Cleaning all Teach:')
client.command('DELETE EDGE Teach')

print('Cleaning all LocatesIn:')
client.command('DELETE EDGE LocatesIn')

print('Cleaning all WorksIn:')
client.command('DELETE EDGE WorksIn')

print('Cleaning all WorksFor:')
client.command('DELETE EDGE WorksFor')

print('Cleaning all ApplyFor:')
client.command('DELETE EDGE ApplyFor')

print('Cleaning all Master:')
client.command('DELETE EDGE Master')

print('Cleaning all CWorksIn:')
client.command('DELETE EDGE CWorksIn')

print('Cleaning all Require:')
client.command('DELETE EDGE Require')

print('Cleaning all Propose:')
client.command('DELETE EDGE Propose')

print('Cleaning all Practice:')
client.command('DELETE EDGE Practice')
