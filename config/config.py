import json
import os 
from pathlib import Path
from dotenv import load_dotenv
class Config:
    def __init__(self):
        load_dotenv()
        config_dir = Path(__file__).parent
        config_file = config_dir / "config.json"
        with open(config_file,"r")as file:
            self.data = json.load(file)
    def get_ai_provider(self):
        return self.data["ai"]["provider"] 
    def get_gemini_api_key(self):
            api_key = os.getenv("GEMINI_API_KEY")
            return api_key       
    def get_backend_url(self):
         return self.data["backend"]["url"]