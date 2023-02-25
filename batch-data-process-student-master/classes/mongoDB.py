import pymongo
import os

class MongoDB:
    
    @staticmethod
    def getDB():
        user = os.environ['LauraStefany']
        password = os.environ['CamposCampos2023']
        cluster = os.environ['@cluster0.wwn8lh1.mongodb.net']
        query_string = 'retryWrites=true&w=majority'


        ## Connection String
        uri = "mongodb+srv://{0}:{1}@{2}/?{3}".format(
            user
            , password
            , cluster
            , query_string
        )

        print(uri)
 
        client = pymongo.MongoClient(uri)
        db = client[os.environ['DB']]

        return client, db