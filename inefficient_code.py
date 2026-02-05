"""
Example code with various performance inefficiencies.
This module demonstrates common anti-patterns that slow down code execution.
"""

import time


class DataProcessor:
    """A class with multiple inefficient implementations."""
    
    def __init__(self):
        self.data = []
        self.cache = {}
    
    # INEFFICIENCY 1: O(n) lookup with list instead of set
    def has_duplicate_ids(self, items):
        """Check if there are duplicate IDs in the list."""
        seen = []  # Using list instead of set
        for item in items:
            if item['id'] in seen:  # O(n) lookup
                return True
            seen.append(item['id'])
        return False
    
    # INEFFICIENCY 2: Repeated string concatenation in loop
    def build_report(self, records):
        """Build a report string from records."""
        if not records:
            return ""
        report = ""  # String concatenation in loop
        for i, record in enumerate(records):
            if i > 0:
                report += "\n"
            report += f"ID: {record['id']}, Name: {record['name']}"
        return report
    
    # INEFFICIENCY 3: Loading entire file into memory
    def count_lines(self, filename):
        """Count lines in a file."""
        try:
            with open(filename, 'r') as f:
                data = f.read()  # Loads entire file
                return len(data.split('\n'))
        except FileNotFoundError:
            return 0
    
    # INEFFICIENCY 4: Unnecessary list comprehension
    def filter_and_count(self, items, threshold):
        """Filter items and return count."""
        filtered = [item for item in items if item['value'] > threshold]
        return len(filtered)  # Only need count, not the list
    
    # INEFFICIENCY 5: No caching for expensive computation
    def fibonacci(self, n):
        """Calculate fibonacci number recursively without caching."""
        if n <= 1:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)
    
    # INEFFICIENCY 6: Multiple passes over data
    def get_statistics(self, numbers):
        """Get min, max, and average of numbers."""
        minimum = min(numbers)  # First pass
        maximum = max(numbers)  # Second pass
        average = sum(numbers) / len(numbers)  # Third pass
        return {'min': minimum, 'max': maximum, 'avg': average}
    
    # INEFFICIENCY 7: Using list when generator would suffice
    def process_large_dataset(self, data):
        """Process large dataset inefficiently."""
        # Creates entire list in memory
        squared = [x ** 2 for x in data]
        filtered = [x for x in squared if x % 2 == 0]
        return sum(filtered)
    
    # INEFFICIENCY 8: Not using database batch operations
    def save_many_records(self, db_connection, records):
        """Save records one by one."""
        for record in records:
            # Simulating individual INSERT statements
            db_connection.execute(f"INSERT INTO table VALUES ({record})")
            db_connection.commit()  # Commit after each insert
    
    # INEFFICIENCY 9: Unnecessary deep copying
    def transform_data(self, data_list):
        """Transform data with unnecessary copying."""
        import copy
        result = []
        for item in data_list:
            # Deep copy when shallow copy or no copy would suffice
            new_item = copy.deepcopy(item)
            new_item['processed'] = True
            result.append(new_item)
        return result
    
    # INEFFICIENCY 10: Inefficient search algorithm
    def find_common_elements(self, list1, list2):
        """Find common elements between two lists."""
        common = []
        for item1 in list1:  # O(n * m) complexity
            for item2 in list2:
                if item1 == item2 and item1 not in common:
                    common.append(item1)
        return common


def demonstrate_inefficiencies():
    """Demonstrate the inefficient code."""
    processor = DataProcessor()
    
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
    demonstrate_inefficiencies()
