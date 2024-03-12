import pymongo
import certifi

URL = "mongodb+srv://root:root@cluster0.q32xd0o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(URL, tlsCAFile=certifi.where())
DB = client.get_database("organika")
