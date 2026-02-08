// lib/api.ts
// Centralized API client with JWT handling
import { mockApiClient } from './mockApi';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

class ApiClient {
  private baseUrl: string;

  constructor() {
    this.baseUrl = API_BASE_URL;
  }

  private async request<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<T> {
    // Try to use the real API first, fall back to mock if it fails
    try {
      const url = `${this.baseUrl}${endpoint}`;

      const config: RequestInit = {
        headers: {
          'Content-Type': 'application/json',
          ...options.headers,
        },
        ...options,
      };

      // Add JWT token if available
      const token = localStorage.getItem('token');
      if (token) {
        config.headers = {
          ...config.headers,
          'Authorization': `Bearer ${token}`,
        };
      }

      const response = await fetch(url, config);

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.message || `HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.warn(`API request failed: ${endpoint}. Falling back to mock API.`);
      console.warn('Error details:', error);
      
      // Route to appropriate mock API method based on the request
      const method = options.method || 'GET';
      switch (method) {
        case 'GET':
          return mockApiClient.get<T>(endpoint);
        case 'POST':
          return mockApiClient.post<T>(endpoint, options.body ? JSON.parse(options.body as string) : undefined);
        case 'PUT':
          return mockApiClient.put<T>(endpoint, options.body ? JSON.parse(options.body as string) : undefined);
        case 'DELETE':
          return mockApiClient.delete<T>(endpoint);
        default:
          throw new Error(`Unsupported method: ${method}`);
      }
    }
  }

  get<T>(endpoint: string, options?: RequestInit) {
    return this.request<T>(endpoint, { ...options, method: 'GET' });
  }

  post<T>(endpoint: string, data?: any, options?: RequestInit) {
    return this.request<T>(endpoint, {
      ...options,
      method: 'POST',
      body: JSON.stringify(data),
    });
  }

  put<T>(endpoint: string, data?: any, options?: RequestInit) {
    return this.request<T>(endpoint, {
      ...options,
      method: 'PUT',
      body: JSON.stringify(data),
    });
  }

  delete<T>(endpoint: string, options?: RequestInit) {
    return this.request<T>(endpoint, { ...options, method: 'DELETE' });
  }
}

export const apiClient = new ApiClient();

export default ApiClient;