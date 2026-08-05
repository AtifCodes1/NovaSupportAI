class Agent:
    def __init__(self):
        self.convo_list = []
    def receive_message(self,message):
        self.convo_list.append(message)
    def get_last_msg(self):
        if self.convo_list:
            return self.convo_list[-1] 
        else:
            return "Convo list is empty."              