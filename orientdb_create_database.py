#!/usr/bin/python3.6

import pyorient
from datetime import datetime

client = pyorient.OrientDB('localhost', 2424)
session_id = client.connect('root', 'root')

print('Opening the DB: Square')
client.db_open('Square', 'root', 'root')

print('Opening session: ' + str(session_id))

###################################USER CREATION###################################

print('Create the user \'John\', \'Doe\' with its date of birth set as now')
client.command('INSERT INTO User SET FirstName = \'John\', LastName = \'Doe\', DateOfBirth = \'2018-04-09\', InsertionDate = \'2018-04-09\'')

print('Create the user \'Foo\', \'Bar\', with its date of birth set as now')
client.command('INSERT INTO User SET FirstName = \'Foo\', LastName = \'Bar\', DateOfBirth = \'2018-04-09\', InsertionDate = \'2018-04-09\'')

print('Create the user \'Tom\', \'mmy\', with its date of birth set as now')
client.command('INSERT INTO User SET FirstName = \'Tom\', LastName = \'mmy\', DateOfBirth = \'2018-04-09\', InsertionDate = \'2018-04-09\'')

###################################COMPANY CREATION###################################

print('Create company ApplyStartup which is a website to apply for a job with its siret containing 1234567890 and its siren containing 0987654321')
client.command('INSERT INTO Company SET Name = \'ApplyStartup\', NameLowercase = \'applystartup\', Siret = \'1234567890\', Siren = \'0987654321\', InsertionDate = \'2018-04-09\', Description = \'AH ! UNE MURENNE\'')

print('Create company Epitech which is a website to apply for a job with its siret containing 1234567890 and its siren containing 0987654321')
client.command('INSERT INTO Company SET Name = \'Epitech\', NameLowercase = \'epitech\', Siret = \'1234567890\', Siren = \'0987654321\', InsertionDate = \'2018-04-09\', Description = \'AH ! UNE MURENNE\'')

###################################OFFER CREATION###################################

print('Create the offer lead dev for ApplyStartup')
client.command('INSERT INTO Offer SET Name = \'Lead dev\', NameLowercase = \'lead dev\', Description = \'AH ! UNE MURENNE\', GrossWage = 2000, InsertionDate = \'2018-04-09\'')

print('Create the offer Business dev for ApplyStartup')
client.command('INSERT INTO Offer SET Name = \'Business Developper\', NameLowercase = \'business developper\', Description = \'AH ! UNE MURENNE\', GrossWage = 2000, InsertionDate = \'2018-04-09\'')

print('Create the offer dpr from Epitech')
client.command('INSERT INTO Offer SET Name = \'DPR\', NameLowercase = \'dpr\', Description = \'AH ! UNE MURENNE\', GrossWage = 2000, InsertionDate = \'2018-04-09\'')

###################################HOBBIES CREATION###################################

print('Create the Hobby football')
client.command('INSERT INTO Hobbies SET Name = \'Football\', NameLowercase = \'football\', InsertionDate = \'2018-04-09\'')

print('Create the Hobby basketball')
client.command('INSERT INTO Hobbies SET Name = \'Basketball\', NameLowercase = \'basketball\', InsertionDate = \'2018-04-09\'')

print('Create the Hobby baseball')
client.command('INSERT INTO Hobbies SET Name = \'Baseball\', NameLowercase = \'baseball\', InsertionDate = \'2018-04-09\'')

print('Create the Hobby golf')
client.command('INSERT INTO Hobbies SET Name = \'Golf\', NameLowercase = \'golf\', InsertionDate = \'2018-04-09\'')

###################################SCHOOLS CREATION###########################

print('Create the School Epitech')
client.command('INSERT INTO School SET Name = \'Epitech\', NameLowercase = \'epitech\', InsertionDate = \'2018-04-09\'')

print('Create the School Enac')
client.command('INSERT INTO School SET Name = \'Enac\', NameLowercase = \'enac\', InsertionDate = \'2018-04-09\'')

print('Create the School Ipsa')
client.command('INSERT INTO School SET Name = \'Ipsa\', NameLowercase = \'ipsa\', InsertionDate = \'2018-04-09\'')

###################################ACTIVITY AND DOMAIN CREATION###########################

print('Create the ActivityAndDomain Biology')
client.command('INSERT INTO ActivityAndDomain SET Name = \'Biology\', NameLowercase = \'biology\', InsertionDate = \'2018-04-09\'')

print('Create the ActivityAndDomain Data science')
client.command('INSERT INTO ActivityAndDomain SET Name = \'Data science\', NameLowercase = \'data science\', InsertionDate = \'2018-04-09\'')

print('Create the ActivityAndDomain Artificial Intelligence')
client.command('INSERT INTO ActivityAndDomain SET Name = \'Artificial Intelligence\', NameLowercase = \'artificial intelligence\', InsertionDate = \'2018-04-09\'')

###################################SKILLS CREATION###########################

print('Create the Skill PHP')
client.command('INSERT INTO Skills SET Name = \'PHP\', NameLowercase = \'php\', InsertionDate = \'2018-04-09\'')

print('Create the Skill Python')
client.command('INSERT INTO Skills SET Name = \'Python\', NameLowercase = \'python\', InsertionDate = \'2018-04-09\'')

print('Create the Skill RF')
client.command('INSERT INTO Skills SET Name = \'RF\', NameLowercase = \'rf\', InsertionDate = \'2018-04-09\'')

print('Create the Skill Rendering')
client.command('INSERT INTO Skills SET Name = \'Rendering\', NameLowercase = \'rendering\', InsertionDate = \'2018-04-09\'')

###################################CITY CREATION###########################

print('Create the city Toulouse')
client.command('INSERT INTO City SET Name = \'Toulouse\', NameLowercase = \'toulouse\', InsertionDate = \'2018-04-09\'')

print('Create the city Bordeaux')
client.command('INSERT INTO City SET Name = \'Bordeaux\', NameLowercase = \'bordeaux\', InsertionDate = \'2018-04-09\'')

print('Create the city Paris')
client.command('INSERT INTO City SET Name = \'Paris\', NameLowercase = \'paris\', InsertionDate = \'2018-04-09\'')

####################################GENERAL QUERIES#############################

query_football = 'SELECT FROM Hobbies WHERE NameLowercase = \'football\''
query_basketball = 'SELECT FROM Hobbies WHERE NameLowercase = \'basketball\''
query_baseball = 'SELECT FROM Hobbies WHERE NameLowercase = \'baseball\''

query_tom = 'SELECT FROM User WHERE FirstName LIKE \'Tom\''
query_foobar = 'SELECT FROM User WHERE FirstName LIKE \'Foo\''
query_johndoe = 'SELECT FROM User WHERE FirstName LIKE \'John\''

query_epitech = 'SELECT FROM School WHERE NameLowercase LIKE \'epitech\''
query_enac = 'SELECT FROM School WHERE NameLowercase LIKE \'enac\''
query_ipsa = 'SELECT FROM School WHERE NameLowercase LIKE \'ipsa\''

query_toulouse = 'SELECT FROM City WHERE NameLowercase LIKE \'toulouse\''
query_bordeaux = 'SELECT FROM City WHERE NameLowercase LIKE \'bordeaux\''
query_paris = 'SELECT FROM City WHERE NameLowercase LIKE \'paris\''

query_biology = 'SELECT FROM ActivityAndDomain WHERE NameLowercase LIKE \'biology\''
query_datascience = 'SELECT FROM ActivityAndDomain WHERE NameLowercase LIKE \'data science\''
query_ai = 'SELECT FROM ActivityAndDomain WHERE NameLowercase LIKE \'artificial intelligence\''

query_applystartup = 'SELECT FROM Company WHERE NameLowercase LIKE \'applystartup\''
query_epitech_company = 'SELECT FROM Company WHERE NameLowercase LIKE \'epitech\''

query_php = 'SELECT FROM Skills WHERE NameLowercase LIKE \'php\''
query_rf = 'SELECT FROM Skills WHERE NameLowercase LIKE \'rf\''
query_rendering = 'SELECT FROM Skills WHERE NameLowercase LIKE \'rendering\''
query_python = 'SELECT FROM Skills WHERE NameLowercase LIKE \'python\''

query_leaddev = 'SELECT FROM Offer WHERE NameLowercase LIKE \'lead dev\''
query_dpr = 'SELECT FROM Offer WHERE NameLowercase LIKE \'dpr\''
query_businessdev = 'SELECT FROM Offer WHERE NameLowercase LIKE \'business developper\''

###################################STUDIED CREATION###########################

print('Create an edge between John Doe and Epitech')
client.command('CREATE EDGE Studied FROM (' + query_johndoe + ') TO (' + query_epitech + ') SET StartDate = \'2018-04-09\', EndDate = \'2018-04-09\', Diploma = \'Master\', StillStudying = false, InsertionDate = \'2018-04-09\'')

print('Create an edge between Foo Bar and Epitech')
client.command('CREATE EDGE Studied FROM (' + query_foobar + ') TO (' + query_enac + ') SET StartDate = \'2018-04-09\', EndDate = \'2018-04-09\', Diploma = \'Master\', StillStudying = false, InsertionDate = \'2018-04-09\'')

print('Create an edge between Tom MMy and Enac')
client.command('CREATE EDGE Studied FROM (' + query_tom + ') TO (' + query_enac + ') SET StartDate = \'2018-04-09\', EndDate = \'2018-04-09\', Diploma = \'Master\', StillStudying = false, InsertionDate = \'2018-04-09\'')
client.command('CREATE EDGE Studied FROM (' + query_tom + ') TO (' + query_ipsa + ') SET StartDate = \'2018-04-09\', EndDate = \'2018-04-09\', Diploma = \'Master\', StillStudying = false, InsertionDate = \'2018-04-09\'')

###################################LivesIn CREATION###########################

print('Create an edge between Toulouse and John Doe')
client.command('CREATE EDGE LivesIn FROM (' + query_johndoe + ') TO (' + query_toulouse + ') SET InsertionDate = \'2018-04-09\'')

print('Create an edge between Bordeaux and Tom my')
client.command('CREATE EDGE LivesIn FROM (' + query_tom + ') TO (' + query_bordeaux + ') SET InsertionDate = \'2018-04-09\'')

print('Create an edge between Bordeaux and Foo bar')
client.command('CREATE EDGE LivesIn FROM (' + query_foobar + ') TO (' + query_bordeaux + ') SET InsertionDate = \'2018-04-09\'')

###################################LocatesIn CREATION###########################

print('Create an edge between Toulouse and Epitech')
client.command('CREATE EDGE LocatesIn FROM (' + query_epitech + ') TO (' + query_toulouse + ') SET InsertionDate = \'2018-04-09\'')

print('Create an edge between Toulouse and Enac')
client.command('CREATE EDGE LocatesIn FROM (' + query_enac + ') TO (' + query_toulouse + ') SET InsertionDate = \'2018-04-09\'')

print('Create an edge between Paris and Ipsa')
client.command('CREATE EDGE LocatesIn FROM (' + query_ipsa + ') TO (' + query_paris + ') SET InsertionDate = \'2018-04-09\'')

###################################WorksIn CREATION###########################

print('Create an edge between John Doe and Biology')
client.command('CREATE EDGE WorksIn FROM (' + query_johndoe + ') TO (' + query_biology + ') SET InsertionDate = \'2018-04-09\'')

print('Create an edge between John Doe and Data Science')
client.command('CREATE EDGE WorksIn FROM (' + query_johndoe + ') TO (' + query_datascience + ') SET InsertionDate = \'2018-04-09\'')

print('Create an edge between Foo Bar and Data Science')
client.command('CREATE EDGE WorksIn FROM (' + query_foobar + ') TO (' + query_datascience + ') SET InsertionDate = \'2018-04-09\'')

print('Create an edge between Tom MMy and Biology')
client.command('CREATE EDGE WorksIn FROM (' + query_tom + ') TO (' + query_biology + ') SET InsertionDate = \'2018-04-09\'')

###################################WorksFor CREATION###########################

print('Create an edge between John Doe and ApplyStartup')
client.command('CREATE EDGE WorksFor FROM (' + query_johndoe + ') TO (' + query_applystartup + ') SET Position = \'CTO\', InsertionDate = \'2018-04-09\'')

###################################ApplyFor CREATION###########################

print('Create an edge between Foo Bar and Lead dev, DPR')
client.command('CREATE EDGE ApplyFor FROM (' + query_foobar + ') TO (' + query_leaddev + ') SET InsertionDate = \'2018-04-09\'')
client.command('CREATE EDGE ApplyFor FROM (' + query_foobar + ') TO (' + query_dpr + ') SET InsertionDate = \'2018-04-09\'')

print('Create an edge between Tom and ApplyStartup')
client.command('CREATE EDGE ApplyFor FROM (' + query_tom + ') TO (' + query_leaddev + ') SET InsertionDate = \'2018-04-09\'')

###################################Master CREATION###########################

print('Create an edge between Foo Bar and Php Python and Rendering')
client.command('CREATE EDGE Master FROM (' + query_foobar + ') TO (' + query_php + ') SET Level = 4, InsertionDate = \'2018-04-09\'')
client.command('CREATE EDGE Master FROM (' + query_foobar + ') TO (' + query_python + ') SET Level = 3, InsertionDate = \'2018-04-09\'')
client.command('CREATE EDGE Master FROM (' + query_foobar + ') TO (' + query_rendering + ') SET Level = 2, InsertionDate = \'2018-04-09\'')

print('Create an edge between John Doe and Python')
client.command('CREATE EDGE Master FROM (' + query_johndoe + ') TO (' + query_python + ') SET Level = 4, InsertionDate = \'2018-04-09\'')

print('Create an edge between Tom my and Php, rendering')
client.command('CREATE EDGE Master FROM (' + query_tom + ') TO (' + query_php + ') SET Level = 4, InsertionDate = \'2018-04-09\'')
client.command('CREATE EDGE Master FROM (' + query_tom + ') TO (' + query_rendering + ') SET Level = 4, InsertionDate = \'2018-04-09\'')

###################################CWorksIn CREATION###########################

print('Create an edge between ApplyStartup and biology, data science')
client.command('CREATE EDGE CWorksIn FROM (' + query_applystartup + ') TO (' + query_biology + ') SET InsertionDate = \'2018-04-09\'')
client.command('CREATE EDGE CWorksIn FROM (' + query_applystartup + ') TO (' + query_datascience + ') SET InsertionDate = \'2018-04-09\'')

print('Create an edge between Epitech and artificial intelligence')
client.command('CREATE EDGE CWorksIn FROM (' + query_epitech + ') TO (' + query_ai + ') SET InsertionDate = \'2018-04-09\'')

###################################Require CREATION###########################

print('Create an edge between Lead dev and Php Python')
client.command('CREATE EDGE Require FROM (' + query_leaddev + ') TO (' + query_php + ') SET Level = 4, InsertionDate = \'2018-04-09\'')
client.command('CREATE EDGE Require FROM (' + query_leaddev + ') TO (' + query_python + ') SET Level = 4, InsertionDate = \'2018-04-09\'')

print('Create an edge between DPR and Rendering')
client.command('CREATE EDGE Require FROM (' + query_dpr + ') TO (' + query_rendering + ') SET Level = 4, InsertionDate = \'2018-04-09\'')

print('Create an edge between Business Dev and RF')
client.command('CREATE EDGE Require FROM (' + query_businessdev + ') TO (' + query_rf + ') SET Level = 4, InsertionDate = \'2018-04-09\'')

###################################Propose CREATION###########################

print('Create an edge between ApplyStartup and leaddev and bus dev')
client.command('CREATE EDGE Propose FROM (' + query_applystartup + ') TO (' + query_leaddev + ') SET InsertionDate = \'2018-04-09\'')
client.command('CREATE EDGE Propose FROM (' + query_applystartup + ') TO (' + query_businessdev + ') SET InsertionDate = \'2018-04-09\'')

print('Create an edge between Epitech and DPR')
client.command('CREATE EDGE Propose FROM (' + query_epitech + ') TO (' + query_dpr + ') SET InsertionDate = \'2018-04-09\'')

###################################Practice CREATION###########################

print('Create an edge between football and johndoe')
client.command('CREATE EDGE Practice FROM (' + query_johndoe + ') TO (' + query_football + ') SET StartDate = \'2018-04-09\', EndDate = \'2018-04-09\', InsertionDate = \'2018-04-09\'')

print('Create an edge between football and foobar')
client.command('CREATE EDGE Practice FROM (' + query_foobar + ') TO (' + query_football + ') SET StartDate = \'2018-04-09\', EndDate = \'2018-04-09\', InsertionDate = \'2018-04-09\'')
