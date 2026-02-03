from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import profile

app = FastAPI()

# フロントエンド(SvelteKit)からのアクセスのみを許可する設定
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(profile.router)

@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello from FastAPI!"}
