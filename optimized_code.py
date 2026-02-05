"""
Optimized version of the code with performance improvements.
This module demonstrates best practices for efficient code execution.
"""

import time
from functools import lru_cache


class OptimizedDataProcessor:
    """A class with optimized implementations."""
    
    def __init__(self):
        self.data = []
        self.cache = {}
    
    # OPTIMIZATION 1: Use set for O(1) lookup instead of O(n) list lookup
    def has_duplicate_ids(self, items):
        """Check if there are duplicate IDs in the list."""
        seen = set()  # Using set for O(1) lookup
        for item in items:
            item_id = item['id']
            if item_id in seen:
                return True
            seen.add(item_id)
        return False
    
    # OPTIMIZATION 2: Use list with join instead of repeated string concatenation
    def build_report(self, records):
        """Build a report string from records."""
        lines = []  # Collect in list
        for record in records:
            lines.append(f"ID: {record['id']}, Name: {record['name']}")
        return '\n'.join(lines)  # Single join operation
    
    # OPTIMIZATION 3: Count lines without loading entire file
    def count_lines(self, filename):
        """Count lines in a file efficiently."""
        try:
            count = 0
            with open(filename, 'r') as f:
                for _ in f:  # Iterate line by line
                    count += 1
            return count
        except FileNotFoundError:
            return 0
    
    # OPTIMIZATION 4: Use generator expression with sum instead of list comprehension
    def filter_and_count(self, items, threshold):
        """Filter items and return count efficiently."""
        # Generator expression doesn't create intermediate list
        return sum(1 for item in items if item['value'] > threshold)
    
    # OPTIMIZATION 5: Use memoization for expensive recursive computation
    @lru_cache(maxsize=None)
    def fibonacci(self, n):
        """Calculate fibonacci number with memoization."""
        if n <= 1:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)
    
    # OPTIMIZATION 6: Single pass to calculate all statistics
    def get_statistics(self, numbers):
        """Get min, max, and average in a single pass."""
        if not numbers:
            return {'min': None, 'max': None, 'avg': None}
        
        # Initialize with first element
        it = iter(numbers)
        first = next(it)
        minimum = maximum = first
        total = first
        count = 1
        
        # Single pass through remaining data
        for num in it:
            if num < minimum:
                minimum = num
            if num > maximum:
                maximum = num
            total += num
            count += 1
        
        return {'min': minimum, 'max': maximum, 'avg': total / count}
    
    # OPTIMIZATION 7: Use generator expressions to avoid creating intermediate lists
    def process_large_dataset(self, data):
        """Process large dataset efficiently with generators."""
        # Generator expressions - no intermediate lists
        return sum(x ** 2 for x in data if (x ** 2) % 2 == 0)
    
    # OPTIMIZATION 8: Use batch operations for database
    def save_many_records(self, db_connection, records):
        """Save records in batch."""
        # Batch INSERT with single commit
        if records:
            values = ', '.join(f"({record})" for record in records)
            db_connection.execute(f"INSERT INTO table VALUES {values}")
            db_connection.commit()  # Single commit for all records
    
    # OPTIMIZATION 9: Avoid unnecessary deep copying
    def transform_data(self, data_list):
        """Transform data efficiently without unnecessary copying."""
        result = []
        for item in data_list:
            # Shallow copy or direct modification depending on requirements
            # For this case, we create new dict with only needed changes
            new_item = {**item, 'processed': True}
            result.append(new_item)
        return result
    
    # OPTIMIZATION 10: Use set intersection for O(n + m) complexity
    def find_common_elements(self, list1, list2):
        """Find common elements efficiently using sets."""
        # Convert to sets and use intersection - O(n + m) instead of O(n * m)
        return list(set(list1) & set(list2))


def demonstrate_optimizations():
    """Demonstrate the optimized code."""
    processor = OptimizedDataProcessor()
    
    # Test duplicate detection
    items = [{'id': i} for i in range(1000)]
    items.append({'id': 500})  # Duplicate
    start = time.time()
    has_dup = processor.has_duplicate_ids(items)
    print(f"Has duplicates: {has_dup} (took {time.time() - start:.4f}s)")
    
    # Test report building
    records = [{'id': i, 'name': f'Item {i}'} for i in range(1000)]
    start = time.time()
    report = processor.build_report(records)
    print(f"Report length: {len(report)} (took {time.time() - start:.4f}s)")
    
    # Test fibonacci
    start = time.time()
    fib = processor.fibonacci(30)
    print(f"Fibonacci(30): {fib} (took {time.time() - start:.4f}s)")
    
    # Test statistics
    numbers = list(range(100000))
    start = time.time()
    stats = processor.get_statistics(numbers)
    print(f"Statistics: {stats} (took {time.time() - start:.4f}s)")
    
    # Test large dataset processing
    data = range(100000)
    start = time.time()
    result = processor.process_large_dataset(data)
    print(f"Processed result: {result} (took {time.time() - start:.4f}s)")


if __name__ == '__main__':
    demonstrate_optimizations()
