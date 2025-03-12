# testeo_LFU
TESTEO

# Proyecto LFU Cache con FastAPI

Este proyecto implementa una caché LFU (Least Frequently Used) y una API para mostrar su funcionamiento.

## Estructura

- `src/lfu_cache.py`: Implementación de la caché LFU.
- `src/api_client.py`: API con FastAPI que utiliza la caché.
- `tests/test_lfu_cache.py`: Pruebas unitarias.
- `requirements.txt`: Dependencias del proyecto.

## Instalación

1. Clonar el repositorio.
2. Crear y activar entorno virtual con uv.
3. Instalar dependencias.
4. Correr la API con:
```bash
uvicorn src.api_client:app --reload