import json
from ai.base_ai import BaseAI
from google import genai
from config.config import Config
class GeminiAI(BaseAI):
    def __init__(self):
        self.config = Config()
        api_key = self.config.get_gemini_api_key()
        self.client = genai.Client(api_key=api_key)
    def understand(self,message):
        prompt = f'''Analyze this customer message.
                    message = {message}
                    Identify:
                    1. intent
                    2. order number
                    Don't provide extra information or text.
                    Return only JSON.'''
        response = self.client.models.generate_content(
                    model="gemini-3.5-flash-lite",contents=prompt)
        answer = response.text.strip()
        data = json.loads(answer)
        return data
    def extract_order_number(self,message):
        prompt = f'''Analyze this customer message.
                    message = {message}
                    And extract order_number from it,
                    Don't give extra text or information 
                    Just return it in json.'''
        response = self.client.models.generate_content(
                            model="gemini-3.5-flash-lite",contents=prompt)
        answer = response.text.strip()
        data = json.loads(answer)
        return data