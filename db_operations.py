import pymongo


url="mongodb://localhost:27017/"


### createMongodb method will create a new database, collection and a user
def createMongodb():
    with pymongo.MongoClient(url) as client:
        db= client["Device_Configuration"]
        collection= db["Interfaces"]
        collection.delete_many({}) #Reset documents with every execution
        db.command("updateUser", "cisco", pwd="cisco123", roles=[{"role":"readWrite","db":"Device_Configuration"}])

        int1 = {
        "Switch_name":"switch1",
        "Interface_Name":"int g1/0",
        "Description":"Connected to the switch2 gi1/2",
        "State":"up",
        }
        int2 = {
        "Switch_name":"switch1",
        "Interface_Name":"int fc1/1/0",
        "Description":"connected to the storage port 1",
        "State":"up",
        }
        int3 = {
        "Switch_name":"switch2",
        "Interface_Name":"int GigabitEthernet1/0/3",
        "Description":"Connected to printer CX2",
        "State":"up",
        }

        collection.insert_many([int1,int2,int3])
