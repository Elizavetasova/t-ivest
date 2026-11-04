```

        portfolio-explainer/
        │
        ├── frontend/
        │   ├── public/
        │   │
        │   ├── src/
        │   │   ├── api/   # HTTP-запросы к backend
        │   │   │   ├── client.ts
        │   │   │   ├── portfolio.ts
        │   │   │   └── explain.ts
        │   │   │
        │   │   ├── components/   # UI-компоненты
        │   │   │   ├── PortfolioSummary.tsx
        │   │   │   ├── PositionTable.tsx
        │   │   │   ├── QuestionInput.tsx
        │   │   │   ├── ExplanationCard.tsx
        │   │   │   └── NewsSources.tsx
        │   │   │
        │   │   ├── types/   # TypeScript-интерфейсы
        │   │   │   └── portfolio.ts
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
        │   │   ├── main.py
        │   │   │
        │   │   ├── api/
        │   │   │   ├── routes/   # REST endpoints   (API routes не должны содержать финансовые расчёты или логику работы с LLM.
        │   │   │   │   ├── portfolio.py   #            Они только принимают запрос, вызывают service и возвращают результат.)
        │   │   │   │   └── explain.py
        │   │   │   └── dependencies.py
        │   │   │
        │   │   ├── schemas/   # Pydantic-модели
        │   │   │   ├── portfolio.py   # Модели данных Pydantic - Используем Pydantic v2.
        │   │   │   ├── explanation.py   # Модель запроса на объяснение
        │   │   │   └── common.py
        │   │   │
        │   │   ├── services/   # Логика приложения
        │   │   │   ├── portfolio_service.py
        │   │   │   ├── analysis_service.py
        │   │   │   ├── news_service.py
        │   │   │   └── explanation_service.py
        │   │   │
        │   │   ├── providers/   # Источники финансовых данных
        │   │   │   ├── base.py
        │   │   │   ├── mock_provider.py
        │   │   │   └── tinvest_provider.py
        │   │   │
        │   │   ├── repositories/   # 	Работа с данными
        │   │   │   └── portfolio_repository.py
        │   │   │
        │   │   └── config.py
        │   │
        │   ├── tests/   # Тесты
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
        │   └── api-contract.md
        │
        ├── .gitignore
        ├── README.md
        └── docker-compose.yml

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
