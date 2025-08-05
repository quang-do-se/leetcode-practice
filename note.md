## Edge Cases

- Null values
- Empty array
- Empty string
- Negative number
- Zero
- Duplicates
- Off-by-one (loop, out of bound)
- Different in lengths

Always read the constraints.

## Array

- Whenever you're trying to solve an array problem in place, always consider the possibility of iterating backwards instead of forwards through the array. It can completely change the problem, and make it a lot easier.

## Linked List

When working with linked lists, consider the following cases:

- Insertion or deletion in the **middle**
- Insertion or deletion at the **beginning**
- Insertion or deletion at the **end**
- Handling a **single** node
- Handling an **empty** list

Also, check if the linked list is a **singly linked list** or **doubly linked list**.

## Two-pointers technique

- Consider if index can be out of bound for either pointer
- If two pointers move in opposite direction, make sure the algorithm can stop correctly
- Two pointers can go **same direction**, **opposite direction**, or **fixed width** (sliding window)


### Other notes for Two-pointers technique:
- This technique is often used in a **sorted** array.
- This technique sometimes will relate to Greedy Algorithm.

## Identity vs Equality

In Python:
  - use `is` when you want to check against an object's identity (e.g. checking to see if `var` is `None` or checks if two variables point to the same object in memory).
  - Use `==` operator when you want to check equality or compares the content of objects. (e.g. check if two lists contain the same elements).

In Java:
  - use `==` operator when you want to check against an object's identity (e.g. checks if two variables point to the same object in memory).
  - Use `equals()` method when you want to check equality or compares the content of objects. (e.g. check if two lists contain the same elements).

## Recursive to Iterative

When converting a recursive algorithm to an iterative approach, we typically need to use a `stack` or `queue` to simulate the recursive function's call stack. If the recursive function maintains state, such as accumulations or additional variables, we may need to use a custom object, extra data structures (e.g., dictionaries or lists), or tuples in Python to store and track that state.

## Binary Search

- Use `mid = low + (high - low) // 2` to avoid integer overflow

### Insertion Position

The Lower Bound and Upper Bound matters when there are duplicate elements in the list.

- Lower Bound: first/smallest index where `arr[i] >= target`
- Upper Bound: first/smallest index where `arr[i] > target` (strictly greater than target)

Note: It's quite tricky to determine whether to include/exclude `mid` value when implementing the Lower Bound or Upper Bound search. So keep these conditions in mind.

```python
import bisect

array = [7, -4, 3, 9, 9, 9, 12]
target = 9

print(bisect.bisect_left(array, target))   # 3
print(bisect.bisect_right(array, target))  # 6
```

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
  - Try to avoid using `mutable default arguments` like `list` or `dict`


## Time Complexity

- When dividing an integer `x` by `y`, there can be at most `O(logarithm base y of x)` divisions.


## Tips

- In problems where we have to find kth largest/smallest number, we can always start by using any one of these three methods: sorting the array, using a priority queue, or using a sorted set. As these three methods keep array elements in sorted order and it's easy to find the required element.

- Never forget to take the time complexity of built-in operations into consideration when you compute the time complexity for your solution.


## Modulo

In Python, the modulo operator (%) always returns a non-negative result when used with a positive divisor:

``` python
-25 % 26 = 1
-51 % 26 = 1
 51 % 26 = 25
```

However, in C++ and Java, the result of the % operator can be negative if the dividend is negative:

``` java
-25 % 26 = -25
-51 % 26 = -25
 51 % 26 =  25
```

To always get a positive remainder in C++ or Java, use the following formula: 

**`((a % m) + m) % m`**

This ensures the result is always in the range `[0, m)` regardless of whether `a` is positive or negative.

``` java
((-25 % 26) + 26) % 26 = 1
((-51 % 26) + 26) % 26 = 1
(( 51 % 26) + 26) % 26 = 25
```

# Needs review

- Two's Complement
- Boyer-Moore Voting Algorithm
- Floyd's Cycle Detection Algorithm
