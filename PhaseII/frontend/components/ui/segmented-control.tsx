// components/ui/segmented-control.tsx
// Animated segmented control for priority selection

import * as React from 'react';

import { cn } from '@/lib/utils';

interface SegmentedControlProps extends React.HTMLAttributes<HTMLDivElement> {
  options: { value: string; label: string }[];
  value: string;
  onValueChange: (value: string) => void;
}

const SegmentedControl = React.forwardRef<
  HTMLDivElement,
  SegmentedControlProps
>(({ className, options, value, onValueChange, ...props }, ref) => {
  return (
    <div
      ref={ref}
      className={cn(
        'inline-flex h-10 items-center justify-center rounded-lg bg-muted p-1 text-muted-foreground',
        className
      )}
      {...props}
    >
      {options.map((option) => (
        <button
          key={option.value}
          className={`relative inline-flex h-8 items-center justify-center whitespace-nowrap rounded-md px-3 py-1.5 text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 ${
            value === option.value
              ? 'bg-background text-foreground shadow-sm'
              : 'text-muted-foreground hover:text-foreground'
          }`}
          onClick={() => onValueChange(option.value)}
        >
          {value === option.value && (
            <span className="absolute inset-0 rounded-md bg-gradient-to-r from-indigo-500 to-cyan-500 opacity-10" />
          )}
          {option.label}
        </button>
      ))}
    </div>
  );
});
SegmentedControl.displayName = 'SegmentedControl';

export { SegmentedControl };