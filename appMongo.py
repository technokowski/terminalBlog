__author__ = "technokowski"

import pymongo

# On start, type mongod in one terminal, then mongo in another:
# show dbs,

# To kill the mongod process when restarting: ps ax | grep mongod
# then: kill -9 mongod

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']

students = [person['mark'] for person in collection.find({}) if person['mark'] >= 99]

#for student in students:
#    print(student)


print(students)

