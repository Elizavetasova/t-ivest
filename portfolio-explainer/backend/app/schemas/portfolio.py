from datetime import datetime
from pydantic import BaseModel, Field


class Position(BaseModel):
    ticker: str
    name: str
    quantity: float
    currency: str = "RUB"

    current_price: float
    previous_price: float

    market_value: float
    weight_percent: float

    change_percent: float
    contribution_percent: float


class PortfolioSummary(BaseModel):
    portfolio_id: str
    currency: str = "RUB"

    total_value: float
    previous_value: float

    change_absolute: float
    change_percent: float

    positions_count: int
    updated_at: datetime


class PortfolioResponse(BaseModel):
    summary: PortfolioSummary
    positions: list[Position]

