# API Contracts: Intermediate Level Features

## Command Interface Contracts

### Add Command
```
Input: add "title" ["description"] ["priority"] ["tags"]
Output: Success message with task ID and details
Validation:
  - Title is required and non-empty
  - Priority must be one of "high", "medium", "low"
  - Tags are comma-separated strings
```

### Update Command
```
Input: update id ["title"] ["description"] ["priority"] ["tags"]
Output: Success message or error if task not found
Validation:
  - ID must be a valid integer
  - Priority must be one of "high", "medium", "low"
```

### List Command
```
Input: list
Output: Formatted list of tasks with priority and tags
Behavior:
  - Applies current filter if active
  - Applies current sort order
  - Shows status message indicating active filters/sorts
```

### Filter Command
```
Input: filter [status|priority|tag] [value] | filter clear
Output: Confirmation message and updated task list
Validation:
  - Filter type must be status, priority, or tag
  - Status value must be pending or completed
  - Priority value must be high, medium, or low
```

### Sort Command
```
Input: sort [created|created_desc|title|title_desc|priority|priority_rev]
Output: Confirmation message and updated task list
Validation:
  - Sort criteria must be one of the valid options
```