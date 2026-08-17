from api.client import APIClient
from config.config import Config
class OrderService:
    def __init__(self):
        self.config = Config()
        url = self.config.get_backend_url()
        self.api_client = APIClient(url)
    def get_status(self,ordernumber):
        response = self.api_client.get(f"/orders/{ordernumber}")
        if response.status_code == 200:
            return response.json()
        return None