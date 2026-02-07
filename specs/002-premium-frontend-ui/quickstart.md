# Quickstart Guide: Premium Frontend UI

## Prerequisites
- Node.js 18.x or later
- npm or yarn package manager
- Git for version control

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd todo-frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Set up environment variables**
   Create a `.env.local` file in the root directory:
   ```
   NEXT_PUBLIC_API_URL=https://api.todo-app.com/v1
   NEXT_PUBLIC_JWT_SECRET=your-jwt-secret
   ```

4. **Run the development server**
   ```bash
   npm run dev
   # or
   yarn dev
   ```

5. **Open your browser**
   Visit [http://localhost:3000](http://localhost:3000) to see the application

## Key Scripts

- `npm run dev` - Start development server with hot reloading
- `npm run build` - Build the application for production
- `npm run start` - Start the production server
- `npm run lint` - Run ESLint to check for code issues
- `npm run type-check` - Run TypeScript type checking

## Project Structure

```
/app
  /layout.tsx                    # Root layout with theme provider
  /page.tsx                      # Landing page
  /login/page.tsx                # Login page with premium UI
  /signup/page.tsx               # Signup page with premium UI
  /dashboard
    /page.tsx                    # Main dashboard with task list
  /globals.css                   # Global styles and Tailwind directives
/components
  /ui                            # shadcn/ui components with custom variants
    /button.tsx                  # Gradient button variant
    /card.tsx                    # Glassmorphic card variant
    /input.tsx                   # Animated input with floating label
    /dialog.tsx                  # Glassmorphic modal variant
    /switch.tsx                  # Animated theme toggle
    /[other-shadcn-components]    # Other customized components
  /auth                          # Authentication components
    /AuthCard.tsx                # Centered glass card for auth
    /AuthForm.tsx                # Animated auth form
  /todo                          # Task-related components
    /TaskCard.tsx                # Glassmorphic task card with hover effects
    /TaskList.tsx                # Responsive grid/list for tasks
    /TaskForm.tsx                # Animated modal form for tasks
    /EmptyState.tsx              # Beautiful empty state illustration
    /LoadingSkeleton.tsx         # Premium shimmer loading skeleton
  /navigation                    # Navigation components
    /Navbar.tsx                  # Glass navbar with theme toggle
    /UserDropdown.tsx            # User profile dropdown
  /theme                         # Theme-related components
    /ThemeProvider.tsx           # Theme context provider
    /ThemeToggle.tsx             # Animated theme toggle button
/lib
  /api.ts                        # Centralized API client with JWT handling
  /types.ts                      # Shared TypeScript types
  /utils.ts                      # Utility functions
/styles
  /globals.css                   # Global styles
  /themes.css                    # Theme-specific styles
```

## Key Technologies Used

- **Next.js 16+**: React framework with App Router
- **TypeScript**: Type-safe JavaScript
- **Tailwind CSS**: Utility-first CSS framework
- **shadcn/ui**: Accessible UI components
- **Framer Motion**: Production-ready animations
- **Lucide React**: Beautiful icon library
- **React Hook Form**: Forms with easy validation
- **Zod**: Schema validation

## Premium UI Features

- Glassmorphism effects with backdrop blur
- Smooth gradient backgrounds and elements
- Subtle animations and micro-interactions
- Responsive design for all device sizes
- Dark/light theme with seamless switching
- Loading skeletons with shimmer effects
- Animated empty states with illustrations

## API Integration

The frontend communicates with the backend API through a centralized client located at `/lib/api.ts`. This client automatically attaches JWT tokens to requests and handles common error scenarios.

Example API call:
```typescript
import { apiClient } from '@/lib/api';

// Fetch user's tasks
const tasks = await apiClient.get('/tasks');
```

## Theming

The application supports both light and dark themes with smooth transitions. The theme is managed through a React Context and CSS variables. Users can toggle between themes using the theme switch in the navbar.