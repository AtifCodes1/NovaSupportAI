from api.client import APIClient
class OrderService:
    def __init__(self):
        self.api_client = APIClient("http://127.0.0.1:8001")
    def get_status(self,ordernumber):
        response = self.api_client.get(f"/orders/{ordernumber}")
        if response.status_code == 200:
            return response.json()
        return None