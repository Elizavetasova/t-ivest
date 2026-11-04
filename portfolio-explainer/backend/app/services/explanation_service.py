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

from typing import Any

from app.services.portfolio_service import get_portfolio


def explain_portfolio(
    portfolio_id: str,
    question: str,
    period: str = "day",
) -> dict[str, Any]:
    """Формирует объяснение изменения портфеля."""

    portfolio = get_portfolio(portfolio_id)

    change_percent = portfolio["change_percent"]
    change_absolute = portfolio["change_absolute"]
    currency = portfolio["currency"]

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

    sorted_positions = sorted(
        portfolio["positions"],
        key=lambda position: position["change_absolute"],
    )

    main_factors = []

    for position in sorted_positions[:3]:
        main_factors.append({
            "ticker": position["ticker"],
            "name": position["name"],
            "change_percent": round(position["change_percent"], 2),
            "contribution_percent": round(
                position["contribution_percent"], 2
            ),
            "change_absolute": round(position["change_absolute"], 2),
        })

    return {
        "portfolio_id": portfolio_id,
        "question": question,
        "period": period,
        "summary": summary,
        "portfolio_change_percent": change_percent,
        "main_factors": main_factors,
        "possible_causes": [],
        "sources": [],
        "limitations": [
            "Используются демонстрационные данные.",
            "Новости и рыночные события пока не анализируются.",
        ],
    }