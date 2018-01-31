from database import Database
import pymongo
from models.post import Post

__author__ = "technokowski"



Database.initialize()

myPost = Post('Movies', 'fartman', 'Yes he is!', 'Turd Furgeson', 'Jan 31 2018', 1)

print(myPost.content)


