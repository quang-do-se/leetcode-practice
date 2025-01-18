# Edge Cases

## String

- Consider if string is empty

## Two pointers

- Consider if index can be out of bound for either pointer

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