from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class ReturnRequest(BaseModel):
    order_number : str
orders = {
    "1001": {
        "status": "shipped",
        "location": "Islamabad",
        "estimated_delivery": "5 working days"},
    "1002": {
        "status": "processing",
        "location": "Peshawar",
        "estimated_delivery": "8 working days"}}
returns = {
    "1001": {
        "return_eligible": True,
        "return_status": "Not_requested"},
    "1002": {
        "return_eligible": False,
        "return_status": "Not_eligible"}}
@app.get("/")
def home():
    return {"message": "Mock Backend is running"}
@app.get("/orders/{order_number}")
def get_order(order_number: str):
    if order_number in orders:
        return orders[order_number]
    return {"error": "Order not found"}
@app.get("/returns/{order_number}")
def get_return(order_number: str):
    if order_number in returns:
        return returns[order_number]
    return {"error": "Return information not found"}
@app.post("/returns")
def create_return(request : ReturnRequest):
    if request.order_number not in returns:
        return "Return information not found"
    data = returns[request.order_number]
    if not data["return_eligible"]:
        return {
            "order_number" : request.order_number,
            "return_status" : "Not_eligible"
        }
    data["return_status"] = "Requested"
    return {
        "order_number": request.order_number,
        "return_eligible": data["return_eligible"],
        "return_status": data["return_status"]}