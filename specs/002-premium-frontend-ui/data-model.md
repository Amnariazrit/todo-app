# Data Model for Premium Frontend UI

## Entities

### User
Represents the authenticated user with profile information and preferences.

**Fields**:
- id: string (unique identifier)
- email: string (email address for authentication)
- name: string (display name)
- createdAt: Date (account creation timestamp)
- updatedAt: Date (last update timestamp)
- preferences: UserPreferences (nested object for user preferences)

**Validation rules**:
- email must be a valid email format
- name must be 1-50 characters
- id must be unique

**Relationships**:
- One-to-many with Task (a user can have multiple tasks)

### UserPreferences
Represents user-specific preferences including theme settings.

**Fields**:
- theme: 'light' | 'dark' (selected theme preference)
- notificationsEnabled: boolean (whether notifications are enabled)
- language: string (user's preferred language)

**Validation rules**:
- theme must be either 'light' or 'dark'

### Task
Represents a task item with properties like title, description, priority, tags, and completion status.

**Fields**:
- id: string (unique identifier)
- title: string (task title)
- description: string (optional task description)
- priority: 'low' | 'medium' | 'high' (priority level)
- tags: string[] (array of tag strings)
- completed: boolean (completion status)
- createdAt: Date (task creation timestamp)
- updatedAt: Date (last update timestamp)
- userId: string (foreign key linking to User)

**Validation rules**:
- title must be 1-100 characters
- description must be 0-500 characters if provided
- priority must be one of 'low', 'medium', or 'high'
- tags array must have 0-10 items
- each tag must be 1-20 characters

**State transitions**:
- incomplete → completed (when task is marked as done)
- completed → incomplete (when task is unmarked)

**Relationships**:
- Many-to-one with User (many tasks belong to one user)

### Theme
Represents the visual theme settings (dark/light mode) with associated color schemes.

**Note**: This entity is primarily managed through the UserPreferences object rather than as a separate data store. The theme state is maintained in the frontend application state and user preferences.

**Fields**:
- mode: 'light' | 'dark'
- colors: ThemeColors (color definitions for the theme)

**Validation rules**:
- mode must be either 'light' or 'dark'

### ThemeColors
Represents the color definitions for a theme.

**Fields**:
- primary: string (primary color in hex format)
- secondary: string (secondary color in hex format)
- background: string (background color in hex format)
- card: string (card/background element color)
- text: string (text color)
- border: string (border color)
- accent: string (accent color for highlights)

**Validation rules**:
- All color fields must be valid hex color codes (#RRGGBB or #RGB format)
- Contrast ratios must meet WCAG 2.1 AA standards