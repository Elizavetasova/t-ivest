# Точный REST API контракт

Для MVP реализуем три основных endpoint.

| Метод | Endpoint | Назначение |
|---|---|---|
| `GET` | `/api/v1/health` | Проверка backend |
| `GET` | `/api/v1/portfolio/{portfolio_id}` | Получение портфеля |
| `POST` | `/api/v1/portfolio/{portfolio_id}/explain` | Получение AI-объяснения |

Обратите внимание: portfolio_id передаётся в URL для объяснения, поэтому не нужно дублировать его в теле запроса.

## Endpoint 1. Health check

`GET /api/v1/health`

Ответ:

```
{
  "status": "ok"
}
```

Нужен для проверки, запущен ли backend.

## Endpoint 2. Получение портфеля

`GET /api/v1/portfolio/demo`

Ответ:

```
{
  "summary": {
    "portfolio_id": "demo",
    "currency": "RUB",
    "total_value": 100000,
    "previous_value": 102500,
    "change_absolute": -2500,
    "change_percent": -2.439,
    "positions_count": 3,
    "updated_at": "2026-11-03T15:00:00Z"
  },
  "positions": [
    {
      "ticker": "SBER",
      "name": "Сбербанк",
      "quantity": 100,
      "currency": "RUB",
      "current_price": 250,
      "previous_price": 260,
      "market_value": 25000,
      "weight_percent": 25,
      "change_percent": -3.846,
      "contribution_percent": -0.976
    }
  ]
}
```

В реальном ответе массив positions будет содержать все позиции портфеля.

## Endpoint 3. Объяснение изменений

`POST /api/v1/portfolio/demo/explain`

Запрос:

```
{
  "question": "Почему мой портфель снизился сегодня?",
  "period": "day"
}
```

Ответ:

```
{
  "request_id": "req_001",
  "portfolio_id": "demo",
  "generated_at": "2026-11-03T15:01:00Z",
  "portfolio_change_percent": -2.439,
  "summary": "Портфель снизился на 2.44%. Основной вклад в снижение внес SBER.",
  "main_factors": [
    {
      "ticker": "SBER",
      "name": "Сбербанк",
      "change_percent": -3.846,
      "contribution_percent": -0.976,
      "explanation": "Актив внес отрицательный вклад в результат портфеля."
    }
  ],
  "possible_causes": [
    {
      "description": "Обнаружена новость, потенциально связанная с движением актива.",
      "ticker": "SBER",
      "source_urls": [],
      "confidence": "low"
    }
  ],
  "sources": [],
  "limitations": [
    "Причинно-следственная связь между новостью и движением цены не подтверждена."
  ]
}
```

Здесь sources пустой, потому что пример не содержит настоящих новостей. В демонстрации с реальными источниками он должен быть заполнен.

# Полезно для тестирования endpoint:

Backend будет доступен по адресу http://localhost:8000, frontend — http://localhost:5173.

FastAPI автоматически предоставит интерактивную документацию:

http://localhost:8000/docs


___________________________________________________

## REST API-контракт — определяет, как frontend (React) и backend (FastAPI) обмениваются данными.

## Endpoint — это конкретный адрес на backend, по которому frontend может обратиться за определённой информацией или действием. (адрес, который backend предоставляет для взаимодействия с ним)

Например:
```
    http://localhost:8000/api/v1/portfolio/demo-001
```

Это endpoint, который может возвращать данные портфеля.

Backend — это серверная часть проекта. В нашем случае она работает на FastAPI.

Когда React обращается к endpoint, FastAPI принимает запрос и возвращает ответ.

```
    React (frontend)
        |
        | HTTP-запрос
        ↓
    FastAPI (backend)
        |
        | Получает данные портфеля
        ↓
    Mock-данные (тестовые данные)
        |
        | Возвращает JSON
        ↓
    React показывает портфель
```

## HTTP-методы:

| Метод | Назначение | Пример в нашем проекте |
|---|---|---|
| `GET` | Получить данные | Получить портфель |
| `POST` | Отправить данные / выполнить действие | Запросить AI-анализ портфеля |

```
        Pydantic schemas
               |
               v
        Mock Portfolio Provider
               |
               v
        GET /portfolio
               |
               v
        React Portfolio UI
               |
               v
        Portfolio Analysis
               |
               v
        POST /explain
               |
               v
        LLM integration
               |
               v
        News integration
```
То есть сначала приложение должно работать без AI вообще.

Потом добавляется AI.
