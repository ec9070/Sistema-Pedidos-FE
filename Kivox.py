from forms.login import Login
from dotenv import load_dotenv
import os
from services.api_client import APIClient
import util.globals as globales

load_dotenv()

def main():
    api = APIClient(os.getenv("API"))
    globales.setApi(api)
    Login()

if __name__ == '__main__':
    main()