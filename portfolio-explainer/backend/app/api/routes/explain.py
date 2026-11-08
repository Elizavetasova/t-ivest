# Обработку неизвестного портфеля (ValueError → 404) лучше сделать отдельно.

from fastapi import APIRouter

from app.schemas.explanation import (
    ExplainRequest,
    ExplanationResponse,
)

from app.services.explanation_service import (
    explain_portfolio,
)


router = APIRouter()


@router.post(
    "/portfolio/{portfolio_id}/explain",
    response_model=ExplanationResponse,
)
def explain_endpoint(
    portfolio_id: str,
    request: ExplainRequest,
):
    return explain_portfolio(
        portfolio_id=portfolio_id,
        question=request.question,
        period=request.period,
    )
