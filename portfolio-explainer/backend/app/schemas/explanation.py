from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class ExplainRequest(BaseModel):
    question: str = Field(
        min_length=3,
        max_length=500
    )

    period: Literal["day", "week", "month"] = "day"


class NewsSource(BaseModel):
    title: str
    url: str
    publisher: str
    published_at: datetime
    ticker: str | None = None


class ExplanationFactor(BaseModel):
    ticker: str
    name: str

    change_percent: float
    contribution_percent: float

    explanation: str


class PossibleCause(BaseModel):
    description: str
    ticker: str | None = None

    source_urls: list[str] = Field(
        default_factory=list
    )

    confidence: Literal[
        "low",
        "medium",
        "high"
    ]


class ExplanationResponse(BaseModel):
    request_id: str
    portfolio_id: str

    generated_at: datetime

    question: str
    period: Literal["day", "week", "month"]

    portfolio_change_percent: float
    summary: str

    main_factors: list[ExplanationFactor]
    possible_causes: list[PossibleCause]
    sources: list[NewsSource]
    limitations: list[str]
