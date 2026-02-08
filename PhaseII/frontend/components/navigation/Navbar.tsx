// components/navigation/Navbar.tsx
// Glass navbar with theme toggle

import Link from 'next/link';
import { ThemeToggle } from '@/components/theme/ThemeToggle';
import { Button } from '@/components/ui/button';

export function Navbar() {
  return (
    <nav className="glass-theme border-b backdrop-blur-md sticky top-0 z-10">
      <div className="container flex h-16 items-center justify-between px-4">
        <Link href="/" className="flex items-center gap-2">
          <div className="h-8 w-8 rounded-full bg-gradient-to-r from-indigo-500 to-cyan-500"></div>
          <span className="text-xl font-bold bg-gradient-to-r from-indigo-600 to-cyan-500 bg-clip-text text-transparent">
            TodoApp
          </span>
        </Link>
        
        <div className="flex items-center gap-4">
          <ThemeToggle />
          
          <div className="relative">
            <Button variant="ghost" size="icon" className="rounded-full">
              <div className="h-8 w-8 rounded-full bg-muted"></div>
            </Button>
          </div>
        </div>
      </div>
    </nav>
  );
}