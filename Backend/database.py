from motor.motor_asyncio import AsyncIOMotorClient

uri = "mongodb+srv://rivejuan987:Juann9876@cluster0.wr8kl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Usar AsyncIOMotorClient en lugar de MongoClient para la conexión asincrónica
client = AsyncIOMotorClient(uri)
db = client["DataUser"]
collection = db["DataRegister"]

{
  "user_id": "12345", 
  "weekly_progress": {
    "day": "Monday",
    "activities_completed": 2,
    "total_activities": 3,
    "percentage": 66
  },
  "week_reset_date": "2024-11-27"
}