from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import dashboard



# Inicializar la aplicación de FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a FastAPI"}

# Ruta con parámetros (GET request)
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Ruta para enviar datos usando POST request
@app.post("/create-item/")
def create_item(item: dict):
    return {"item": item, "message": "Item creado con éxito"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto según sea necesario
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dashboard.router, prefix="/api")