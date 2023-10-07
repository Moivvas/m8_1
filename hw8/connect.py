# This code taken from Atlas MongoDB
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://moivvas:password@moivvas.am1rhde.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

if __name__ == '__main__':
        
    # Send a ping to confirm a successful connection
    # print Documents from author collection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        
        results = client.hw8_1.authors.find()
        for r in results:
            print(r)
            
    except Exception as e:
        print(e)
