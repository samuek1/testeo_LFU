from fastapi import FastAPI
from src.lfu_cache import LFUCache

app = FastAPI()
cache = LFUCache(capacity=3)  # Capacidad limitada de ejemplo

@app.get("/")
def read_root():
    return {"message": "¡API funcionando con caché LFU!"}

@app.get("/datos/{item_id}")
def get_data(item_id: int):
    # Verificar si el dato ya está en la caché
    cached_data = cache.get(item_id)
    if cached_data != -1:
        return {"source": "cache", "data": cached_data}

    # Si no está, simular petición a una API externa (aquí solo generamos un dato)
    data = {
        "id": item_id,
        "nombre": f"Elemento {item_id}",
        "descripcion": "Este es un dato de prueba desde la API."
    }

    # Guardar en caché
    cache.put(item_id, data)

    return {"source": "api", "data": data}