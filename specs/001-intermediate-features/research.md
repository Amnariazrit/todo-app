# Research: Intermediate Level Features Implementation

## Decision: Task Class Extension
**Rationale**: The existing Task class needs to be extended with priority and tags attributes to support the new features. This follows the requirement to add priority (str) and tags (list[str]) to the Task entity.

**Alternatives considered**:
- Separate priority/tags storage: Would complicate the data model and relationships
- Dictionary-based extension: Would lose type safety and validation
- Inheritance approach: Would be over-engineering for this simple extension

## Decision: Global State Management
**Rationale**: Using global variables for current_filter and current_sort aligns with the in-memory, single-user console application architecture. This maintains simplicity while providing the required functionality.

**Alternatives considered**:
- Class-based state management: Would add complexity for a simple console app
- Configuration files: Contradicts the in-memory requirement
- Session-based state: Not applicable for console application

## Decision: Command Structure
**Rationale**: Extending existing commands (add, update, list) and adding new commands (filter, sort, search) provides a consistent user experience while implementing all required functionality.

**Alternatives considered**:
- Subcommand approach: Would be more complex for users
- Single command with complex syntax: Would be harder to use
- Menu-based interface: Would be inconsistent with existing CLI approach

## Decision: Sorting Implementation
**Rationale**: Using a configuration dictionary with lambda functions for sorting keys provides flexibility and clean implementation for all required sorting options.

**Alternatives considered**:
- Multiple separate sorting functions: Would create code duplication
- External sorting library: Not needed for basic sorting requirements
- Database-like query approach: Over-engineering for in-memory application

## Decision: Filtering Implementation
**Rationale**: Using a dictionary-based filter system with type/value pairs allows for easy extension and clear implementation of all required filter types.

**Alternatives considered**:
- Class-based filter system: Would add unnecessary complexity
- Function-based filters: Would be harder to manage and extend
- Boolean expression evaluation: Would be over-engineering for simple filters

## Decision: Input Validation
**Rationale**: Implementing validation functions for priority and tags ensures data integrity while providing user-friendly error messages.

**Alternatives considered**:
- No validation: Would lead to data integrity issues
- Complex validation rules: Would be over-engineering for this application
- External validation library: Not needed for simple validation requirements