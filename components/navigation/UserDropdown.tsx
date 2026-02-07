// components/navigation/UserDropdown.tsx
// User profile dropdown

import { LogOut } from 'lucide-react';
import { Button } from '@/components/ui/button';

export function UserDropdown() {
  const handleLogout = () => {
    // Clear token from localStorage
    localStorage.removeItem('token');
    // Redirect to login
    window.location.href = '/login';
  };

  return (
    <div className="relative">
      <Button 
        variant="ghost" 
        size="icon" 
        className="rounded-full"
        onClick={handleLogout}
      >
        <LogOut className="h-5 w-5" />
      </Button>
    </div>
  );
}