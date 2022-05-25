
import motor.motor_asyncio

MONGO_DB = "mongodb+srv://Zaid:Zaid@cluster0.4bszo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

mongo_dbb = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB)
dbb = mongo_dbb["SPAMBOT"]
SPAMBOT = 'SPAMBOT'

