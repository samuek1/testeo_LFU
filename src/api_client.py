from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡API funcionando!"}

@app.get("/datos/{item_id}")
def get_data(item_id: int):
    return {
        "id": item_id,
        "nombre": f"Elemento {item_id}",
        "descripcion": "Este es un dato de prueba."
    }