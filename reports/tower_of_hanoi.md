# PROBLEM 1: TOWER OF HANOI (RECURSION)

## 1.1 Introduction

The Tower of Hanoi is a mathematical puzzle used to demonstrate the concept of recursion in computer science. It consists of three rods and a number of disks of different sizes. The objective is to transfer all the disks from the starting rod to the destination rod using an auxiliary rod.

## 1.2 Problem Objective

The objective of this problem is to implement the Tower of Hanoi algorithm using recursion in Python. The program accepts the number of disks from the user and displays the sequence of movements required to solve the puzzle.

## 1.3 Rules of the Puzzle

The puzzle follows three main rules:

1. Only one disk can be moved at a time.
2. Only the top disk of a rod can be moved.
3. A larger disk cannot be placed on top of a smaller disk.

## 1.4 Explanation of the Recursive Approach

The program uses recursion to divide the problem into smaller problems until only one disk remains.

The solution follows three main steps:

1. Move the top n-1 disks from the source rod to the auxiliary rod.
2. Move the largest disk from the source rod to the destination rod.
3. Move the n-1 disks from the auxiliary rod to the destination rod.

The process continues until the base case is reached.

**Base Case:** When only one disk remains, the program moves that disk directly to the destination rod.

**Recursive Case:** When there is more than one disk, the function calls itself to solve smaller versions of the problem.

## 1.5 Algorithm

1. Start the program.
2. Ask the user to enter the number of disks.
3. Check that the input is a positive whole number.
4. If the number of disks is one, move the disk directly to the destination.
5. Otherwise, recursively move n-1 disks to the auxiliary rod.
6. Move the largest disk to the destination rod.
7. Recursively move the remaining disks to the destination rod.
8. Display every movement.
9. End the program.

## 1.6 Tower of Hanoi Diagram

The diagram below shows the initial arrangement of three disks on the source rod before the puzzle is solved.

```text
       Rod A          Rod B          Rod C
      (Source)      (Auxiliary)   (Destination)

        |                |              |
       [1]               |              |
      [ 2 ]              |              |
     [  3  ]             |              |
   ---------         ---------       ---------
```

Rod A contains all three disks at the beginning. Rod B is the auxiliary rod, while Rod C is the destination rod.

The disks are transferred one at a time while following the rules of the Tower of Hanoi puzzle.

## 1.6 Python Implementation

The program was implemented in Python using a recursive function called `solve_hanoi()`. A `main()` function handles user input and validates incorrect entries.

The program also handles invalid input, including zero, negative numbers and non-numeric entries.

The complete commented source code is included in the project appendix.

## 1.7 Testing and Results

The following tests were performed:

| Test | Input   | Expected result       | Status |
| ---- | ------- | --------------------- | ------ |
| 1    | 4 disks | 15 movements          | Passed |
| 2    | 3 disks | 7 movements           | Passed |
| 3    | 0 disks | Error message         | Passed |
| 4    | hello   | Invalid input message | Passed |

The test results confirmed that the program correctly performs the Tower of Hanoi movements and handles invalid user input.

## 1.8 Time and Space Complexity

The minimum number of movements required to solve the Tower of Hanoi puzzle is:

T(n) = 2^n - 1

For three disks:

T(3) = 2^3 - 1 = 7 movements.

For four disks:

T(4) = 2^4 - 1 = 15 movements.

**Time Complexity:** O(2^n), because the number of movements grows exponentially with the number of disks.

**Space Complexity:** O(n), because recursive function calls are stored on the call stack, with a maximum recursion depth proportional to the number of disks.

## 1.9 Conclusion

The Tower of Hanoi problem was successfully implemented using recursion in Python. The program accepts user input, validates the input and displays the required disk movements.

Testing with three and four disks produced the expected results. The exercise demonstrated how recursion can break a complex problem into smaller, manageable problems.
