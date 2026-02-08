// API utility functions
import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
});

// Add token to requests if available
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Auth API functions
export const authAPI = {
  register: (userData) => api.post('/auth/register', userData),
  login: (credentials) => api.post('/auth/login', credentials),
};

// Tasks API functions
export const tasksAPI = {
  getTasks: (userId) => api.get(`/api/${userId}/tasks`),
  createTask: (userId, taskData) => api.post(`/api/${userId}/tasks`, taskData),
  updateTask: (userId, taskId, taskData) => api.put(`/api/${userId}/tasks/${taskId}`, taskData),
  deleteTask: (userId, taskId) => api.delete(`/api/${userId}/tasks/${taskId}`),
  toggleTaskCompletion: (userId, taskId) => api.patch(`/api/${userId}/tasks/${taskId}/complete`),
};

export default api;