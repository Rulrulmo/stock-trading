from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class StockInfo(BaseModel):
    """주식 기본 정보 스키마"""
    symbol: str
    name: str
    sector: Optional[str] = None
    market_cap: Optional[float] = None

class StockPrice(BaseModel):
    """주식 가격 정보 스키마"""
    symbol: str
    current_price: float
    change: float
    change_percent: float
    volume: int
    timestamp: datetime

class StockHistory(BaseModel):
    """주식 히스토리 데이터 스키마"""
    symbol: str
    date: datetime
    open_price: float
    high_price: float
    low_price: float
    close_price: float
    volume: int

class StockHistoryResponse(BaseModel):
    """주식 히스토리 응답 스키마"""
    symbol: str
    history: List[StockHistory]
    period_days: int 