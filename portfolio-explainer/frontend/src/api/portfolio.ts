import { apiRequest } from "./client";

import type {
  PortfolioResponse
} from "../types/portfolio";


export function getPortfolio(
  portfolioId: string
) {
  return apiRequest<PortfolioResponse>(
    `/portfolio/${portfolioId}`
  );
}