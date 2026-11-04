# Пример использования в React

```
    import { useState } from "react";

    import { explainPortfolio } from "../api/explain";

    import type {
    ExplanationResponse
    } from "../types/portfolio";


    export function QuestionInput() {

    const [question, setQuestion] = useState("");

    const [result, setResult] =
        useState<ExplanationResponse | null>(null);

    const [loading, setLoading] = useState(false);

    async function handleSubmit() {

        setLoading(true);

        try {

        const response = await explainPortfolio(
            "demo",
            {
            question,
            period: "day"
            }
        );

        setResult(response);

        } catch (error) {

        console.error(error);

        } finally {

        setLoading(false);

        }
    }

    return (
        <div>

        <input
            value={question}
            onChange={(event) =>
            setQuestion(event.target.value)
            }
            placeholder="Почему мой портфель снизился?"
        />

        <button
            onClick={handleSubmit}
            disabled={loading}
        >
            {loading ? "Анализ..." : "Объяснить"}
        </button>

        {result && (
            <div>
            <h3>Объяснение</h3>

            <p>{result.summary}</p>
            </div>
        )}

        </div>
    );
    }
```