from enum import Enum

class State(Enum):
    START = 1
    RUNNING = 2
    PAUSED = 3
    STOPPED = 4


print(State.START)  # Output: State.START
print(State.RUNNING)  # Output: State.RUNNING
print(State.PAUSED)  # Output: State.PAUSED
print(State.STOPPED)  # Output: State.STOPPED

print(State.START.name)  # Output: START
print(State.START.value)  # Output: 1

print(State.RUNNING.name)  # Output: RUNNING
print(State.RUNNING.value)  # Output: 2

print(State.PAUSED.name)  # Output: PAUSED
print(State.PAUSED.value)  # Output: 3

print(State.STOPPED.name)  # Output: STOPPED
print(State.STOPPED.value)  # Output: 4


