// app/signup/page.tsx
// Signup page with premium UI

import Link from 'next/link';
import { AuthCard } from '@/components/auth/AuthCard';
import { AuthForm } from '@/components/auth/AuthForm';

export default function SignupPage() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-500 via-purple-500 to-cyan-500 p-4">
      <AuthCard>
        <div className="text-center mb-6">
          <h1 className="text-3xl font-bold bg-gradient-to-r from-indigo-600 to-cyan-500 bg-clip-text text-transparent">
            Create Account
          </h1>
          <p className="text-muted-foreground mt-2">
            Join us today
          </p>
        </div>
        
        <AuthForm type="register" />
        
        <div className="mt-6 text-center text-sm">
          Already have an account?{' '}
          <Link href="/login" className="font-medium underline">
            Sign in
          </Link>
        </div>
      </AuthCard>
    </div>
  );
}