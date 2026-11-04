import { apiRequest } from "./client";

import type {
  ExplainRequest,
  ExplanationResponse
} from "../types/portfolio";


export function explainPortfolio(
  portfolioId: string,
  request: ExplainRequest
) {
  return apiRequest<ExplanationResponse>(
    `/portfolio/${portfolioId}/explain`,
    {
      method: "POST",
      body: JSON.stringify(request),
    }
  );
}