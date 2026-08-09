from agent.agent import Agent
class ConversationManager:
    def __init__(self):
        self.conversations = {}
    def get_agent(self,user_id):
        if(user_id in self.conversations):
            return self.conversations[user_id]
        else:
            agent = Agent()
            self.conversations[user_id]=agent
            return self.conversations[user_id]