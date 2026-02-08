// components/todo/LoadingSkeleton.tsx
// Premium shimmer loading skeleton

import { Card } from '@/components/ui/card';
import { motion } from 'framer-motion';

export function LoadingSkeleton() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {[...Array(6)].map((_, index) => (
        <motion.div
          key={index}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ 
            duration: 0.5, 
            delay: index * 0.1 
          }}
        >
          <Card variant="glass" className="animate-pulse bg-gradient-to-br from-background/50 to-indigo-50/30 dark:to-gray-800/30">
            <div className="p-5">
              <div className="flex items-center gap-3">
                <div className="h-5 w-5 rounded-full bg-gradient-to-r from-indigo-200 to-cyan-200 dark:from-indigo-900/50 dark:to-cyan-900/50"></div>
                <div className="flex-1 space-y-2">
                  <div className="h-4 bg-gradient-to-r from-indigo-100/50 to-cyan-100/50 dark:from-indigo-900/30 dark:to-cyan-900/30 rounded w-3/4"></div>
                  <div className="h-3 bg-gradient-to-r from-indigo-100/50 to-cyan-100/50 dark:from-indigo-900/30 dark:to-cyan-900/30 rounded w-1/2"></div>
                  <div className="flex gap-1">
                    <div className="h-6 w-12 bg-gradient-to-r from-indigo-100/50 to-cyan-100/50 dark:from-indigo-900/30 dark:to-cyan-900/30 rounded-full"></div>
                    <div className="h-6 w-12 bg-gradient-to-r from-indigo-100/50 to-cyan-100/50 dark:from-indigo-900/30 dark:to-cyan-900/30 rounded-full"></div>
                  </div>
                </div>
              </div>
            </div>
          </Card>
        </motion.div>
      ))}
    </div>
  );
}