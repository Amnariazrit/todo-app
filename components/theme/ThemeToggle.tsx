// components/theme/ThemeToggle.tsx
// Animated theme toggle button

'use client';

import { Moon, Sun } from 'lucide-react';
import { useTheme } from 'next-themes';
import { motion } from 'framer-motion';

import { Button } from '@/components/ui/button';

export function ThemeToggle() {
  const { theme, setTheme } = useTheme();

  return (
    <Button
      variant="ghost"
      size="icon"
      onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
      aria-label="Toggle theme"
      className="relative overflow-visible"
    >
      <motion.div
        animate={{ rotate: theme === 'dark' ? 180 : 0 }}
        transition={{ duration: 0.5, type: 'spring', stiffness: 100, damping: 15 }}
      >
        <Sun className="h-5 w-5 rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0" />
      </motion.div>
      <motion.div
        animate={{ rotate: theme === 'dark' ? 0 : -180 }}
        transition={{ duration: 0.5, type: 'spring', stiffness: 100, damping: 15 }}
        className="absolute"
      >
        <Moon className="h-5 w-5 rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100" />
      </motion.div>
    </Button>
  );
}