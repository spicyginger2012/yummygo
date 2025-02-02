from fastapi import FastAPI, Request
from routes.api_router import api_router
import sys
sys.path.append("d:/yummygo/backend")
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI(title="FastAPI Application")

origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,  # Cho phép client từ localhost:3000
    allow_credentials=True,  # Bật gửi cookies trong các yêu cầu
    allow_methods=["*"],
    allow_headers=["*"],
)

# Đăng ký tất cả router
app.include_router(api_router)



@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI application!"}
