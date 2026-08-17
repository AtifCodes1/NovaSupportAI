import requests
class APIClient:
    def __init__(self,baseurl):
        self.base_url = baseurl
    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"   
        response = requests.get(url)
        return response 
    def post(self,endpoint,data):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url,json=data)
        return response