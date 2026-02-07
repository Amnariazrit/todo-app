# speckit.plan
## Phase II – Frontend Technical Plan (Premium & Eye-Catching UI)
### Todo Web App – Next.js Frontend

### 1. Overall Architecture

The frontend architecture follows Next.js 16+ App Router conventions with a focus on premium UI components and smooth user experiences. The architecture consists of:

- **Global Layout**: Root layout with theme provider and global styles
- **Authentication Wrapper**: Protected routes for authenticated users only
- **Component Architecture**: Reusable premium UI components with consistent styling
- **State Management**: Client-side state for UI interactions, server components for initial data
- **API Integration**: Centralized API client with JWT token handling

The architecture emphasizes performance with server components for initial rendering and client components for interactivity, ensuring optimal loading times while maintaining rich UI interactions.

### 2. File Structure (Frontend only)

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
/hooks                           # Custom hooks
  /useTheme.ts                   # Theme management hook
  /useAuth.ts                    # Authentication state hook
/public                          # Static assets
  /icons                         # Icon assets
  /illustrations                 # Illustration assets for empty states
```

### 3. Global Design System & Theme

#### Tailwind Configuration
- **Custom Colors**: Indigo, purple, cyan gradients for primary accents
- **Glassmorphism Utilities**: Backdrop blur, semi-transparent backgrounds
- **Shadow Presets**: Soft shadows for premium feel
- **Animation Presets**: Subtle transitions and hover effects

#### Theme Provider
- **Dark/Light Mode**: Context-based theme switching with system preference detection
- **CSS Variables**: Dynamic color variables that update based on theme
- **Transition Effects**: Smooth theme transitions with 300ms duration

#### shadcn/ui Custom Variants
- **Button Variants**: Gradient backgrounds, hover effects, ripple animations
- **Card Variants**: Glassmorphic styling with backdrop blur
- **Input Variants**: Floating labels, gradient focus rings, smooth transitions
- **Dialog Variants**: Slide-up animations, glass backgrounds

### 4. Key Components Breakdown

#### Navbar (glass + animated toggle)
- **Structure**: Glassmorphic bar with logo on left, user avatar and theme toggle on right
- **Functionality**: Theme toggle with sun/moon animation, user dropdown with logout
- **Styling**: Backdrop blur, semi-transparent background, subtle border
- **Animations**: Smooth theme transition, hover effects on interactive elements

#### TaskCard (glass card + hover lift + priority glow + animated complete)
- **Structure**: Glassmorphic card with task title, description, priority badge, tags
- **Interactions**: Hover lift effect (scale 1.02), shadow enhancement
- **Priority Badges**: Glowing badges with color coding (red/orange/green)
- **Complete Toggle**: Animated checkmark with subtle confetti effect
- **Styling**: Consistent glassmorphism, proper spacing, responsive design

#### TaskList (grid responsive + fade-in stagger)
- **Layout**: Responsive grid (1 column on mobile, 2 on tablet, 3 on desktop)
- **Animations**: Staggered fade-in for each task card on load
- **Empty State**: Beautiful illustration with pulsing CTA button when no tasks
- **Loading State**: Premium skeleton screens with shimmer effect

#### TaskForm/Modal (slide-up + gradient submit + animated inputs)
- **Structure**: Glassmorphic modal with form fields for task creation/editing
- **Animations**: Slide-up entrance, slide-down exit
- **Form Fields**: Animated inputs with floating labels, gradient focus rings
- **Priority Selector**: Animated segmented control with color shifts
- **Tag Selector**: Multi-select with colorful animated chips
- **Submit Button**: Gradient background, ripple effect, loading spinner

#### EmptyState (illustration + pulse CTA)
- **Visuals**: Beautiful illustration representing the empty state
- **CTA Button**: Gradient button with pulse animation to draw attention
- **Messaging**: Clear, friendly text encouraging user action

#### LoadingSkeleton (shimmer premium effect)
- **Design**: Premium skeleton elements mimicking actual UI components
- **Animation**: Shimmer effect moving across elements
- **Performance**: Fast loading perception with smooth transitions to actual content

### 5. Animation & Interaction Plan

#### Framer Motion Implementation
- **Page Transitions**: Fade-in transitions between pages
- **Component Entrance**: Staggered animations for lists and grids
- **Hover Effects**: Scale and shadow enhancements for interactive elements
- **Micro-interactions**: Button presses, form interactions, toggle switches

#### Specific Animations
- **Task Card Entrance**: Fade-in with slight scale-up (duration: 300ms, delay: staggered)
- **Checkbox Confetti**: Subtle confetti effect when task is completed
- **Modal Slide-up**: Smooth slide-up animation for modals (duration: 250ms)
- **Theme Transition**: Smooth color transition when switching themes (duration: 300ms)
- **Button Ripple**: Radial ripple effect on button click
- **Input Focus**: Gradient border animation and floating label movement

#### Performance Considerations
- **Reduced Motion**: Respect user's reduced motion preferences
- **Mobile Optimizations**: Lighter animations on mobile devices
- **Frame Rate**: Maintain 60fps for all animations
- **Cleanup**: Proper cleanup of animation resources

### 6. Authentication Flow (UI only)

#### Login Page
- **Layout**: Full-screen background gradient with centered glass card
- **Form Elements**: Animated inputs with floating labels, gradient submit button
- **Social Login**: Social login buttons if available
- **Toggle**: Smooth slide animation to switch between login and signup

#### Signup Page
- **Layout**: Same as login but with additional fields
- **Form Validation**: Real-time validation with elegant error display
- **Privacy Notice**: Clear privacy and terms information

#### Protected Routes
- **Wrapper Component**: Higher-order component for protecting routes
- **Redirect Logic**: Redirect to login if not authenticated
- **Smooth Transitions**: Animated transitions between auth states

### 7. Data Fetching & State

#### Server Components
- **Initial Data**: Fetch initial task list on server for faster initial render
- **User Info**: Retrieve user information on server for personalized experience
- **Metadata**: Server-rendered metadata for SEO

#### Client Components
- **Form Interactions**: Client-side state for form inputs and validation
- **UI State**: Theme preferences, modal states, loading states
- **Real-time Updates**: Handle task updates without full page refresh

#### API Client Setup
- **Centralized Client**: Single API client in `/lib/api.ts` for all requests
- **JWT Handling**: Automatic attachment of JWT token to requests
- **Error Handling**: Consistent error handling with user-friendly messages
- **Loading States**: Proper loading states during API requests

### 8. Implementation Order Recommendation

1. **Theme System**: Set up Tailwind configuration and theme provider
2. **Base Components**: Customize shadcn/ui components with premium styling
3. **Layout Components**: Create navbar and global layout
4. **Authentication Pages**: Build login/signup with premium UI
5. **Dashboard Layout**: Create dashboard page structure
6. **Task Components**: Build task card, list, and empty state
7. **Task Form**: Create modal form for adding/editing tasks
8. **Animations**: Add Framer Motion animations throughout
9. **API Integration**: Connect components to backend API
10. **Polish**: Fine-tune animations, fix responsive issues, enhance accessibility

### 9. Non-Functional Notes

#### Accessibility
- **Focus Rings**: Visible focus indicators for keyboard navigation
- **Semantic HTML**: Proper heading hierarchy and landmark elements
- **ARIA Labels**: Appropriate ARIA attributes for interactive elements
- **Screen Reader**: Compatibility with screen readers

#### Performance
- **Code Splitting**: Leverage Next.js automatic code splitting
- **Image Optimization**: Use Next.js Image component for optimized images
- **Lazy Loading**: Lazy load non-critical components
- **Memoization**: Use React.memo for expensive components

#### Dark Mode
- **Seamless Transition**: Smooth transitions between light and dark modes
- **System Preference**: Default to system preference with option to override
- **Consistency**: Consistent color palette across both themes
- **Preservation**: Remember user's theme preference between sessions