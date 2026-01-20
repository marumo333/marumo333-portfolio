from uuid import uuid4

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from schemas import ProfileResponse

app = FastAPI()

# フロントエンド(SvelteKit)からのアクセスのみを許可する設定
origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/api/profile/me",response_model=ProfileResponse)
def get_portfolio():
    return {
            "id":uuid4(),
            "role": "developer",
            "bio": "文系出身でエンジニアを志すものです。",
            "avatar_url": None,
            "updated_at":None
        }
