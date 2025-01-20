# Edge Cases

## String

- Consider if string is empty

## Two pointers

- Consider if index can be out of bound for either pointer

## Identity vs Equality

In Python:
  - use `is` when you want to check against an object's identity (e.g. checking to see if `var` is `None` or checks if two variables point to the same object in memory).
  - Use `==` operator when you want to check equality or compares the content of objects. (e.g. check if two lists contain the same elements).

In Java:
  - use `==` operator when you want to check against an object's identity (e.g. checks if two variables point to the same object in memory).
  - Use `equals()` method when you want to check equality or compares the content of objects. (e.g. check if two lists contain the same elements).

## Recursive to Iterative

When converting a recursive algorithm to an iterative approach, we typically need to use a `stack` or `queue` to simulate the recursive function's call stack. If the recursive function maintains state, such as accumulations or additional variables, we may need to use a custom object, extra data structures (e.g., dictionaries or lists), or tuples in Python to store and track that state.

## Binary Tree

The maximum number of leaves in a binary tree is `n / 2`​ (for a full binary tree),
or `2 ^ (log(n) - 1) == 2 ^ log(n) / 2 == n / 2`

## Collection

### Concurrent Modification

- Avoid modifying a collection directly while iterating over it, as it can lead to skipped elements or unexpected behavior.
- Instead, collect changes separately, use list comprehensions or collection filter, or employ safe iteration techniques like reversing or using built-in thread-safe collection such as `CopyOnWriteArrayList`.

#### Issues
```python
nums = [2, 4, 6, 8]
for num in nums:
    if num % 2 == 0:
        nums.remove(num)

print(nums)  # Output: [4, 8]
```

```python
nums = [2, 4, 6, 8]
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        nums.pop(i)

# Throw IndexError: list index out of range
```

#### Fix - Reverse traversal
```python
nums = [2, 4, 6, 8]
for i in range(len(nums) - 1, -1, -1):
    if nums[i] % 2 == 0:
        nums.pop(i)

print(nums)  # Output: []
```