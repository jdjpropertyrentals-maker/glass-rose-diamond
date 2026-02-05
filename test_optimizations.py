"""
Tests to verify that optimized implementations produce correct results.
"""

import pytest
import tempfile
import os
from inefficient_code import DataProcessor
from optimized_code import OptimizedDataProcessor


@pytest.fixture
def inefficient_processor():
    return DataProcessor()


@pytest.fixture
def optimized_processor():
    return OptimizedDataProcessor()


class TestDuplicateDetection:
    """Test duplicate ID detection."""
    
    def test_no_duplicates(self, inefficient_processor, optimized_processor):
        items = [{'id': i} for i in range(100)]
        assert inefficient_processor.has_duplicate_ids(items) == False
        assert optimized_processor.has_duplicate_ids(items) == False
    
    def test_has_duplicates(self, inefficient_processor, optimized_processor):
        items = [{'id': i} for i in range(100)]
        items.append({'id': 50})
        assert inefficient_processor.has_duplicate_ids(items) == True
        assert optimized_processor.has_duplicate_ids(items) == True
    
    def test_empty_list(self, inefficient_processor, optimized_processor):
        assert inefficient_processor.has_duplicate_ids([]) == False
        assert optimized_processor.has_duplicate_ids([]) == False


class TestStringBuilding:
    """Test report building."""
    
    def test_build_report(self, inefficient_processor, optimized_processor):
        records = [
            {'id': 1, 'name': 'Alice'},
            {'id': 2, 'name': 'Bob'},
            {'id': 3, 'name': 'Charlie'}
        ]
        
        result1 = inefficient_processor.build_report(records)
        result2 = optimized_processor.build_report(records)
        
        # Both should produce the same output
        assert result1 == result2
        assert 'Alice' in result1
        assert 'Bob' in result1
        assert 'Charlie' in result1
    
    def test_empty_records(self, inefficient_processor, optimized_processor):
        assert inefficient_processor.build_report([]) == ""
        assert optimized_processor.build_report([]) == ""


class TestFileReading:
    """Test line counting."""
    
    def test_count_lines(self, inefficient_processor, optimized_processor):
        # Create a temporary file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5")
            temp_file = f.name
        
        try:
            count1 = inefficient_processor.count_lines(temp_file)
            count2 = optimized_processor.count_lines(temp_file)
            
            # Both should count the same number of lines
            assert count1 == count2
            assert count1 == 5
        finally:
            os.unlink(temp_file)
    
    def test_nonexistent_file(self, inefficient_processor, optimized_processor):
        assert inefficient_processor.count_lines('nonexistent.txt') == 0
        assert optimized_processor.count_lines('nonexistent.txt') == 0


class TestFilterAndCount:
    """Test filtering and counting."""
    
    def test_filter_and_count(self, inefficient_processor, optimized_processor):
        items = [{'value': i} for i in range(100)]
        threshold = 50
        
        count1 = inefficient_processor.filter_and_count(items, threshold)
        count2 = optimized_processor.filter_and_count(items, threshold)
        
        assert count1 == count2
        assert count1 == 49  # 51-99 inclusive
    
    def test_no_items_above_threshold(self, inefficient_processor, optimized_processor):
        items = [{'value': i} for i in range(10)]
        threshold = 100
        
        assert inefficient_processor.filter_and_count(items, threshold) == 0
        assert optimized_processor.filter_and_count(items, threshold) == 0


class TestFibonacci:
    """Test Fibonacci calculation."""
    
    def test_fibonacci_base_cases(self, inefficient_processor, optimized_processor):
        assert inefficient_processor.fibonacci(0) == 0
        assert optimized_processor.fibonacci(0) == 0
        
        assert inefficient_processor.fibonacci(1) == 1
        assert optimized_processor.fibonacci(1) == 1
    
    def test_fibonacci_small_values(self, inefficient_processor, optimized_processor):
        # Clear cache for optimized version
        optimized_processor.fibonacci.cache_clear()
        
        for n in range(10):
            result1 = inefficient_processor.fibonacci(n)
            result2 = optimized_processor.fibonacci(n)
            assert result1 == result2
    
    def test_fibonacci_known_values(self, inefficient_processor, optimized_processor):
        # Test known Fibonacci numbers
        optimized_processor.fibonacci.cache_clear()
        
        # fib(10) = 55
        assert inefficient_processor.fibonacci(10) == 55
        assert optimized_processor.fibonacci(10) == 55


class TestStatistics:
    """Test statistics calculation."""
    
    def test_statistics(self, inefficient_processor, optimized_processor):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        stats1 = inefficient_processor.get_statistics(numbers)
        stats2 = optimized_processor.get_statistics(numbers)
        
        assert stats1['min'] == stats2['min'] == 1
        assert stats1['max'] == stats2['max'] == 10
        assert stats1['avg'] == stats2['avg'] == 5.5
    
    def test_statistics_single_value(self, inefficient_processor, optimized_processor):
        numbers = [42]
        
        stats1 = inefficient_processor.get_statistics(numbers)
        stats2 = optimized_processor.get_statistics(numbers)
        
        assert stats1['min'] == stats2['min'] == 42
        assert stats1['max'] == stats2['max'] == 42
        assert stats1['avg'] == stats2['avg'] == 42


class TestLargeDataset:
    """Test large dataset processing."""
    
    def test_process_large_dataset(self, inefficient_processor, optimized_processor):
        data = range(100)
        
        result1 = inefficient_processor.process_large_dataset(data)
        result2 = optimized_processor.process_large_dataset(data)
        
        assert result1 == result2
    
    def test_process_empty_dataset(self, inefficient_processor, optimized_processor):
        data = []
        
        assert inefficient_processor.process_large_dataset(data) == 0
        assert optimized_processor.process_large_dataset(data) == 0


class TestTransformData:
    """Test data transformation."""
    
    def test_transform_data(self, inefficient_processor, optimized_processor):
        data = [
            {'id': 1, 'value': 10},
            {'id': 2, 'value': 20},
            {'id': 3, 'value': 30}
        ]
        
        result1 = inefficient_processor.transform_data(data)
        result2 = optimized_processor.transform_data(data)
        
        # Check that all items have 'processed' flag
        assert all(item['processed'] for item in result1)
        assert all(item['processed'] for item in result2)
        
        # Check that original values are preserved
        assert result1[0]['id'] == result2[0]['id'] == 1
        assert result1[1]['value'] == result2[1]['value'] == 20


class TestFindCommonElements:
    """Test finding common elements."""
    
    def test_find_common_elements(self, inefficient_processor, optimized_processor):
        list1 = [1, 2, 3, 4, 5]
        list2 = [4, 5, 6, 7, 8]
        
        result1 = set(inefficient_processor.find_common_elements(list1, list2))
        result2 = set(optimized_processor.find_common_elements(list1, list2))
        
        # Should find 4 and 5 as common elements
        assert result1 == result2 == {4, 5}
    
    def test_no_common_elements(self, inefficient_processor, optimized_processor):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        
        result1 = inefficient_processor.find_common_elements(list1, list2)
        result2 = optimized_processor.find_common_elements(list1, list2)
        
        assert len(result1) == 0
        assert len(result2) == 0
    
    def test_all_common_elements(self, inefficient_processor, optimized_processor):
        list1 = [1, 2, 3, 4, 5]
        list2 = [1, 2, 3, 4, 5]
        
        result1 = set(inefficient_processor.find_common_elements(list1, list2))
        result2 = set(optimized_processor.find_common_elements(list1, list2))
        
        assert result1 == result2 == {1, 2, 3, 4, 5}


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
