// lib/mockApi.ts
// Mock API implementation for testing without backend

import { Task } from './types';

// In-memory storage for mock data
let mockTasks: Task[] = [
  {
    id: '1',
    title: 'Complete project proposal',
    description: 'Finish the proposal document for the new project',
    priority: 'high',
    tags: ['work', 'important'],
    completed: false,
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
    userId: 'user1'
  },
  {
    id: '2',
    title: 'Buy groceries',
    description: 'Get milk, eggs, bread, and fruits',
    priority: 'medium',
    tags: ['personal'],
    completed: true,
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
    userId: 'user1'
  },
  {
    id: '3',
    title: 'Schedule meeting',
    description: 'Arrange team sync for next week',
    priority: 'low',
    tags: ['work'],
    completed: false,
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
    userId: 'user1'
  }
];

let taskIdCounter = 4;

// User data for mock authentication
let mockUser = {
  id: 'user1',
  email: 'test@example.com',
  name: 'Test User',
  createdAt: new Date().toISOString(),
  updatedAt: new Date().toISOString(),
  preferences: {}
};

export const mockApiClient = {
  async get<T>(endpoint: string): Promise<T> {
    await new Promise(resolve => setTimeout(resolve, 300)); // Simulate network delay
    
    if (endpoint === '/tasks') {
      // Filter tasks for the current user (in mock, we'll just return all tasks)
      return mockTasks as unknown as T;
    }
    
    // Handle getting a specific task
    const taskId = endpoint.match(/\/tasks\/(.+)/)?.[1];
    if (taskId) {
      const task = mockTasks.find(t => t.id === taskId);
      if (!task) {
        throw new Error('Task not found');
      }
      return task as unknown as T;
    }
    
    if (endpoint === '/users/preferences') {
      return mockUser.preferences as unknown as T;
    }
    
    throw new Error(`Endpoint ${endpoint} not implemented in mock`);
  },

  async post<T>(endpoint: string, data?: any): Promise<T> {
    await new Promise(resolve => setTimeout(resolve, 500)); // Simulate network delay
    
    if (endpoint === '/tasks') {
      const newTask: Task = {
        id: taskIdCounter.toString(),
        title: data.title,
        description: data.description || '',
        priority: data.priority || 'medium',
        tags: data.tags || [],
        completed: false,
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
        userId: mockUser.id
      };
      
      taskIdCounter++;
      mockTasks.push(newTask);
      return newTask as unknown as T;
    }
    
    if (endpoint === '/auth/login') {
      // In a real scenario, we'd verify credentials
      // For mock, we'll just accept any credentials and return the mock user
      return {
        token: 'mock-token-for-testing',
        user: mockUser
      } as unknown as T;
    }
    
    if (endpoint === '/auth/register') {
      // Create a new user with the provided data
      mockUser = {
        id: `user${Date.now()}`, // Generate a unique ID
        email: data.email,
        name: data.name,
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
        preferences: {}
      };
      
      return {
        token: 'mock-token-for-testing',
        user: mockUser
      } as unknown as T;
    }
    
    throw new Error(`Endpoint ${endpoint} not implemented in mock`);
  },

  async put<T>(endpoint: string, data?: any): Promise<T> {
    await new Promise(resolve => setTimeout(resolve, 400)); // Simulate network delay
    
    const taskId = endpoint.match(/\/tasks\/(.+)/)?.[1];
    if (taskId) {
      const taskIndex = mockTasks.findIndex(t => t.id === taskId);
      if (taskIndex === -1) {
        throw new Error('Task not found');
      }
      
      const updatedTask = {
        ...mockTasks[taskIndex],
        ...data,
        updatedAt: new Date().toISOString()
      };
      
      mockTasks[taskIndex] = updatedTask;
      return updatedTask as unknown as T;
    }
    
    if (endpoint === '/users/preferences') {
      // Update user preferences
      mockUser.preferences = { ...mockUser.preferences, ...data };
      mockUser.updatedAt = new Date().toISOString();
      return mockUser.preferences as unknown as T;
    }
    
    throw new Error(`Endpoint ${endpoint} not implemented in mock`);
  },

  async delete<T>(endpoint: string): Promise<T> {
    await new Promise(resolve => setTimeout(resolve, 400)); // Simulate network delay
    
    const taskId = endpoint.match(/\/tasks\/(.+)/)?.[1];
    if (taskId) {
      const initialLength = mockTasks.length;
      mockTasks = mockTasks.filter(t => t.id !== taskId);
      
      if (mockTasks.length === initialLength) {
        throw new Error('Task not found');
      }
      
      return { message: 'Task deleted successfully' } as unknown as T;
    }
    
    throw new Error(`Endpoint ${endpoint} not implemented in mock`);
  }
};