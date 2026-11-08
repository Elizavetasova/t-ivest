# Этот сервис отвечает за объяснение результатов.

# На первом этапе можно не подключать LLM. 
# Создадим простое объяснение на основе 
# рассчитанных данных. Это позволит протестировать 
# backend и frontend независимо от AI.

# backend/app/services/explanation_service.py
# Сейчас это не полноценный AI-агент, а временная реализация сервиса объяснения. Но frontend уже сможет получить ответ в нужном формате и отобразить его.

# Впоследствии внутри explain_portfolio() можно добавить:
# 1. Получение рассчитанных данных портфеля.
# 2. Получение релевантных новостей.
# 3. Формирование контекста для LLM.
# 4. Вызов модели.
# 5. Проверку и возврат ответа.
# Сам endpoint при этом менять практически не придётся.

from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from app.services.portfolio_service import get_portfolio


def explain_portfolio(
    portfolio_id: str,
    question: str,
    period: str = "day",
) -> dict[str, Any]:
    """Формирует объяснение изменения портфеля без LLM."""

    portfolio = get_portfolio(portfolio_id)

    # После исправления portfolio_service
    # показатели портфеля находятся в summary.
    portfolio_summary = portfolio["summary"]

    change_percent = portfolio_summary["change_percent"]
    change_absolute = portfolio_summary["change_absolute"]
    currency = portfolio_summary["currency"]

    if change_percent < 0:
        summary = (
            f"Портфель снизился на {abs(change_percent):.2f}% "
            f"({abs(change_absolute):,.2f} {currency})."
        )
    elif change_percent > 0:
        summary = (
            f"Портфель вырос на {change_percent:.2f}% "
            f"({change_absolute:,.2f} {currency})."
        )
    else:
        summary = "Стоимость портфеля не изменилась."

    # Сортируем позиции от наибольшего отрицательного
    # изменения к наименьшему.
    sorted_positions = sorted(
        portfolio["positions"],
        key=lambda position: position["change_absolute"],
    )

    main_factors = []

    for position in sorted_positions[:3]:
        change = position["change_absolute"]

        if change < 0:
            factor_explanation = (
                f"Стоимость позиции снизилась на "
                f"{abs(change):,.2f} {currency}."
            )
        elif change > 0:
            factor_explanation = (
                f"Стоимость позиции выросла на "
                f"{change:,.2f} {currency}."
            )
        else:
            factor_explanation = (
                "Стоимость позиции не изменилась."
            )

        main_factors.append({
            "ticker": position["ticker"],
            "name": position["name"],
            "change_percent": round(
                position["change_percent"], 2
            ),
            "contribution_percent": round(
                position["contribution_percent"], 2
            ),
            "explanation": factor_explanation,
        })

    return {
        "request_id": str(uuid4()),
        "portfolio_id": portfolio_id,
        "generated_at": datetime.now(timezone.utc),

        "question": question,
        "period": period,

        "portfolio_change_percent": round(
            change_percent, 2
        ),
        "summary": summary,

        "main_factors": main_factors,
        "possible_causes": [],
        "sources": [],

        "limitations": [
            "Используются демонстрационные данные.",
            "Новости и рыночные события пока не анализируются.",
            "Объяснение сформировано без использования LLM.",
        ],
    }
