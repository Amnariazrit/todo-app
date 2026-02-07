// components/auth/AuthForm.tsx
// Animated auth form

'use client';

import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { useRouter } from 'next/navigation';

import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { apiClient } from '@/lib/api';
import { LoginRequest, RegisterRequest } from '@/lib/types';

interface AuthFormProps {
  type: 'login' | 'register';
}

const loginSchema = z.object({
  email: z.string().email('Invalid email address'),
  password: z.string().min(6, 'Password must be at least 6 characters'),
});

const registerSchema = z.object({
  email: z.string().email('Invalid email address'),
  password: z.string().min(6, 'Password must be at least 6 characters'),
  name: z.string().min(1, 'Name is required'),
});

export function AuthForm({ type }: AuthFormProps) {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const router = useRouter();

  // Use different form schemas based on type
  const schema = type === 'login' ? loginSchema : registerSchema;
  
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: zodResolver(schema),
  });

  const onSubmit = async (data: any) => {
    setIsLoading(true);
    setError(null);

    try {
      let response;
      if (type === 'login') {
        response = await apiClient.post<LoginRequest>('/auth/login', data);
      } else {
        response = await apiClient.post<RegisterRequest>('/auth/register', data);
      }

      // Store token in localStorage
      localStorage.setItem('token', response.token);
      
      // Redirect to dashboard
      router.push('/dashboard');
      router.refresh(); // Refresh to update auth state
    } catch (err: any) {
      setError(err.message || 'An error occurred during authentication');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      {type === 'register' && (
        <div>
          <Input
            id="name"
            placeholder="Name"
            {...register('name' as any)}
            className={`${(errors as any).name ? 'border-red-500' : ''}`}
          />
          {(errors as any).name && (
            <p className="mt-1 text-sm text-red-500">{((errors as any).name.message as string)}</p>
          )}
        </div>
      )}

      <div>
        <Input
          id="email"
          type="email"
          placeholder="Email"
          {...register('email' as any)}
          className={`${(errors as any).email ? 'border-red-500' : ''}`}
        />
        {(errors as any).email && (
          <p className="mt-1 text-sm text-red-500">{((errors as any).email.message as string)}</p>
        )}
      </div>

      <div>
        <Input
          id="password"
          type="password"
          placeholder="Password"
          {...register('password' as any)}
          className={`${(errors as any).password ? 'border-red-500' : ''}`}
        />
        {(errors as any).password && (
          <p className="mt-1 text-sm text-red-500">{((errors as any).password.message as string)}</p>
        )}
      </div>

      {error && <p className="text-sm text-red-500">{error}</p>}

      <Button 
        type="submit" 
        className="w-full" 
        variant="gradient"
        disabled={isLoading}
      >
        {isLoading ? 'Processing...' : type === 'login' ? 'Sign In' : 'Sign Up'}
      </Button>
    </form>
  );
}