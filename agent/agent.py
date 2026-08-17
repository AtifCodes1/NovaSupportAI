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
        self.current_action =None
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
    def _handle_order(self,ordernumber):
        order = self.orderservice.get_status(ordernumber)
        if order is None:
            return f"No order on {ordernumber}"
        else:
            return order
    def _handle_return(self,ordernumber):
        if self.current_action=="Check":
            return_order = self.returnservice.process_return(ordernumber)
            if return_order is None:
                return (f"no order found for return {ordernumber}")
            elif not return_order["return_eligible"]:
                return (f"order {ordernumber} is not eligible for return")
            else:
                return return_order
        elif self.current_action=="Request":    
            return_order = self.returnservice.request_return(ordernumber)
            if return_order is None:
                return (f"no order found for return {ordernumber}")
            else:
                return return_order
        else:
            return "I couldn't understand what you want to do with the return."    
        
    def _handle_waiting(self):
        ordernumber = self._get_order_number()
        if ordernumber is None:
            return "I couldn't find an order number. Please provide it."
        if self.current_intent == "Order":
            response= self._handle_order(ordernumber)
        elif self.current_intent == "Return":
            response= self._handle_return(ordernumber)
        else:
            return "Something went wrong"
        self.waiting_for = None
        self.current_intent = None
        self.current_action = None
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
            return self._handle_order(order_number)
        elif intent == "Return":
            order_number = result.order_number
            self.current_action = result.action
            if order_number is None:
                self.current_intent = "Return"
                self.waiting_for = "return_order_number"
                return "Please provide your order number"
            return self._handle_return(order_number)
        else:
            return "No decision"