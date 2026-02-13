// components/todo/TaskManager.tsx
// Task manager component that handles state for both TaskList and TaskForm

'use client';

import { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { TaskList } from '@/components/todo/TaskList';
import { TaskForm } from '@/components/todo/TaskForm';
import { Task } from '@/lib/types';
import { apiClient } from '@/lib/api';

export function TaskManager() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchTasks = async () => {
      try {
        // Try to fetch tasks from API, fallback to mock data if API fails
        const data = await apiClient.get<Task[]>('/tasks');
        setTasks(data);
      } catch (err: any) {
        setError(err.message || 'Failed to fetch tasks');
        
        // Fallback to mock data
        const mockTasks: Task[] = [
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
        setTasks(mockTasks);
      } finally {
        setLoading(false);
      }
    };

    fetchTasks();
  }, []);

  const handleToggleComplete = async (id: string) => {
    try {
      // Update task status via API
      await apiClient.put(`/tasks/${id}`, { completed: !tasks.find(t => t.id === id)?.completed });
      
      // Update local state
      setTasks(tasks.map(task =>
        task.id === id ? { ...task, completed: !task.completed } : task
      ));
    } catch (err) {
      // If API fails, update local state anyway (optimistic update)
      setTasks(tasks.map(task =>
        task.id === id ? { ...task, completed: !task.completed } : task
      ));
    }
  };

  const handleAddTask = async (taskData: any) => {
    try {
      // Add task via API
      const newTask = await apiClient.post<Task>('/tasks', taskData);
      setTasks([newTask, ...tasks]);
    } catch (err) {
      // If API fails, create locally with random ID
      const newTask: Task = {
        id: Math.random().toString(36).substr(2, 9),
        title: taskData.title,
        description: taskData.description,
        priority: taskData.priority,
        tags: taskData.tags,
        completed: false,
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
        userId: 'user1'
      };
      setTasks([newTask, ...tasks]);
    }
  };

  const handleUpdateTask = async (id: string, updates: Partial<{ title: string; description: string; priority: Task['priority']; tags: string[] }>) => {
    try {
      // Update task via API
      const updatedTask = await apiClient.put<Task>(`/tasks/${id}`, updates);
      
      // Update local state
      setTasks(tasks.map(task =>
        task.id === id ? updatedTask : task
      ));
    } catch (err) {
      // If API fails, update local state anyway
      setTasks(tasks.map(task =>
        task.id === id ? { ...task, ...updates, updatedAt: new Date().toISOString() } : task
      ));
    }
  };

  const handleDeleteTask = async (id: string) => {
    try {
      // Delete task via API
      await apiClient.delete(`/tasks/${id}`);
      
      // Update local state
      setTasks(tasks.filter(task => task.id !== id));
    } catch (err) {
      // If API fails, remove from local state anyway
      setTasks(tasks.filter(task => task.id !== id));
    }
  };

  return (
    <>
      <TaskList
        tasks={tasks}
        loading={loading}
        error={error}
        onToggleComplete={handleToggleComplete}
        onUpdate={handleUpdateTask}
        onDelete={handleDeleteTask}
      />
      <motion.div
        className="fixed bottom-6 right-6 z-40"
        initial={{ scale: 0 }}
        animate={{ scale: 1 }}
        whileHover={{ scale: 1.1 }}
        whileTap={{ scale: 0.9 }}
        transition={{ type: 'spring', stiffness: 300, damping: 20, delay: 0.8 }}
      >
        <TaskForm onSubmit={handleAddTask} />
      </motion.div>
    </>
  );
}