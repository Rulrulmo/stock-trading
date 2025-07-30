import asyncio
from typing import List, Dict, Any
from datetime import datetime, timedelta
import random
from app.schemas.stock import StockInfo, StockPrice, StockHistory, StockHistoryResponse

class StockService:
    """주식 데이터 서비스 클래스"""
    
    def __init__(self):
        # 샘플 주식 데이터
        self.sample_stocks = {
            "AAPL": {"name": "Apple Inc.", "sector": "Technology", "market_cap": 2000000000000},
            "GOOGL": {"name": "Alphabet Inc.", "sector": "Technology", "market_cap": 1500000000000},
            "MSFT": {"name": "Microsoft Corporation", "sector": "Technology", "market_cap": 1800000000000},
            "TSLA": {"name": "Tesla Inc.", "sector": "Automotive", "market_cap": 800000000000},
            "AMZN": {"name": "Amazon.com Inc.", "sector": "Consumer Discretionary", "market_cap": 1200000000000}
        }
    
    async def get_all_stocks(self) -> List[StockInfo]:
        """모든 주식 목록을 반환합니다."""
        stocks = []
        for symbol, data in self.sample_stocks.items():
            stocks.append(StockInfo(
                symbol=symbol,
                name=data["name"],
                sector=data["sector"],
                market_cap=data["market_cap"]
            ))
        return stocks
    
    async def get_stock_price(self, symbol: str) -> StockPrice:
        """특정 주식의 현재 가격을 반환합니다."""
        if symbol not in self.sample_stocks:
            raise ValueError(f"Stock {symbol} not found")
        
        # 실제 구현에서는 외부 API를 호출하여 실시간 데이터를 가져옵니다
        base_price = random.uniform(100, 500)
        change = random.uniform(-10, 10)
        change_percent = (change / base_price) * 100
        
        return StockPrice(
            symbol=symbol,
            current_price=base_price + change,
            change=change,
            change_percent=change_percent,
            volume=random.randint(1000000, 10000000),
            timestamp=datetime.now()
        )
    
    async def get_stock_history(self, symbol: str, days: int = 30) -> StockHistoryResponse:
        """특정 주식의 히스토리 데이터를 반환합니다."""
        if symbol not in self.sample_stocks:
            raise ValueError(f"Stock {symbol} not found")
        
        history = []
        base_price = random.uniform(100, 500)
        
        for i in range(days):
            date = datetime.now() - timedelta(days=days-i-1)
            open_price = base_price + random.uniform(-20, 20)
            high_price = open_price + random.uniform(0, 10)
            low_price = open_price - random.uniform(0, 10)
            close_price = open_price + random.uniform(-5, 5)
            
            history.append(StockHistory(
                symbol=symbol,
                date=date,
                open_price=round(open_price, 2),
                high_price=round(high_price, 2),
                low_price=round(low_price, 2),
                close_price=round(close_price, 2),
                volume=random.randint(1000000, 10000000)
            ))
            
            base_price = close_price
        
        return StockHistoryResponse(
            symbol=symbol,
            history=history,
            period_days=days
        ) 