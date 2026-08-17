from pydantic import BaseModel
class AIResponse(BaseModel):
    intent : str
    action :str |None = None
    order_number : str|None = None
class OrderNumberResponse(BaseModel):
    order_number : str|None = None

