from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# フロントエンド(SvelteKit)からのアクセスを許可する設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/portfolio")
def get_portfolio():
    return [
        {"id": 1, "title": "My First Project", "description": "SvelteKitで作りました"},
        {"id": 2, "title": "Python API", "description": "FastAPIで動いています"}
    ]