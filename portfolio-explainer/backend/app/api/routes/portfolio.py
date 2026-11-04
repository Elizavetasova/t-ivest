from fastapi import APIRouter, HTTPException

from app.schemas.portfolio import PortfolioResponse
from app.services.portfolio_service import (
    get_portfolio
)


router = APIRouter()


@router.get(
    "/portfolio/{portfolio_id}",
    response_model=PortfolioResponse
)
def portfolio_endpoint(portfolio_id: str):

    portfolio = get_portfolio(portfolio_id)

    if portfolio is None:
        raise HTTPException(
            status_code=404,
            detail="Portfolio not found"
        )

    return portfolio