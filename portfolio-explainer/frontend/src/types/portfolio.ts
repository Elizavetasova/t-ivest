export interface Position {
  ticker: string;
  name: string;

  quantity: number;
  currency: string;

  current_price: number;
  previous_price: number;

  market_value: number;
  weight_percent: number;

  change_percent: number;
  contribution_percent: number;
}

export interface PortfolioSummary {
  portfolio_id: string;
  currency: string;

  total_value: number;
  previous_value: number;

  change_absolute: number;
  change_percent: number;

  positions_count: number;
  updated_at: string;
}

export interface PortfolioResponse {
  summary: PortfolioSummary;
  positions: Position[];
}

export interface ExplainRequest {
  question: string;
  period: "day" | "week" | "month";
}

export interface ExplanationFactor {
  ticker: string;
  name: string;

  change_percent: number;
  contribution_percent: number;

  explanation: string;
}

export interface PossibleCause {
  description: string;

  ticker?: string;

  source_urls: string[];

  confidence: "low" | "medium" | "high";
}

export interface NewsSource {
  title: string;
  url: string;
  publisher: string;

  published_at: string;

  ticker?: string;
}

export interface ExplanationResponse {
  request_id: string;
  portfolio_id: string;

  generated_at: string;

  portfolio_change_percent: number;

  summary: string;

  main_factors: ExplanationFactor[];

  possible_causes: PossibleCause[];

  sources: NewsSource[];

  limitations: string[];
}