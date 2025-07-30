from fastapi import FastAPI
from app.routers import stock

app = FastAPI(title="Stock Trading API", version="1.0.0")

# 라우터 등록
app.include_router(stock.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Stock Trading API", "version": "1.0.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy"} 