```

        portfolio-explainer/
        │
        ├── frontend/
        │   ├── public/
        │   │
        │   ├── src/
        │   │   ├── api/
        │   │   │   ├── client.ts
        │   │   │   ├── portfolio.ts
        │   │   │   └── explain.ts
        │   │   │
        │   │   ├── components/
        │   │   │   ├── PortfolioSummary.tsx
        │   │   │   ├── PositionTable.tsx
        │   │   │   ├── QuestionInput.tsx
        │   │   │   ├── ExplanationCard.tsx
        │   │   │   └── NewsSources.tsx
        │   │   │
        │   │   ├── types/
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
        │   │   │   ├── routes/
        │   │   │   │   ├── portfolio.py
        │   │   │   │   └── explain.py
        │   │   │   └── dependencies.py
        │   │   │
        │   │   ├── schemas/
        │   │   │   ├── portfolio.py
        │   │   │   ├── explanation.py
        │   │   │   └── common.py
        │   │   │
        │   │   ├── services/
        │   │   │   ├── portfolio_service.py
        │   │   │   ├── analysis_service.py
        │   │   │   ├── news_service.py
        │   │   │   └── explanation_service.py
        │   │   │
        │   │   ├── providers/
        │   │   │   ├── base.py
        │   │   │   ├── mock_provider.py
        │   │   │   └── tinvest_provider.py
        │   │   │
        │   │   ├── repositories/
        │   │   │   └── portfolio_repository.py
        │   │   │
        │   │   └── config.py
        │   │
        │   ├── tests/
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