from services.order_service import OrderService
class Agent:
    def __init__(self):
        self.convo_list = []
        self.orderservice = OrderService()
        self.waiting_for = None
    def receive_message(self,message):
        self.convo_list.append(message)
    def get_last_msg(self):
        if self.convo_list:
            return self.convo_list[-1] 
        else:
            return "Convo list is empty."  
    def check_intent(self):
        last_msg = self.get_last_msg().lower().split()
        if last_msg != "Convo list is empty.":
            for word in last_msg:
                if word == "hi" or word == "hello":
                    return "Greetings"
                elif word == "order" or word == "payment":
                    return "Order"
                elif word == "refund" or word == "return":
                    return "Return"
            return "Nothing Understandable"
        else:
            return last_msg
    def missing_value(self):
        intent = self.check_intent()
        if intent == "Order":
            self.waiting_for = "order_number" 
            return "Please provide your missing number"  
    def decide_action(self):
        if self.waiting_for == "order_number":
            order_number = self.get_last_msg()
            self.waiting_for = None
            return self.orderservice.get_status(order_number)
        intent = self.check_intent()
        if intent == "Greetings":
            return "Handle Greeting"
        elif intent == "Order":
            return self.missing_value()
        elif intent == "Return":
            return "Handle return"
        else:
            return "No decision"   