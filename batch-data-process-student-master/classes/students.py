from classes.mongoDB import MongoDB
from classes.carrers import carrers

class students():
    def __init__(self,studentAccountNumber,studentName,cellphoneNumber , carrer,studentAge,data) :
       
        self.studentAccountNumber = studentAccountNumber
        self.studentName = studentName
        self.cellphoneNumber = cellphoneNumber
        self.carrer = carrer
        self.studentAge = studentAge
        self.collection = 'data'
        
      
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
  
        
        