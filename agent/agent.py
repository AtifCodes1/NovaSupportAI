from services.order_service import OrderService
from services.return_service import ReturnService
from ai.gemini_ai import GeminiAI
class Agent:
    def __init__(self):
        self.convo_list = []
        self.orderservice = OrderService()
        self.returnservice = ReturnService()
        self.current_intent = None
        self.waiting_for = None
        self.ai = GeminiAI()
    def _get_order_number(self):
        last_msg = self.get_last_msg()
        result = self.ai.extract_order_number(last_msg)
        if result.order_number is None:
            return None
        self.waiting_for = None   
        return result.order_number 
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
    def _handle_waiting(self):
        ordernumber = self._get_order_number()
        if ordernumber is None:
            return "I couldn't find an order number. Please provide it."
        if self.current_intent == "Order":
            response= self.orderservice.get_status(ordernumber)
        elif self.current_intent == "Return":
            response= self.returnservice.process_return(ordernumber)
        else:
            return "Something went wrong"
        self.waiting_for = None
        self.current_intent = None
        return response
    def decide_action(self):
        if self.waiting_for is not None:
            return self._handle_waiting()
        result = self.check_intent()
        intent = result.intent
        if intent == "Greetings":
            return"What can I help you?"
        elif intent == "Order":
            order_number = result.order_number
            if order_number is None:
                self.current_intent = "Order"
                self.waiting_for = "order_number"
                return "Please provide your order number"
            return self.orderservice.get_status(order_number)
        elif intent == "Return":
            order_number = result.order_number
            if order_number is None:
                self.current_intent = "Return"
                self.waiting_for = "return_order_number"
                return "Please provide your order number"
            return self.returnservice.process_return(order_number)
        else:
            return "No decision"