from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend access (important)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for demo (restrict in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "FastAPI is running 🚀"}

@app.get("/data")
def get_data():
    return {
        "name": "Vatsal",
        "role": "Trader",
        "status": "Active"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="192.168.0.250", port=3030, reload=True)  # reload for development
    