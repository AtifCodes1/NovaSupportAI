import json
from ai.base_ai import BaseAI
from google import genai
from config.config import Config
from ai.models import AIResponse,OrderNumberResponse
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
            2. action
            3. order number
        The intent must be exactly one of:
            "Greetings"
            "Order"
            "Return"
            "Unknown"
        If the intent is "Return", the action must be exactly one of:
            "Check"
            "Request"
        Use "Check" when the customer is asking about return eligibility,
            return status, or whether they can return the order.
        Use "Request" when the customer wants to actually submit/create
            a return request.
        If the intent is not "Return", set action to null.
        If there is no order number, set order_number to null.
        Don't provide extra information or text.
        Return only JSON.'''
        response = self.client.models.generate_content(
                    model="gemini-3.5-flash-lite",contents=prompt)
        answer = response.text.strip()
        data = json.loads(answer)
        result = AIResponse(**data)
        return result
    def extract_order_number(self,message):
        prompt = f'''Analyze this customer message.
                    message = {message}
                    Extract order_number from message,
                    The json must contain this key "order_number"
                    if there is no order_number set it to null,
                    if you just see numeric numbers set it to "order_number"
                    Don't give extra text or information 
                    give the json with just order_number
                    Just return it in json.'''
        response = self.client.models.generate_content(
                            model="gemini-3.5-flash-lite",contents=prompt)
        answer = response.text.strip()
        data = json.loads(answer)
        result = OrderNumberResponse(**data)
        return result