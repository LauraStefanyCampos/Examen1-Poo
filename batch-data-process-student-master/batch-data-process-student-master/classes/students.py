from classes.mongoDB import MongoDB
from classes.carrers import carrers

class students():
    def __init__(self,studentAccountNumber,studentName,cellphoneNumber , carrer,studentAge) :
        self.studentAccountNumber = studentAccountNumber
        self.studentName = studentName
        self.cellphoneNumber = cellphoneNumber
        self.carrer = carrer
        self.studentAge = studentAge
        self.__collection ='DATA'
        
        
        
    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id

    def update(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        objStore = { '$set' : self.__dict__ }
        collection.update_one( filterToUse , objStore )

    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        collection.delete_one( filterToUse )

    @staticmethod
    def get_list(db):
        collection = db["DATA"]
        Dataprocess = collection.find()

        list_Data = []
        for e in Dataprocess:
            temp_data = Dataprocess(
                e["studentAccountNumber"]
                , e["studentName"]
                , e["cellphoneNumber"]
                , e["carrer"]
                , e["studentAge"] 
            )

            list_Data.append(temp_data)
        return list_Data
    
    @staticmethod
    def delete_all(db):
        lista_e = students.get_list(db)
        for e in lista_e:
            e.delete(db)

    @staticmethod
    def print_full_report_long_path(db):
        collection = db["student"]

        for e in collection.find():
            r = { 
                "AccountNumber" : e["studentAccountNumber"]
                , "cellphoneNumber": e["cellphoneNumber"] 
                , "tipo": DATA.get_one(db, e["student"] ).tipo
            }
            print(r)

    @staticmethod
    def print_full_report_short_path(db):
        collection = db["student"]

        result = collection.aggregate([
            {
                '$lookup': {
                    'from': "student"
                    , 'localField': "student"
                    , "foreignField": "_id"
                    , "as": "te"
                }
            },{
                '$project': {
                    'numberAccount': 1
                    , '': 1
                    , 'te.tipo': 1
                }  
            }
        ])

        for d in result:
            print(d)