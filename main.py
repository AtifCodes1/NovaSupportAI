from fastapi import FastAPI
from pydantic import BaseModel
from core.conversation_manager import ConversationManager
from config.settings import Settings
settings = Settings()
class ChatRequest(BaseModel):
   user_id : str
   message : str  
app = FastAPI(
    title =settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION)
conversation_manager = ConversationManager()
@app.get("/")
def moggli():
    return{
        "message" :"Moggli is on the new Project"}
@app.post("/chat")
def chat(request : ChatRequest):
    agent = conversation_manager.get_agent(request.user_id)
    agent.receive_message(request.message)
    response = agent.decide_action()
    print(response)
