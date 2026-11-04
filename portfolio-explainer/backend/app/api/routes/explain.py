from fastapi import APIRouter, HTTPException

from app.schemas.explanation import (
    ExplainRequest,
    ExplanationResponse
)

from app.services.explanation_service import (
    explain_portfolio
)


router = APIRouter()


@router.post(
    "/portfolio/{portfolio_id}/explain",
    response_model=ExplanationResponse
)
def explain_endpoint(
    portfolio_id: str,
    request: ExplainRequest
):

    result = explain_portfolio(
        portfolio_id=portfolio_id,
        question=request.question,
        period=request.period
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Portfolio not found"
        )

    return result