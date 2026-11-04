const API_URL =
  import.meta.env.VITE_API_URL ??
  "http://localhost:8000/api/v1";

export async function apiRequest<T>(
  endpoint: string,
  options?: RequestInit
): Promise<T> {

  const response = await fetch(
    `${API_URL}${endpoint}`,
    {
      headers: {
        "Content-Type": "application/json",
        ...options?.headers,
      },
      ...options,
    }
  );

  if (!response.ok) {
    throw new Error(
      `API error: ${response.status}`
    );
  }

  return response.json() as Promise<T>;
}