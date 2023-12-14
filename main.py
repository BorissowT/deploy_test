import datetime

from pymongo import MongoClient
username = "admin"
password = "password"
client = MongoClient("mongodb", 27018, username=username, password=password)

db = client.test_database


post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}
posts = db.posts
post_id = posts.insert_one(post).inserted_id
all_posts = posts.find()

# Print each post
for post in all_posts:
    print(post)
