# glass-rose-diamond

A demonstration repository showcasing common performance inefficiencies in code and their optimized solutions.

## Overview

This repository contains:
- **inefficient_code.py**: Examples of common performance anti-patterns
- **optimized_code.py**: Optimized versions of the same functionality
- **benchmark.py**: Performance comparison between implementations
- **test_optimizations.py**: Test suite to verify correctness
- **PERFORMANCE_IMPROVEMENTS.md**: Detailed documentation of all optimizations

## Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Running the Benchmarks

Compare performance between inefficient and optimized implementations:

```bash
python benchmark.py
```

### Running Tests

Verify that optimizations produce correct results:

```bash
python -m pytest test_optimizations.py -v
```

### Running Individual Examples

```bash
# See inefficient implementations in action
python inefficient_code.py

# See optimized implementations in action
python optimized_code.py
```

## Performance Improvements Covered

1. **Set vs List for Membership Testing** - O(1) vs O(n) lookup
2. **String Join vs Concatenation** - Avoiding repeated string creation
3. **Line-by-Line File Reading** - Streaming vs loading entire file
4. **Generator Expressions** - Avoiding intermediate lists
5. **Memoization** - Caching expensive recursive computations
6. **Single-Pass Algorithms** - Reducing iterations over data
7. **Generator Pipelines** - Processing large datasets efficiently
8. **Database Batch Operations** - Reducing transaction overhead
9. **Shallow vs Deep Copy** - Avoiding unnecessary copying
10. **Set Operations** - Using set intersection for finding commons

See [PERFORMANCE_IMPROVEMENTS.md](PERFORMANCE_IMPROVEMENTS.md) for detailed explanations of each optimization.

## Key Takeaways

- **Choose the right data structure** for your use case
- **Profile before optimizing** to find real bottlenecks
- **Understand algorithmic complexity** (Big O notation)
- **Use lazy evaluation** with generators when possible
- **Batch operations** when interacting with external systems
- **Cache expensive computations** when appropriate

## License

MIT