from fastapi import APIRouter
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime

router = APIRouter()

# Configura tu conexión a MongoDB
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["mental_health"]
progress_collection = db["progress"]

# Inicializar datos de progreso si no existen
@router.on_event("startup")
async def init_progress():
    existing_data = await progress_collection.find_one({"user_id": "default_user"})
    if not existing_data:
        await progress_collection.insert_one({
            "user_id": "default_user",
            "date": datetime.utcnow().strftime("%Y-%m-%d"),
            "activities_completed": 0,
            "progress": 0
        })

# Ruta para obtener el progreso
@router.get("/progress")
async def get_progress():
    data = await progress_collection.find_one({"user_id": "default_user"})
    if not data:
        return {"error": "No progress found"}
    return data

# Ruta para actualizar progreso
@router.post("/progress")
async def update_progress():
    data = await progress_collection.find_one({"user_id": "default_user"})
    if not data:
        return {"error": "No progress found"}
    
    activities = data["activities_completed"] + 1
    progress = (activities / 21) * 100  # 21 actividades semanales
    
    # Si las actividades alcanzan el máximo semanal, reinicia
    if activities >= 21:
        activities = 0
        progress = 0
    
    await progress_collection.update_one(
        {"user_id": "default_user"},
        {"$set": {"activities_completed": activities, "progress": progress}}
    )
    return {"activities_completed": activities, "progress": progress}

