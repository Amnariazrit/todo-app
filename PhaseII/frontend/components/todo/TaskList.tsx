// components/todo/TaskList.tsx
// Responsive grid/list for tasks

'use client';

import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { TaskCard } from '@/components/todo/TaskCard';
import { EmptyState } from '@/components/todo/EmptyState';
import { LoadingSkeleton } from '@/components/todo/LoadingSkeleton';
import { Task } from '@/lib/types';
import { apiClient } from '@/lib/api';

interface TaskListProps {
  tasks: Task[];
  loading: boolean;
  error: string | null;
  onToggleComplete: (id: string) => void;
  onUpdate: (id: string, updates: Partial<{ title: string; description: string; priority: string; tags: string[] }>) => void;
  onDelete: (id: string) => void;
}

export function TaskList({ 
  tasks, 
  loading, 
  error, 
  onToggleComplete, 
  onUpdate, 
  onDelete 
}: TaskListProps) {

  if (loading) {
    return <LoadingSkeleton />;
  }

  if (error) {
    return <div className="text-center text-red-500 py-10">Error: {error}</div>;
  }

  if (tasks.length === 0) {
    return <EmptyState />;
  }

  return (
    <motion.div
      className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
      initial="hidden"
      animate="show"
      variants={{
        hidden: { opacity: 0 },
        show: {
          opacity: 1,
          transition: {
            staggerChildren: 0.1
          }
        }
      }}
    >
      <AnimatePresence>
        {tasks.map((task, index) => (
          <motion.div
            key={task.id}
            initial={{ opacity: 0, y: 20, scale: 0.95 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: -20, scale: 0.95 }}
            transition={{
              duration: 0.4,
              delay: index * 0.1,
              type: "spring",
              stiffness: 100,
              damping: 15
            }}
            layout
            variants={{
              hidden: { opacity: 0, y: 20 },
              show: { opacity: 1, y: 0 }
            }}
          >
            <TaskCard
              id={task.id}
              title={task.title}
              description={task.description}
              priority={task.priority}
              tags={task.tags}
              completed={task.completed}
              onToggleComplete={onToggleComplete}
              onUpdate={onUpdate}
              onDelete={onDelete}
            />
          </motion.div>
        ))}
      </AnimatePresence>
    </motion.div>
  );
}