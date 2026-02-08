// components/auth/AuthCard.tsx
// Centered glass card for authentication

import { Card, CardContent } from '@/components/ui/card';

interface AuthCardProps {
  children: React.ReactNode;
  className?: string;
}

export function AuthCard({ children, className }: AuthCardProps) {
  return (
    <Card 
      variant="glass" 
      className={`w-full max-w-md mx-auto p-0 overflow-hidden ${className}`}
    >
      <CardContent className="p-8">
        {children}
      </CardContent>
    </Card>
  );
}