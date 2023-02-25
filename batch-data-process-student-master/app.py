import pymongo
from classes import DATA, Dataprocess

def main():

    pipeline = Dataprocess(DATA)
    
    pipeline.create_careers()
    pipeline.create_students()
    pipeline.create_enrollments()
    
    
    allKeys = DATA.keys()

if tKey in allKeys:
    print("Key Found!")
else:
    print("Key Not Found!")
    
    return True

if __name__ == "__main__":
    main()