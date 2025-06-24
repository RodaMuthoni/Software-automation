# Manual implementation
def manual_sort(data, key):
    """Sort list of dictionaries by specified key"""
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][key] > data[j+1][key]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

# AI-suggested implementation (GitHub Copilot style)
def ai_sort(data, key):
    """Sort list of dictionaries by specified key"""
    return sorted(data, key=lambda x: x[key])

# Test data
employees = [
    {"name": "Alice", "age": 30, "department": "Sales"},
    {"name": "Bob", "age": 25, "department": "Engineering"},
    {"name": "Charlie", "age": 35, "department": "Marketing"}
]

# Performance comparison
import timeit

manual_time = timeit.timeit(
    'manual_sort(employees.copy(), "age")', 
    globals=globals(), 
    number=1000
)

ai_time = timeit.timeit(
    'ai_sort(employees.copy(), "age")', 
    globals=globals(), 
    number=1000
)

print(f"Manual sort time: {manual_time:.5f}s")
print(f"AI-suggested sort time: {ai_time:.5f}s")
print(f"AI implementation is {manual_time/ai_time:.1f}x faster")


