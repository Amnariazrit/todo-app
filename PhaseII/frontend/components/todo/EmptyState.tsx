// components/todo/EmptyState.tsx
// Beautiful empty state illustration

import { PlusCircle } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { motion } from 'framer-motion';

export function EmptyState() {
  return (
    <motion.div 
      className="flex flex-col items-center justify-center py-12 text-center"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <motion.div 
        className="mb-6 p-4 rounded-full bg-primary/10"
        initial={{ scale: 0 }}
        animate={{ scale: 1 }}
        transition={{ 
          type: "spring", 
          stiffness: 200, 
          damping: 15,
          delay: 0.2
        }}
      >
        {/* In a real app, we would use an actual illustration */}
        <motion.div 
          className="text-5xl"
          animate={{ rotate: [0, 10, -10, 0] }}
          transition={{ 
            duration: 4,
            repeat: Infinity,
            repeatType: "reverse",
            delay: 0.5
          }}
        >
          📋
        </motion.div>
      </motion.div>
      <motion.h3 
        className="text-xl font-semibold mb-2"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.4, duration: 0.5 }}
      >
        No tasks yet
      </motion.h3>
      <motion.p 
        className="text-muted-foreground mb-6 max-w-md"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.6, duration: 0.5 }}
      >
        Get started by creating your first task. You'll stay on top of everything in no time!
      </motion.p>
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.8, duration: 0.5 }}
      >
        <Button variant="gradient">
          <PlusCircle className="mr-2 h-4 w-4" /> Add Your First Task
        </Button>
      </motion.div>
    </motion.div>
  );
}