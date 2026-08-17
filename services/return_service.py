from api.client import APIClient
class ReturnService:
    def __init__(self):
        self.api_client = APIClient("http://127.0.0.1:8001")
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