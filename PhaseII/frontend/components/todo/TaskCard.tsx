// components/todo/TaskCard.tsx
// Premium task card with animations

'use client';

import { useState } from 'react';
import { motion } from 'framer-motion';
import { Check, MoreHorizontal, Edit3, Save, X } from 'lucide-react';
import { Card, CardContent } from '@/components/ui/card';
import { getPriorityColor } from '@/lib/utils';

interface TaskCardProps {
  id: string;
  title: string;
  description?: string;
  priority: 'low' | 'medium' | 'high';
  tags: string[];
  completed: boolean;
  onToggleComplete: (id: string) => void;
  onUpdate: (id: string, updates: Partial<{ title: string; description: string; priority: string; tags: string[] }>) => void;
  onDelete: (id: string) => void;
}

export function TaskCard({
  id,
  title,
  description,
  priority,
  tags,
  completed,
  onToggleComplete,
  onUpdate,
  onDelete
}: TaskCardProps) {
  const [isEditing, setIsEditing] = useState(false);
  const [editTitle, setEditTitle] = useState(title);
  const [editDescription, setEditDescription] = useState(description || '');

  const handleEdit = () => {
    setIsEditing(true);
  };

  const handleSave = () => {
    onUpdate(id, {
      title: editTitle,
      description: editDescription
    });
    setIsEditing(false);
  };

  const handleCancel = () => {
    setEditTitle(title);
    setEditDescription(description || '');
    setIsEditing(false);
  };

  const handleDelete = () => {
    onDelete(id);
  };

  if (isEditing) {
    return (
      <motion.div
        layout
        initial={{ opacity: 0, scale: 0.8 }}
        animate={{ opacity: 1, scale: 1 }}
        exit={{ opacity: 0, scale: 0.8 }}
        transition={{ type: 'spring', stiffness: 300, damping: 25 }}
      >
        <Card
          variant="glass"
          className="overflow-hidden group relative transition-all duration-300"
        >
          <CardContent className="p-4">
            <div className="space-y-3">
              <div className="flex items-center gap-3">
                <div className="relative">
                  <input
                    type="checkbox"
                    checked={completed}
                    onChange={() => onToggleComplete(id)}
                    className="mt-1 h-5 w-5 rounded-full border-gray-300 focus:ring-2 focus:ring-indigo-500 opacity-0 absolute cursor-pointer z-10"
                  />
                  <div
                    className={`flex items-center justify-center h-5 w-5 rounded-full border-2 transition-all duration-200 ${
                      completed
                        ? 'bg-gradient-to-r from-green-400 to-cyan-500 border-transparent'
                        : 'border-gray-400 dark:border-gray-500 group-hover:border-indigo-400 dark:group-hover:border-indigo-300'
                    }`}
                    onClick={() => onToggleComplete(id)}
                  >
                    {completed && (
                      <motion.div
                        initial={{ scale: 0 }}
                        animate={{ scale: 1 }}
                        transition={{ type: 'spring', stiffness: 500, damping: 30 }}
                      >
                        <Check className="h-3 w-3 text-white" />
                      </motion.div>
                    )}
                  </div>
                </div>
                <input
                  type="text"
                  value={editTitle}
                  onChange={(e) => setEditTitle(e.target.value)}
                  className="flex-1 font-semibold bg-transparent border-b border-gray-300 dark:border-gray-600 focus:outline-none focus:border-indigo-500"
                  autoFocus
                />
              </div>
              <textarea
                value={editDescription}
                onChange={(e) => setEditDescription(e.target.value)}
                className="w-full bg-transparent border border-gray-300 dark:border-gray-600 rounded-md p-2 text-sm resize-none focus:outline-none focus:ring-1 focus:ring-indigo-500"
                rows={2}
              />
              <div className="flex justify-end space-x-2 pt-2">
                <button 
                  className="p-1 rounded-full hover:bg-gray-200/30 dark:hover:bg-gray-700/30"
                  onClick={handleCancel}
                >
                  <X className="h-4 w-4 text-gray-500 dark:text-gray-400" />
                </button>
                <button 
                  className="p-1 rounded-full hover:bg-gray-200/30 dark:hover:bg-gray-700/30"
                  onClick={handleSave}
                >
                  <Save className="h-4 w-4 text-gray-500 dark:text-gray-400" />
                </button>
              </div>
            </div>
          </CardContent>
        </Card>
      </motion.div>
    );
  }

  return (
    <motion.div
      layout
      initial={{ opacity: 0, scale: 0.8 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.8 }}
      whileHover={{ y: -8, boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.25)' }}
      transition={{ type: 'spring', stiffness: 300, damping: 25 }}
    >
      <Card
        variant="glass"
        className={`overflow-hidden group relative transition-all duration-300 ${
          completed ? 'opacity-70 bg-opacity-80' : 'hover:scale-[1.02]'
        }`}
      >
        <CardContent className="p-4">
          <div className="flex items-start gap-3">
            <div className="relative">
              <input
                type="checkbox"
                checked={completed}
                onChange={() => onToggleComplete(id)}
                className="mt-1 h-5 w-5 rounded-full border-gray-300 focus:ring-2 focus:ring-indigo-500 opacity-0 absolute cursor-pointer z-10"
              />
              <div
                className={`flex items-center justify-center h-5 w-5 rounded-full border-2 transition-all duration-200 ${
                  completed
                    ? 'bg-gradient-to-r from-green-400 to-cyan-500 border-transparent'
                    : 'border-gray-400 dark:border-gray-500 group-hover:border-indigo-400 dark:group-hover:border-indigo-300'
                }`}
                onClick={() => onToggleComplete(id)}
              >
                {completed && (
                  <motion.div
                    initial={{ scale: 0 }}
                    animate={{ scale: 1 }}
                    transition={{ type: 'spring', stiffness: 500, damping: 30 }}
                  >
                    <Check className="h-3 w-3 text-white" />
                  </motion.div>
                )}
              </div>
            </div>
            <div className="flex-1 min-w-0">
              <div className="flex items-center justify-between">
                <div className="flex-1">
                  <div className="flex items-center gap-2">
                    <h3 className={`font-semibold truncate ${completed ? 'line-through text-muted-foreground' : 'text-foreground'}`}>
                      {title}
                    </h3>
                    <span className={`inline-block w-3 h-3 rounded-full ${getPriorityColor(priority)}`}></span>
                  </div>
                  {description && (
                    <p className="text-sm text-muted-foreground mt-1 truncate">
                      {description}
                    </p>
                  )}
                  <div className="flex flex-wrap gap-1 mt-3">
                    {tags.map((tag, index) => (
                      <motion.span
                        key={index}
                        initial={{ opacity: 0, scale: 0.8 }}
                        animate={{ opacity: 1, scale: 1 }}
                        whileHover={{ scale: 1.05, y: -1 }}
                        whileTap={{ scale: 0.95 }}
                        className="text-xs px-2 py-1 rounded-full bg-indigo-500/10 text-indigo-600 dark:text-indigo-300 border border-indigo-500/20 transition-colors duration-200"
                      >
                        {tag}
                      </motion.span>
                    ))}
                  </div>
                </div>
                <div className="flex space-x-1 opacity-0 group-hover:opacity-100 transition-opacity">
                  <button 
                    className="p-1 rounded-full hover:bg-gray-200/30 dark:hover:bg-gray-700/30"
                    onClick={handleEdit}
                  >
                    <Edit3 className="h-4 w-4 text-gray-500 dark:text-gray-400" />
                  </button>
                  <button 
                    className="p-1 rounded-full hover:bg-gray-200/30 dark:hover:bg-gray-700/30"
                    onClick={handleDelete}
                  >
                    <MoreHorizontal className="h-4 w-4 text-gray-500 dark:text-gray-400" />
                  </button>
                </div>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
    </motion.div>
  );
}