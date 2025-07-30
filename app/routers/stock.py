from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.stock import StockInfo, StockPrice
from app.services.stock_service import StockService

router = APIRouter(tags=["stocks"])
stock_service = StockService()

@router.get("/stocks", response_model=List[StockInfo])
async def get_stocks():
    """모든 주식 목록을 반환합니다."""
    try:
        return await stock_service.get_all_stocks()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/stocks/{symbol}", response_model=StockPrice)
async def get_stock_price(symbol: str):
    """특정 주식의 현재 가격을 반환합니다."""
    try:
        return await stock_service.get_stock_price(symbol)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Stock {symbol} not found")

@router.get("/stocks/{symbol}/history")
async def get_stock_history(symbol: str, days: int = 30):
    """특정 주식의 히스토리 데이터를 반환합니다."""
    try:
        return await stock_service.get_stock_history(symbol, days)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Stock {symbol} history not found") 