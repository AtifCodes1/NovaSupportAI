from fastapi import FastAPI
app = FastAPI(
    title = "NovaSupportAI",
    description="An agent that supports Customers",
    version="1.0.0"
)
@app.get("/")
def moggli():
    return{
        "message" :"Moggli is on the new Project"
    }