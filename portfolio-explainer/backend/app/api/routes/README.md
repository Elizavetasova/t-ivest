# Какой backend API реализовать

Вам не нужно создавать много endpoints. Достаточно трёх:

## `GET /portfolio` 
Возвращает тестовый или реальный портфель.

## `GET /portfolio/changes` 
Возвращает:

- изменение портфеля;

- изменение позиций;

- вклад активов;

- топ-3 позиции по влиянию.

## `POST /portfolio/explain`  (Основной endpoint)

Backend выполняет:  1. Получить portfolio    2. Получить market data    3. Рассчитать portfolio changes   4. Получить новости   5. Передать данные в LLM   6. Проверить ответ    7. Вернуть результат
(Для Python используйте FastAPI и Pydantic.)

Итог:  У нас получается три независимых компонента:

Data Layer — достаёт финансовые данные.

Analysis Layer — рассчитывает фактические изменения.

AI Layer — объясняет результат человеку.
```
React
  |
  | GET portfolio
  v
FastAPI
  |
  v
Mock portfolio
  |
  v
Расчёты
  |
  v
React отображает портфель
  |
  | POST explain
  v
FastAPI
  |
  v
Explanation service
  |
  v
React отображает объяснение
```
