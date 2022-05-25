
from modules.config import MONGO_DB
import motor.motor_asyncio
mongo_dbb = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB)
dbb = mongo_dbb["SPAMBOT"]
SPAMBOT = 'SPAMBOT'

