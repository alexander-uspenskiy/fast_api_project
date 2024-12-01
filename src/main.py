from fastapi import FastAPI
from fastapi.responses import FileResponse  # Import FileResponse
app = FastAPI()

@app.get("/hello")
def hello(name:str):
    return {"Hello": f"How you doing, {name}?"}
@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI app!"}
@app.get("/favicon.ico")
def get_favicon():
    return FileResponse("static/favicon.ico")