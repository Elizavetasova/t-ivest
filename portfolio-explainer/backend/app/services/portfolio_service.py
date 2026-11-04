# получает mock-портфель, 
# рассчитывает его показатели 
# и готовит данные для анализа.

# backend/app/services/portfolio_service.py
# Для начала можно хранить тестовый портфель 
# прямо в файле. Позже перенесёте mock-данные в 
# отдельный JSON или замените 
# mock-провайдер на API Т-Инвестиций.

# !!! Ограничение: пока предполагается, что 
# пользователь не покупал и не продавал активы 
# в течение анализируемого периода. 
# Для MVP это допустимо, но в реальном 
# приложении нужно учитывать операции и 
# денежные потоки.

from typing import Any


MOCK_PORTFOLIOS: dict[str, dict[str, Any]] = {
    "demo-001": {
        "portfolio_id": "demo-001",
        "currency": "RUB",
        "positions": [
            {
                "ticker": "SBER",
                "name": "Сбербанк",
                "quantity": 100,      # количество акций — 100
                "current_price": 280.0,  # сегодня цена 280 ₽
                "previous_price": 290.0, # вчера цена была 290 ₽
            },
            {
                "ticker": "YNDX",
                "name": "Яндекс",
                "quantity": 50,
                "current_price": 4200.0,
                "previous_price": 4300.0,
            },
            {
                "ticker": "LKOH",
                "name": "Лукойл",
                "quantity": 10,
                "current_price": 7000.0,
                "previous_price": 6900.0,
            },
        ],
    }
}


def get_portfolio(portfolio_id: str) -> dict[str, Any]:
    """Возвращает портфель и рассчитывает его показатели."""

    portfolio = MOCK_PORTFOLIOS.get(portfolio_id)

    if portfolio is None:
        raise ValueError(f"Portfolio {portfolio_id} not found")

    positions = []

    total_value = 0.0
    previous_value = 0.0

    for position in portfolio["positions"]:
        quantity = position["quantity"]
        current_price = position["current_price"]
        previous_price = position["previous_price"]

# стоимость позиции вчера — 29 000 ₽
# стоимость позиции сегодня — 28 000 ₽
        market_value = quantity * current_price
        previous_market_value = quantity * previous_price

# изменение стоимости — −1 000 ₽
        change_absolute = market_value - previous_market_value

        change_percent = (
            (current_price - previous_price) / previous_price * 100
            if previous_price != 0
            else 0.0
        )

        total_value += market_value
        previous_value += previous_market_value

        positions.append({
            **position,
            "market_value": market_value,
            "change_absolute": change_absolute,
            "change_percent": change_percent,
        })

    portfolio_change_absolute = total_value - previous_value

    portfolio_change_percent = (
        portfolio_change_absolute / previous_value * 100
        if previous_value != 0
        else 0.0
    )

    for position in positions:
        position["weight_percent"] = (
            position["market_value"] / total_value * 100
            if total_value != 0
            else 0.0
        )

        position["contribution_percent"] = (
            position["change_absolute"] / previous_value * 100
            if previous_value != 0
            else 0.0
        )

    return {
        "portfolio_id": portfolio_id,
        "currency": portfolio["currency"],
        "total_value": round(total_value, 2),
        "previous_value": round(previous_value, 2),
        "change_absolute": round(portfolio_change_absolute, 2),
        "change_percent": round(portfolio_change_percent, 2),
        "positions_count": len(positions),
        "positions": positions,
    }