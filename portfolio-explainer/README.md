# Portfolio Explainer

AI-agent for explaining changes in investment portfolios.

## Architecture

- React + TypeScript
- Python + FastAPI
- Pydantic
- T-Invest API
- LLM API

## Features

- Portfolio overview
- Position analysis
- Portfolio change explanation
- Financial news integration
- Source-backed AI explanations

## Development

### Backend

cd backend

pip install -r requirements.txt

uvicorn app.main:app --reload

### Frontend

cd frontend

npm install

npm run dev

```

        portfolio-explainer/
        │
        ├── frontend/
        │   ├── public/
        │   │
        │   ├── src/
        │   │   ├── api/                                   # HTTP-запросы к backend:
        │   │   │   ├── client.ts                 # HTTP-клиент для обращения к backend
        │   │   │   ├── portfolio.ts              # Функция получения портфеля
        │   │   │   └── explain.ts                # Функция отправки запроса на объяснение
        │   │   │
        │   │   ├── components/                            # UI-компоненты
        │   │   │   ├── PortfolioSummary.tsx
        │   │   │   ├── PositionTable.tsx
        │   │   │   ├── QuestionInput.tsx
        │   │   │   ├── ExplanationCard.tsx
        │   │   │   └── NewsSources.tsx
        │   │   │
        │   │   ├── types/                                 # TypeScript-интерфейсы:
        │   │   │   └── portfolio.ts              # TypeScript-типы для данных портфеля
        │   │   │
        │   │   ├── hooks/
        │   │   │   └── usePortfolio.ts
        │   │   │
        │   │   ├── pages/
        │   │   │   └── PortfolioPage.tsx
        │   │   │
        │   │   ├── App.tsx
        │   │   └── main.tsx
        │   │
        │   ├── .env.example
        │   ├── package.json
        │   └── vite.config.ts
        │
        ├── backend/
        │   ├── app/                                       
        │   │   ├── main.py                                # FastAPI
        │   │   │
        │   │   ├── api/
        │   │   │   ├── routes/                            # REST endpoints:
        │   │   │   │   ├── portfolio.py          # Endpoint портфеля    
        │   │   │   │   └── explain.py            # Endpoint объяснения
        │   │   │   └── dependencies.py
        │   │   │
        │   │   ├── schemas/                               # Pydantic-модели
        │   │   │   ├── portfolio.py              # Pydantic: описание структуры данных портфеля 
        │   │   │   ├── explanation.py            # Pydantic: описание структуры запроса на объяснение и ответа с результатом анализа
        │   │   │   └── common.py
        │   │   │
        │   │   ├── services/                              # Логика приложения:
        │   │   │   ├── portfolio_service.py      # Mock-портфель и расчёты
        │   │   │   ├── analysis_service.py
        │   │   │   ├── news_service.py
        │   │   │   └── explanation_service.py    # Объяснение пока что без LLM
        │   │   │
        │   │   ├── providers/                             # Источники финансовых данных
        │   │   │   ├── base.py
        │   │   │   ├── mock_provider.py
        │   │   │   └── tinvest_provider.py
        │   │   │
        │   │   ├── repositories/                          # Работа с данными
        │   │   │   └── portfolio_repository.py
        │   │   │
        │   │   └── config.py
        │   │
        │   ├── tests/                                     # Тесты
        │   │   ├── test_portfolio.py
        │   │   ├── test_analysis.py
        │   │   └── test_explanation.py
        │   │
        │   ├── requirements.txt
        │   └── .env.example
        │
        ├── data/
        │   └── demo_portfolio.json
        │
        ├── docs/
        │   ├── architecture.md
        │   └── api-contract.md                            # REST-контракт
        │
        ├── .gitignore
        ├── README.md                                      # Документация проекта
        └── docker-compose.yml


# (API routes не должны содержать финансовые расчёты или логику работы с LLM.    
# Они только принимают запрос, вызывают service и возвращают результат.)

# Модели данных Pydantic - Используем Pydantic v2.

# В текущей реализации mock-данные находятся непосредственно в сервисе
# — отдельный mock_portfolio.json в рассмотренной версии не используется.
```

| Компонент | Технология | Почему |
|---|---|---|
| Frontend | React + TypeScript + Vite | Быстро собрать интерактивный интерфейс |
| UI | Tailwind + shadcn/ui | Готовые компоненты |
| Backend | Python + FastAPI | Удобно для финансовых расчётов и AI |
| Финансовые вычисления | Python + pandas | Работа с табличными данными |
| Интеграция с брокером | T-Invest API / MCP | Получение портфеля и котировок |
| Новости | News API или финансовый news feed | Поиск событий по компаниям |
| LLM | OpenAI API | Генерация объяснений |
| Валидация данных | Pydantic | Проверка структуры |
| Хранение | JSON / SQLite | MVP не требует сложной базы |


