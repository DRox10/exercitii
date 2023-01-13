import pymongo

myclient = pymongo.MongoClient("localhost", 27017)
mydb = myclient["thedatabase"]

#-------------check if "thedatabase" exist:
dblist = myclient.list_database_names()
if "thedatabase" in dblist:
    print("THE DATABASE EXIST. ")

#------------adaugarea documentelor in colectie:
mycol = mydb["Filme"]

mydict = {"_id": 1, "titlu": "Black Widow", "gen":"actiune", "an": "2021" }

x = mycol.insert_one(mydict)
print(x.inserted_id)   

mylist = [
    {"_id":2, "titlu":"Captain America", "gen":"actiune", "an":"2016"},
    {"_id":3, "titlu":"Thor: Ragnarok", "gen":"actiune", "an":"2017"},
    {"_id":4, "titlu":"Doctor Strange", "gen":"actiune", "an":"2016"}
]

x = mycol.insert_many(mylist)
print(x.inserted_ids)


#-------------selectarea tuturor documentelor:

for x in mycol.find():
    print(x)