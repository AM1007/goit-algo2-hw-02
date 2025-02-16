from typing import List, Dict
from dataclasses import dataclass
from itertools import combinations

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

def create_print_groups(jobs: List[PrintJob], constraints: PrinterConstraints) -> List[List[PrintJob]]:
    """
    Creates groups of models for simultaneous printing, considering printer constraints.
    
    Args:
        jobs: List of print jobs
        constraints: Printer constraints
    
    Returns:
        List of job groups for simultaneous printing
    """
    groups = []
    remaining_jobs = jobs.copy()
    
    while remaining_jobs:
        current_group = []
        # Iterate through all possible combinations of remaining jobs
        for i in range(min(len(remaining_jobs), constraints.max_items), 0, -1):
            for combo in combinations(remaining_jobs, i):
                total_volume = sum(job.volume for job in combo)
                # Check if the combination meets the constraints
                if total_volume <= constraints.max_volume:
                    current_group = list(combo)
                    break
            if current_group:
                break
                
        if current_group:
            groups.append(current_group)
            # Remove used jobs
            for job in current_group:
                remaining_jobs.remove(job)
        else:
            # If unable to create a group, add a single job
            groups.append([remaining_jobs[0]])
            remaining_jobs.pop(0)
            
    return groups

def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    """
    Optimizes the 3D printing queue according to priorities and printer constraints.
    
    Args:
        print_jobs: List of print jobs
        constraints: Printer constraints
    
    Returns:
        Dict with print order and total time
    """
    # Convert input data into class objects
    jobs = [PrintJob(**job) for job in print_jobs]
    printer_constraints = PrinterConstraints(**constraints)
    
    # Sort jobs by priority (higher priority first)
    jobs.sort(key=lambda x: x.priority)
    
    # Group jobs for simultaneous printing
    groups = create_print_groups(jobs, printer_constraints)
    
    # Create print order and calculate total time
    print_order = []
    total_time = 0
    
    for group in groups:
        # Add model IDs from the group to the print order
        print_order.extend(job.id for job in group)
        # Group print time is the maximum time among the models in the group
        group_time = max(job.print_time for job in group)
        total_time += group_time
    
    return {
        "print_order": print_order,
        "total_time": total_time
    }

def test_printing_optimization():
    # Test 1: Models with the same priority
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
    ]

    # Test 2: Models with different priorities
    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}
    ]

    # Test 3: Exceeding volume constraints
    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
    ]

    constraints = {
        "max_volume": 300,
        "max_items": 2
    }

    print("Test 1 (same priority):")
    result1 = optimize_printing(test1_jobs, constraints)
    print(f"Print order: {result1['print_order']}")
    print(f"Total time: {result1['total_time']} minutes")

    print("\nTest 2 (different priorities):")
    result2 = optimize_printing(test2_jobs, constraints)
    print(f"Print order: {result2['print_order']}")
    print(f"Total time: {result2['total_time']} minutes")

    print("\nTest 3 (exceeding constraints):")
    result3 = optimize_printing(test3_jobs, constraints)
    print(f"Print order: {result3['print_order']}")
    print(f"Total time: {result3['total_time']} minutes")

if __name__ == "__main__":
    test_printing_optimization()
