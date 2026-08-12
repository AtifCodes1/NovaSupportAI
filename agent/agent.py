from services.order_service import OrderService
from ai.gemini_ai import GeminiAI
class Agent:
    def __init__(self):
        self.convo_list = []
        self.orderservice = OrderService()
        self.waiting_for = None
        self.ai = GeminiAI()
    def receive_message(self,message):
        self.convo_list.append(message)
    def get_last_msg(self):
        if self.convo_list:
            return self.convo_list[-1] 
        else:
            return "Convo list is empty."  
    def check_intent(self):
        message = self.get_last_msg()
        result = self.ai.understand(message)
        return result 
    def decide_action(self):
        if self.waiting_for == "order_number":
            last_msg = self.get_last_msg()
            result = self.ai.extract_order_number(last_msg)
            if result.order_number is None:
                return "I couldn't find an order number. Please provide it."
            self.waiting_for = None
            return self.orderservice.get_status(result.order_number)
        result = self.check_intent()
        intent = result.intent
        if intent == "Greetings":
            return "Handle Greeting"
        elif intent == "Order":
            order_number = result.order_number
            if order_number is None:
                self.waiting_for = "order_number"
                return "Please provide your order number"
            return self.orderservice.get_status(order_number)
        elif intent == "Return":
            return "Handle return"
        else:
            return "No decision"