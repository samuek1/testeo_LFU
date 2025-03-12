import httpx

# Cliente para conectarse a JSONPlaceholder
class JSONPlaceholderClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    @staticmethod
    def get_post(post_id: int):
        url = f"{JSONPlaceholderClient.BASE_URL}/posts/{post_id}"
        response = httpx.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "No se pudo obtener el post"}