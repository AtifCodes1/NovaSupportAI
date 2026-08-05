from fastapi import FastAPI
from config.settings import Settings
settings = Settings()
app = FastAPI(
    title =settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION)
@app.get("/")
def moggli():
    return{
        "message" :"Moggli is on the new Project"}
