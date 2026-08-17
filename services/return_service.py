from api.client import APIClient
from config.config import Config
class ReturnService:
    def __init__(self):
        self.config = Config()
        url = self.config.get_backend_url()
        self.api_client = APIClient(url)
    def process_return(self,ordernumber):
        response = self.api_client.get(f"/returns/{ordernumber}")
        if response.status_code == 200:
            return response.json()
        return None
    def request_return(self,ordernumber):
        data = {"order_number":ordernumber}
        response = self.api_client.post("/returns",data)
        if response.status_code==200:
            return response.json()
        return None