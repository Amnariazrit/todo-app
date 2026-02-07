'use client';

import { useState, useEffect } from 'react';
import { motion, AnimatePresence, stagger, useAnimate, Variants } from 'framer-motion';
import { Plus, Sun, Moon, Bell, Search, MoreHorizontal } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { TaskManager } from '@/components/todo/TaskManager';
import { ThemeToggle } from '@/components/theme/ThemeToggle';
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar';

const container: Variants = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1
    }
  }
};

const item: Variants = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 }
};

export default function DashboardPage() {
  const [isMounted, setIsMounted] = useState(false);
  
  useEffect(() => {
    setIsMounted(true);
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-br from-background to-indigo-50/30 dark:to-gray-900/20">
      {/* Glassmorphic Navbar */}
      <motion.header 
        className="border-b bg-background/80 backdrop-blur-sm sticky top-0 z-50"
        initial={{ y: -100 }}
        animate={{ y: 0 }}
        transition={{ type: 'spring', stiffness: 100, damping: 20 }}
      >
        <div className="container flex h-16 items-center justify-between px-4">
          <div className="flex items-center space-x-4">
            <motion.div
              className="text-2xl font-bold bg-gradient-to-r from-indigo-600 to-cyan-500 bg-clip-text text-transparent"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.1 }}
            >
              TaskFlow
            </motion.div>
            
            <div className="relative hidden md:block">
              <Search className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
              <input
                type="text"
                placeholder="Search tasks..."
                className="w-64 rounded-lg border bg-white/30 dark:bg-white/10 backdrop-blur-sm pl-10 pr-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500/50 focus:border-indigo-500"
              />
            </div>
          </div>
          
          <div className="flex items-center space-x-4">
            <motion.button
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              className="relative p-2 rounded-full hover:bg-accent"
            >
              <Bell className="h-5 w-5" />
              <span className="absolute top-1 right-1 h-2 w-2 rounded-full bg-red-500"></span>
            </motion.button>
            
            <ThemeToggle />
            
            <motion.div
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
            >
              <Avatar className="h-8 w-8 cursor-pointer">
                <AvatarImage src="/placeholder-user.jpg" alt="@user" />
                <AvatarFallback>JD</AvatarFallback>
              </Avatar>
            </motion.div>
          </div>
        </div>
      </motion.header>

      <motion.main 
        className="container py-8"
        variants={container}
        initial="hidden"
        animate="show"
      >
        {/* Hero Section */}
        <motion.div 
          className="mb-12 text-center"
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2, duration: 0.5 }}
        >
          <motion.h1 
            className="text-4xl md:text-5xl font-bold bg-gradient-to-r from-indigo-600 via-purple-500 to-cyan-500 bg-clip-text text-transparent"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3, duration: 0.6 }}
          >
            Your Tasks
          </motion.h1>
          <motion.p 
            className="mt-3 text-lg text-muted-foreground max-w-2xl mx-auto"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.5, duration: 0.5 }}
          >
            Everything you need to stay organized and productive today
          </motion.p>
        </motion.div>

        {/* Task Grid/List */}
        <motion.div
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
          <TaskManager />
        </motion.div>
      </motion.main>
    </div>
  );
}