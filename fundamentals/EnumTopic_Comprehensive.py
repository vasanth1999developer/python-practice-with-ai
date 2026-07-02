"""
Comprehensive guide to Python Enums with all topics and examples
"""

from enum import Enum, IntEnum, Flag, IntFlag, auto

# ============================================================================
# 1. BASIC ENUM (Already covered in EnumTopic.py)
# ============================================================================
print("=" * 70)
print("1. BASIC ENUM - Creating and accessing enum members")
print("=" * 70)

class State(Enum):
    START = 1
    RUNNING = 2
    PAUSED = 3
    STOPPED = 4

print(State.START)          # Output: State.START
print(State.START.name)     # Output: START
print(State.START.value)    # Output: 1


# ============================================================================
# 2. ITERATION - Looping through all enum members
# ============================================================================
print("\n" + "=" * 70)
print("2. ITERATION - Looping through enum members")
print("=" * 70)

print("\nAll State members:")
for state in State:
    print(f"  {state.name} = {state.value}")


# ============================================================================
# 3. COMPARISON - Comparing enum members
# ============================================================================
print("\n" + "=" * 70)
print("3. COMPARISON - Comparing enum members")
print("=" * 70)

print(f"State.START == State.START: {State.START == State.START}")  # True
print(f"State.START == State.RUNNING: {State.START == State.RUNNING}")  # False
print(f"State.START is State.START: {State.START is State.START}")  # True
print(f"State.START != State.RUNNING: {State.START != State.RUNNING}")  # True


# ============================================================================
# 4. AUTO() FUNCTION - Auto-generating values
# ============================================================================
print("\n" + "=" * 70)
print("4. AUTO() FUNCTION - Automatically generating values")
print("=" * 70)

class Color(Enum):
    RED = auto()      # 1
    GREEN = auto()    # 2
    BLUE = auto()     # 3
    YELLOW = auto()   # 4

print("Colors with auto():")
for color in Color:
    print(f"  {color.name} = {color.value}")


# ============================================================================
# 5. MEMBERSHIP CHECKING - Using 'in' operator
# ============================================================================
print("\n" + "=" * 70)
print("5. MEMBERSHIP CHECKING - Checking if value is in enum")
print("=" * 70)

print(f"State.START in State: {State.START in State}")  # True
print(f"'START' in State.__members__: {'START' in State.__members__}")  # True

# Check by value
try:
    member = State(1)
    print(f"State(1): {member}")  # State.START
except ValueError as e:
    print(f"State(100) raises: {e}")


# ============================================================================
# 6. CONVERSION - Accessing by value or name
# ============================================================================
print("\n" + "=" * 70)
print("6. CONVERSION - Getting enum member by value or name")
print("=" * 70)

# By value
state_by_value = State(2)
print(f"State(2): {state_by_value}")  # State.RUNNING

# By name
state_by_name = State['PAUSED']
print(f"State['PAUSED']: {state_by_name}")  # State.PAUSED

# All members dict
print(f"\nAll members: {State.__members__}")


# ============================================================================
# 7. IntEnum - Numeric enum with comparison operations
# ============================================================================
print("\n" + "=" * 70)
print("7. IntEnum - Numeric enum (allows comparison)")
print("=" * 70)

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

print(f"Priority.LOW < Priority.HIGH: {Priority.LOW < Priority.HIGH}")  # True
print(f"Priority.MEDIUM >= Priority.LOW: {Priority.MEDIUM >= Priority.LOW}")  # True
print(f"Priority.HIGH + Priority.LOW: {Priority.HIGH + Priority.LOW}")  # 4 (arithmetic)
print(f"Priority.CRITICAL * 2: {Priority.CRITICAL * 2}")  # 8

# IntEnum can be compared with regular integers
print(f"Priority.HIGH == 3: {Priority.HIGH == 3}")  # True
print(f"Priority.LOW < 5: {Priority.LOW < 5}")  # True


# ============================================================================
# 8. FLAG - Bitwise operations on enums
# ============================================================================
print("\n" + "=" * 70)
print("8. FLAG - Combining flags with bitwise operations")
print("=" * 70)

class Permission(Flag):
    READ = auto()      # 1
    WRITE = auto()     # 2
    EXECUTE = auto()   # 4

# Combine flags
user_permission = Permission.READ | Permission.WRITE
print(f"READ | WRITE: {user_permission}")
print(f"Has READ: {Permission.READ in user_permission}")  # True
print(f"Has EXECUTE: {Permission.EXECUTE in user_permission}")  # False

# Remove flag
user_permission_no_write = user_permission & ~Permission.WRITE
print(f"Remove WRITE: {user_permission_no_write}")

# Check all flags
print(f"\nAll flags:")
for perm in Permission:
    print(f"  {perm.name} = {perm.value}")


# ============================================================================
# 9. IntFlag - Integer flag (allows arithmetic)
# ============================================================================
print("\n" + "=" * 70)
print("9. IntFlag - Integer flag (bitwise + arithmetic)")
print("=" * 70)

class Status(IntFlag):
    ACTIVE = auto()    # 1
    VERIFIED = auto()  # 2
    ADMIN = auto()     # 4

combined = Status.ACTIVE | Status.VERIFIED
print(f"ACTIVE | VERIFIED: {combined}")
print(f"Combined value: {int(combined)}")  # 3
print(f"Combined + ADMIN: {combined + Status.ADMIN}")  # 7


# ============================================================================
# 10. FUNCTIONAL API - Creating enums dynamically
# ============================================================================
print("\n" + "=" * 70)
print("10. FUNCTIONAL API - Creating enums dynamically")
print("=" * 70)

# Create enum using dict
Animal = Enum('Animal', {'DOG': 1, 'CAT': 2, 'BIRD': 3})
print(f"DOG: {Animal.DOG}, value: {Animal.DOG.value}")
print(f"CAT: {Animal.CAT}, value: {Animal.CAT.value}")

# Create using string
Fruit = Enum('Fruit', 'APPLE BANANA ORANGE')
print(f"\nFruit enum:")
for fruit in Fruit:
    print(f"  {fruit.name} = {fruit.value}")

# Create using list of tuples
Size = Enum('Size', [('SMALL', 1), ('MEDIUM', 2), ('LARGE', 3)])
print(f"\nSize.SMALL: {Size.SMALL}, value: {Size.SMALL.value}")


# ============================================================================
# 11. ALIASES - Multiple names for same value
# ============================================================================
print("\n" + "=" * 70)
print("11. ALIASES - Multiple names for same enum value")
print("=" * 70)

class Direction(Enum):
    NORTH = 1
    UP = 1          # Alias for NORTH
    SOUTH = 2
    DOWN = 2        # Alias for SOUTH
    EAST = 3
    RIGHT = 3       # Alias for EAST
    WEST = 4
    LEFT = 4        # Alias for WEST

print(f"Direction.NORTH: {Direction.NORTH}")
print(f"Direction.UP: {Direction.UP}")
print(f"Direction.NORTH is Direction.UP: {Direction.NORTH is Direction.UP}")  # True

# Aliases don't appear in iteration
print("\nDirect members (no aliases):")
for direction in Direction:
    print(f"  {direction.name} = {direction.value}")

# All members including aliases
print(f"\nAll members including aliases: {list(Direction.__members__.keys())}")


# ============================================================================
# 12. CUSTOM METHODS - Adding behavior to enums
# ============================================================================
print("\n" + "=" * 70)
print("12. CUSTOM METHODS - Adding methods and properties to enums")
print("=" * 70)

class HTTPStatus(Enum):
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    SERVER_ERROR = 500
    
    def is_success(self):
        """Check if status is successful (200-299)"""
        return 200 <= self.value < 300
    
    def is_client_error(self):
        """Check if status is client error (400-499)"""
        return 400 <= self.value < 500
    
    def is_server_error(self):
        """Check if status is server error (500-599)"""
        return 500 <= self.value < 600
    
    @property
    def description(self):
        """Get description of status code"""
        descriptions = {
            200: "OK - Request successful",
            201: "Created - Resource created",
            400: "Bad Request - Invalid input",
            401: "Unauthorized - Authentication required",
            403: "Forbidden - Access denied",
            404: "Not Found - Resource not found",
            500: "Internal Server Error",
        }
        return descriptions.get(self.value, "Unknown")

print(f"HTTPStatus.OK: {HTTPStatus.OK.value}")
print(f"Is success: {HTTPStatus.OK.is_success()}")  # True
print(f"Description: {HTTPStatus.OK.description}")

print(f"\nHTTPStatus.NOT_FOUND: {HTTPStatus.NOT_FOUND.value}")
print(f"Is client error: {HTTPStatus.NOT_FOUND.is_client_error()}")  # True
print(f"Description: {HTTPStatus.NOT_FOUND.description}")

print(f"\nHTTPStatus.SERVER_ERROR: {HTTPStatus.SERVER_ERROR.value}")
print(f"Is server error: {HTTPStatus.SERVER_ERROR.is_server_error()}")  # True


# ============================================================================
# 13. COMPLEX ENUM WITH MULTIPLE VALUES
# ============================================================================
print("\n" + "=" * 70)
print("13. ENUM WITH MULTIPLE VALUES (Tuples)")
print("=" * 70)

class Continent(Enum):
    ASIA = ("Asia", 44579000, 4694000000)
    AFRICA = ("Africa", 30370000, 1373000000)
    EUROPE = ("Europe", 10180000, 748000000)
    NORTH_AMERICA = ("North America", 24709000, 579000000)
    SOUTH_AMERICA = ("South America", 17840000, 433000000)
    AUSTRALIA = ("Australia", 7692000, 26000000)
    
    def __init__(self, display_name, area, population):
        self.display_name = display_name
        self.area_km2 = area
        self.population = population
    
    def population_density(self):
        return round(self.population / self.area_km2, 2)

print(f"Continent: {Continent.ASIA.display_name}")
print(f"Area: {Continent.ASIA.area_km2} km²")
print(f"Population: {Continent.ASIA.population}")
print(f"Density: {Continent.ASIA.population_density()} people/km²")

print(f"\nContinent: {Continent.AFRICA.display_name}")
print(f"Population Density: {Continent.AFRICA.population_density()} people/km²")


# ============================================================================
# 14. PRACTICAL EXAMPLE - Real-world enum usage
# ============================================================================
print("\n" + "=" * 70)
print("14. PRACTICAL EXAMPLE - Task Manager with Enums")
print("=" * 70)

class TaskStatus(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    CANCELLED = 4

class TaskPriority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class Task:
    def __init__(self, name, status=TaskStatus.PENDING, priority=TaskPriority.MEDIUM):
        self.name = name
        self.status = status
        self.priority = priority
    
    def __str__(self):
        return f"Task: {self.name} | Status: {self.status.name} | Priority: {self.priority.name}"
    
    def is_urgent(self):
        return self.priority >= TaskPriority.HIGH

# Create tasks
task1 = Task("Write report", TaskStatus.IN_PROGRESS, TaskPriority.HIGH)
task2 = Task("Send email", TaskStatus.PENDING, TaskPriority.LOW)
task3 = Task("Fix bug", TaskStatus.IN_PROGRESS, TaskPriority.CRITICAL)

print(task1)
print(task2)
print(task3)

print(f"\nTask1 is urgent: {task1.is_urgent()}")  # True
print(f"Task2 is urgent: {task2.is_urgent()}")  # False
print(f"Task3 is urgent: {task3.is_urgent()}")  # True

# Filter by priority
tasks = [task1, task2, task3]
urgent_tasks = [t for t in tasks if t.priority >= TaskPriority.HIGH]
print(f"\nUrgent tasks: {len(urgent_tasks)}")
for task in urgent_tasks:
    print(f"  - {task.name}")


print("\n" + "=" * 70)
print("END OF COMPREHENSIVE ENUM GUIDE")
print("=" * 70)
