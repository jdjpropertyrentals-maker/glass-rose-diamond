"""
Benchmark script to compare inefficient vs optimized implementations.
"""

import time
import sys
from inefficient_code import DataProcessor
from optimized_code import OptimizedDataProcessor


class MockDBConnection:
    """Mock database connection for testing."""
    def execute(self, query):
        pass
    
    def commit(self):
        pass


def benchmark_function(func, *args, **kwargs):
    """Run a function and return its execution time."""
    start = time.time()
    result = func(*args, **kwargs)
    elapsed = time.time() - start
    return result, elapsed


def compare_implementations():
    """Compare inefficient vs optimized implementations."""
    print("=" * 80)
    print("PERFORMANCE COMPARISON: Inefficient vs Optimized Code")
    print("=" * 80)
    
    inefficient = DataProcessor()
    optimized = OptimizedDataProcessor()
    
    results = []
    
    # Test 1: Duplicate Detection
    print("\n1. DUPLICATE DETECTION (1000 items)")
    print("-" * 80)
    items = [{'id': i} for i in range(1000)]
    items.append({'id': 500})
    
    result1, time1 = benchmark_function(inefficient.has_duplicate_ids, items)
    print(f"   Inefficient: {result1} - Time: {time1:.6f}s")
    
    result2, time2 = benchmark_function(optimized.has_duplicate_ids, items)
    print(f"   Optimized:   {result2} - Time: {time2:.6f}s")
    
    speedup = time1 / time2 if time2 > 0 else float('inf')
    print(f"   Speedup:     {speedup:.2f}x faster")
    results.append(('Duplicate Detection', speedup))
    
    # Test 2: String Building
    print("\n2. STRING BUILDING (1000 records)")
    print("-" * 80)
    records = [{'id': i, 'name': f'Item {i}'} for i in range(1000)]
    
    result1, time1 = benchmark_function(inefficient.build_report, records)
    print(f"   Inefficient: {len(result1)} chars - Time: {time1:.6f}s")
    
    result2, time2 = benchmark_function(optimized.build_report, records)
    print(f"   Optimized:   {len(result2)} chars - Time: {time2:.6f}s")
    
    speedup = time1 / time2 if time2 > 0 else float('inf')
    print(f"   Speedup:     {speedup:.2f}x faster")
    results.append(('String Building', speedup))
    
    # Test 3: Filter and Count
    print("\n3. FILTER AND COUNT (10000 items)")
    print("-" * 80)
    items = [{'value': i} for i in range(10000)]
    threshold = 5000
    
    result1, time1 = benchmark_function(inefficient.filter_and_count, items, threshold)
    print(f"   Inefficient: {result1} items - Time: {time1:.6f}s")
    
    result2, time2 = benchmark_function(optimized.filter_and_count, items, threshold)
    print(f"   Optimized:   {result2} items - Time: {time2:.6f}s")
    
    speedup = time1 / time2 if time2 > 0 else float('inf')
    print(f"   Speedup:     {speedup:.2f}x faster")
    results.append(('Filter and Count', speedup))
    
    # Test 4: Fibonacci
    print("\n4. FIBONACCI(30)")
    print("-" * 80)
    
    result1, time1 = benchmark_function(inefficient.fibonacci, 30)
    print(f"   Inefficient: {result1} - Time: {time1:.6f}s")
    
    # Clear cache for fair comparison
    optimized.fibonacci.cache_clear()
    result2, time2 = benchmark_function(optimized.fibonacci, 30)
    print(f"   Optimized:   {result2} - Time: {time2:.6f}s")
    
    speedup = time1 / time2 if time2 > 0 else float('inf')
    print(f"   Speedup:     {speedup:.2f}x faster")
    results.append(('Fibonacci', speedup))
    
    # Test 5: Statistics
    print("\n5. STATISTICS (100000 numbers)")
    print("-" * 80)
    numbers = list(range(100000))
    
    result1, time1 = benchmark_function(inefficient.get_statistics, numbers)
    print(f"   Inefficient: {result1} - Time: {time1:.6f}s")
    
    result2, time2 = benchmark_function(optimized.get_statistics, numbers)
    print(f"   Optimized:   {result2} - Time: {time2:.6f}s")
    
    speedup = time1 / time2 if time2 > 0 else float('inf')
    print(f"   Speedup:     {speedup:.2f}x faster")
    results.append(('Statistics', speedup))
    
    # Test 6: Large Dataset Processing
    print("\n6. LARGE DATASET PROCESSING (100000 items)")
    print("-" * 80)
    data = range(100000)
    
    result1, time1 = benchmark_function(inefficient.process_large_dataset, data)
    print(f"   Inefficient: {result1} - Time: {time1:.6f}s")
    
    result2, time2 = benchmark_function(optimized.process_large_dataset, data)
    print(f"   Optimized:   {result2} - Time: {time2:.6f}s")
    
    speedup = time1 / time2 if time2 > 0 else float('inf')
    print(f"   Speedup:     {speedup:.2f}x faster")
    results.append(('Large Dataset', speedup))
    
    # Test 7: Transform Data
    print("\n7. TRANSFORM DATA (1000 items)")
    print("-" * 80)
    data_list = [{'id': i, 'value': i * 2} for i in range(1000)]
    
    result1, time1 = benchmark_function(inefficient.transform_data, data_list)
    print(f"   Inefficient: {len(result1)} items - Time: {time1:.6f}s")
    
    result2, time2 = benchmark_function(optimized.transform_data, data_list)
    print(f"   Optimized:   {len(result2)} items - Time: {time2:.6f}s")
    
    speedup = time1 / time2 if time2 > 0 else float('inf')
    print(f"   Speedup:     {speedup:.2f}x faster")
    results.append(('Transform Data', speedup))
    
    # Test 8: Find Common Elements
    print("\n8. FIND COMMON ELEMENTS (500 items each)")
    print("-" * 80)
    list1 = list(range(500))
    list2 = list(range(250, 750))
    
    result1, time1 = benchmark_function(inefficient.find_common_elements, list1, list2)
    print(f"   Inefficient: {len(result1)} common - Time: {time1:.6f}s")
    
    result2, time2 = benchmark_function(optimized.find_common_elements, list1, list2)
    print(f"   Optimized:   {len(result2)} common - Time: {time2:.6f}s")
    
    speedup = time1 / time2 if time2 > 0 else float('inf')
    print(f"   Speedup:     {speedup:.2f}x faster")
    results.append(('Find Common Elements', speedup))
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    for name, speedup in results:
        print(f"{name:30} {speedup:>8.2f}x faster")
    
    avg_speedup = sum(s for _, s in results) / len(results)
    print("-" * 80)
    print(f"{'Average Speedup':30} {avg_speedup:>8.2f}x faster")
    print("=" * 80)


if __name__ == '__main__':
    compare_implementations()
