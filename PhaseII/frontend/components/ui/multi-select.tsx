// components/ui/multi-select.tsx
// Multi-select with animated chips for tags

import * as React from 'react';

import { cn } from '@/lib/utils';

interface MultiSelectProps extends React.TextareaHTMLAttributes<HTMLTextAreaElement> {
  tags: string[];
  onTagsChange: (tags: string[]) => void;
  placeholder?: string;
}

const MultiSelect = React.forwardRef<
  HTMLTextAreaElement,
  MultiSelectProps
>(({ className, tags, onTagsChange, placeholder, ...props }, ref) => {
  const [inputValue, setInputValue] = React.useState('');

  const handleInputChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setInputValue(e.target.value);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && inputValue.trim()) {
      e.preventDefault();
      if (!tags.includes(inputValue.trim())) {
        onTagsChange([...tags, inputValue.trim()]);
      }
      setInputValue('');
    } else if (e.key === 'Backspace' && !inputValue && tags.length > 0) {
      const newTags = [...tags];
      newTags.pop();
      onTagsChange(newTags);
    }
  };

  const removeTag = (tagToRemove: string) => {
    onTagsChange(tags.filter(tag => tag !== tagToRemove));
  };

  return (
    <div className="relative">
      <div className="flex flex-wrap gap-2 mb-2">
        {tags.map((tag, index) => (
          <div 
            key={index} 
            className="flex items-center gap-1 px-3 py-1 rounded-full bg-gradient-to-r from-indigo-500/20 to-cyan-500/20 text-indigo-700 dark:text-indigo-300 text-sm"
          >
            {tag}
            <button 
              type="button"
              className="ml-1 text-xs"
              onClick={() => removeTag(tag)}
            >
              ×
            </button>
          </div>
        ))}
      </div>
      <textarea
        ref={ref}
        className={cn(
          'flex min-h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50',
          className
        )}
        placeholder={placeholder}
        value={inputValue}
        onChange={handleInputChange}
        onKeyDown={handleKeyDown}
        rows={2}
        {...props}
      />
    </div>
  );
});
MultiSelect.displayName = 'MultiSelect';

export { MultiSelect };