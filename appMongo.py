from database import Database
import pymongo
from models.post import Post

__author__ = "technokowski"



Database.initialize()

myPost = Post(blog_id="123",
              title="Another great post",
              content="This is some sample content",
              author="Gabriel")

myPost2 = Post(blog_id="123",
              title="Another great post33",
              content="This is some sample content33",
              author="Gabriel33")

posts = Post.from_blog('123')

for post in posts:
    print(post)


posted = Post.from_mongo('b6a0210b39904b94b00113b6c912132c')
print("#"*99)
print(posted)