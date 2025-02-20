## Follow up

### What if the the digits in the linked list are stored in non-reversed order? For example:

(3→4→2) + (4→6→5) = 8→0→7

### Standard Approaches
1. Store the values in array lists
2. Using two stacks

### Recursive Approaches
Recursive approach will be very complex in this case 
since if two lists are different in length, we need to somehow align them. 

For example: Adding [1] and [9, 9, 9]

There are two approaches:
1. Padding the shorter list to match the length of the longer list
2. Or traverse the longer list until the remaining nodes match the length of the shorter list

