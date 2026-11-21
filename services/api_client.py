import requests
from CTkMessagebox import CTkMessagebox as Message

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None
        self.session = requests.Session()

    def login(self, email, password):
        try:
            response = self.session.post(
                f"{self.base_url}/auth/login",
                data={
                    "username": email,
                    "password": password
                },
                timeout=10
            )
            if response.status_code == 401:
                Message(title="Error de autenticacion", message="Correo o contraseña incorrectos", icon="cancel")
                return False
            self.token = response.json()["access_token"]
            self.session.headers.update({
                "Authorization": f"Bearer {self.token}"
            })
            return True
        except requests.exceptions.RequestException as error:
            Message(title="Error de servidor", message=f"No se pudo conectar con el servidor: {error}", icon="cancel")
            return False
    
    def get(self, endpoint):
        try:
            response = self.session.get(
                f"{self.base_url}{endpoint}",
                timeout=10
            )
            return response.json()
        except requests.exceptions.RequestException as error:
            Message(title="Error de servidor", message=f"No se pudo conectar con el servidor: {error}", icon="cancel")
            return None

    def getPhoto(self, endpoint):
        try: 
            response = self.session.get(
                f"{self.base_url}{endpoint}",
                timeout=10
            )
            return response
        except requests.exceptions.RequestException as error:
            Message(title="Error de servidor", message=f"No se pudo conectar con el servidor: {error}", icon="cancel")
            return None
                