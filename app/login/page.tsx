// app/login/page.tsx
// Login page with premium UI

import Link from 'next/link';
import { AuthCard } from '@/components/auth/AuthCard';
import { AuthForm } from '@/components/auth/AuthForm';
import { Button } from '@/components/ui/button';

export default function LoginPage() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-500 via-purple-500 to-cyan-500 p-4">
      <AuthCard>
        <div className="text-center mb-6">
          <h1 className="text-3xl font-bold bg-gradient-to-r from-indigo-600 to-cyan-500 bg-clip-text text-transparent">
            Welcome Back
          </h1>
          <p className="text-muted-foreground mt-2">
            Sign in to your account
          </p>
        </div>
        
        <AuthForm type="login" />
        
        <div className="mt-6 text-center text-sm">
          Don't have an account?{' '}
          <Link href="/signup" className="font-medium underline">
            Sign up
          </Link>
        </div>
      </AuthCard>
    </div>
  );
}