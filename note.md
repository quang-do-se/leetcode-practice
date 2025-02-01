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

Use `stack` for DFS.

Use `queue` for BFS.

### Notes

The root node (which has no parents) has depth 0.

Total number of nodes in a complete binary tree of depth `d`:

```
n = 2 ^ (d + 1) - 1

=> n + 1 = 2 ^ (d + 1)

=> log (n + 1) = d + 1

=> d = log(n + 1) - 1
```

The maximum number of nodes in a complete binary tree of depth `d` is:
```
2 ^ d
=> 2 ^ (d + 1 - 1)
=> 2 ^ (d + 1) / 2
=> n / 2
```

### Comparison of Breadth-First Traversal and Complete Binary Tree Deserialization

Consider the following binary tree:

```
      1
       \
        2
         \
          3
           \
            4
```

To deserialize this binary tree into an array using two different approaches, we obtain the following results:

Breadth-First Traversal (BFT) Binary Tree:
`[1,None,2,None,3,None,4]`

Complete Binary Tree:
`[1,None,2,None,None,None,3,None,None,None,None,None,None,None,4]`

Since the tree has a depth `d` of 3, we can use the geometric sum formula to calculate the total number of nodes in a Complete Binary Tree:
```
2 ^ 0 + 2 ^ 1 + 2 ^ 2 + 2 ^ 3
=> 2 ^ (d + 1) - 1
=> 2 ^ (3 + 1) - 1
=> 2 ^ 4 - 1 = 15
```

For every level below the root node, in a BFT Binary Tree, we need at least two nodes to represent the tree.
Thus, the total number of nodes in a minimal BFT Binary Tree of depth `d` is calculated as:
```
2 * d + 1
=> 2 * 3 + 1
=> 2 * 3 + 1 = 7
```

The difference in the total number of nodes between the two approaches is:

```
total_nodes_in_complete_binary_tree - total_nodes_in_minimum_bft_binary_tree

=> (2 ^ (d + 1) - 1) - (2 * d + 1)
=> (2 ^ 4 - 1) - (2 * 3 + 1)
=> 15 - 7 = 8
```
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


## Python Gotchas

- https://docs.python-guide.org/writing/gotchas/
  - Try to avoid using `mutable default arguments`
