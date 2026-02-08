// app/auth/page.tsx
// Combined authentication page with slide animation

'use client';

import { useState } from 'react';
import Link from 'next/link';
import { motion } from 'framer-motion';
import { AuthCard } from '@/components/auth/AuthCard';
import { AuthForm } from '@/components/auth/AuthForm';
import { Button } from '@/components/ui/button';

export default function AuthPage() {
  const [isLoginView, setIsLoginView] = useState(true);

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-500 via-purple-500 to-cyan-500 p-4">
      <AuthCard>
        <div className="text-center mb-6">
          <h1 className="text-3xl font-bold bg-gradient-to-r from-indigo-600 to-cyan-500 bg-clip-text text-transparent">
            {isLoginView ? 'Welcome Back' : 'Create Account'}
          </h1>
          <p className="text-muted-foreground mt-2">
            {isLoginView ? 'Sign in to your account' : 'Join us today'}
          </p>
        </div>
        
        <motion.div
          key={isLoginView ? 'login' : 'signup'}
          initial={{ x: isLoginView ? -300 : 300, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          exit={{ x: isLoginView ? 300 : -300, opacity: 0 }}
          transition={{ type: 'spring', damping: 25, stiffness: 300 }}
        >
          <AuthForm type={isLoginView ? 'login' : 'register'} />
        </motion.div>
        
        <div className="mt-6 text-center text-sm">
          {isLoginView ? "Don't have an account? " : "Already have an account? "}
          <Button
            variant="link"
            className="p-0 h-auto font-medium"
            onClick={() => setIsLoginView(!isLoginView)}
          >
            {isLoginView ? 'Sign up' : 'Sign in'}
          </Button>
        </div>
      </AuthCard>
    </div>
  );
}