# Homework on "Greedy Algorithms and Dynamic Programming"

Welcome! How’s your mood?
We hope you're eagerly rubbing your hands, ready for a new challenge! 😉

This homework consists of two independent tasks. In the first task, you'll optimize a task queue based on priorities and constraints, using greedy algorithms for efficient resource management. In the second, you'll apply dynamic programming techniques like memoization and tabulation for solution optimization.

Let this assignment expand your perspective on **greedy algorithms and dynamic programming**! 🧠

***
## Task 1: Optimizing a 3D Printer Queue in a University Lab

Develop a program that optimizes the 3D printing queue by considering priorities and technical constraints, using a greedy algorithm.

### Task Description

1. The input consists of a list of print jobs, where each job contains:

- ID
- Model volume
- Priority
- Printing time
- Implement the main function optimize_printing, which will:

2. Consider task priorities
   
- Group models for simultaneous printing
- Check volume and quantity constraints
- Calculate the total print time
- Return the optimal print order

3.Display the optimal print order and the total execution time.


### Technical Specifications

1. Expected output format for optimize_printing:

```python
{
    "print_order": ["M1", "M2", "M3"],  # Optimal printing order
    "total_time": 360  # Total time in minutes
}
```
2. Input format for print jobs:

```python
print_jobs = [
    {
        "id": str,        # Unique identifier
        "volume": float,  # Volume in cm³ (> 0)
        "priority": int,  # Priority (1, 2, or 3)
        "print_time": int # Printing time in minutes (> 0)
    }
]
```

3. Printer constraints format:

```python
printer_constraints = {
    "max_volume": float,  # Maximum printable volume
    "max_items": int      # Maximum number of models
}
```

4. Task priorities:
- 1 (highest priority) – Course/Diploma projects
- 2 – Lab assignments
- 3 (lowest priority) – Personal projects

### Acceptance Criteria

📌 Mandatory conditions for mentor review: If any of these criteria are not met, the assignment will be returned for revision without evaluation. If you need clarification or get stuck, ask your mentor on Slack.

✅ The program groups models for simultaneous printing without exceeding constraints (10 pts).
✅ Higher-priority tasks are executed first (10 pts).
✅ Printing time for a model group is calculated as the max time among grouped models (10 pts).
✅ The program handles all test cases (10 pts):

Tasks with the same priority
Tasks with different priorities
Exceeding printer constraints
✅ Code uses dataclass for data structures (10 pts).


### Program Template

```python
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int

@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int

def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    """
    Optimizes the 3D printing queue based on priorities and printer constraints.

    Args:
        print_jobs: List of printing tasks.
        constraints: Printer limitations.

    Returns:
        Dictionary with the printing order and total time.
    """
    # Your code here

    return {
        "print_order": None,
        "total_time": None
    }

# Testing
if __name__ == "__main__":
    # Example test cases
    constraints = {"max_volume": 300, "max_items": 2}
    
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
    ]
    
    result = optimize_printing(test1_jobs, constraints)
    print(f"Print Order: {result['print_order']}")
    print(f"Total Time: {result['total_time']} minutes")

```

### Expected Output

#### Test 1 (Same Priority)

```python
Print Order: ['M1', 'M2', 'M3']
Total Time: 270 minutes
```

#### Test 2 (Different Priorities)

```python
Print Order: ['M2', 'M1', 'M3']
Total Time: 270 minutes
```

#### Test 3 (Exceeding Constraints)

```python
Print Order: ['M1', 'M2', 'M3']
Total Time: 450 minutes
```

***

## Task 2: Optimal Rod Cutting for Maximum Profit

Develop a program to **find the best way to cut a rod to maximize profit**. Implement two approaches:

1. Recursion with memoization
2. Tabulation (bottom-up dynamic programming)

### Task Description

1. Input consists of rod length and an array of prices where `price[i]` is the price of a rod of length `i+1`.
2. The goal is to determine how to cut the rod to maximize profit.
3. Implement both dynamic programming approaches.
4. Display the optimal cutting strategy and maximum profit.

### Technical Specifications

1. Input format:

```python
length = 5  # Rod length
prices = [2, 5, 7, 8, 10]  # Prices for lengths 1, 2, 3, 4, 5
```

2. Constraints:

- Rod length > 0
- All prices > 0
- The price array must not be empty
- The price array length must match the rod length

### Acceptance Criteria

✅ The program implements both methods (10 pts each):

```pyhton
def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    """Finds the optimal rod cutting strategy using memoization."""
    pass

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """Finds the optimal rod cutting strategy using tabulation."""
    pass
```

✅ Each method returns a dictionary containing:

- Maximum profit (10 pts)
- List of cut lengths (10 pts)
- Total number of cuts (10 pts)

### Expected Output Format

```python
{
    "max_profit": 12,  # Maximum profit
    "cuts": [2, 2, 1],  # List of segment lengths
    "number_of_cuts": 2  # Number of cuts
}
```

### Program Template

```python
from typing import List, Dict

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    # Your memoization-based solution here
    return {"max_profit": None, "cuts": None, "number_of_cuts": None}

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    # Your tabulation-based solution here
    return {"max_profit": None, "cuts": None, "number_of_cuts": None}

if __name__ == "__main__":
    length = 5
    prices = [2, 5, 7, 8, 10]

    print(rod_cutting_memo(length, prices))
    print(rod_cutting_table(length, prices))
```

### Expected Output

```python
Max Profit: 12
Cuts: [2, 2, 1]
Number of Cuts: 2
```