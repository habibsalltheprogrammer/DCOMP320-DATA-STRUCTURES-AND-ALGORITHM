# PROBLEM 2: BINARY TREE TRAVERSALS

## 2.1 Introduction

A binary tree is a non-linear data structure in which each node can have a maximum of two children, known as the left child and the right child.

This project implements four binary tree traversal techniques using Python. The tree used in this implementation contains 31 nodes, numbered from 1 to 31, following the binary tree structure provided in the DCOMP320 assignment.

## 2.2 Problem Objective

The objective of this problem is to implement and demonstrate the following binary tree traversal techniques:

1. Pre-order traversal.
2. In-order traversal.
3. Post-order traversal.
4. Level-order traversal.

The program must display the order in which the nodes are visited for each traversal technique.

## 2.3 Binary Tree Structure

The binary tree consists of 31 nodes, with Node 1 as the root node. Each parent node is connected to its left and right children according to the structure provided in the assignment.

The Python implementation uses a Node class to represent individual nodes and a build_tree() function to construct the complete binary tree.

## 2.4 Explanation of the Traversal Techniques

### A. Pre-order Traversal

Pre-order traversal follows the order:

**Root → Left → Right**

The root node is visited first, followed by the left subtree and then the right subtree. This implementation uses recursion.

### B. In-order Traversal

In-order traversal follows the order:

**Left → Root → Right**

The left subtree is visited first, followed by the root node and then the right subtree. This implementation also uses recursion.

### C. Post-order Traversal

Post-order traversal follows the order:

**Left → Right → Root**

The left subtree is visited first, followed by the right subtree. The root node is visited last.

### D. Level-order Traversal

Level-order traversal visits the nodes one level at a time, starting from the root and moving from left to right.

This implementation uses a queue and follows the FIFO (First In, First Out) principle.

### flowchart Pre-order Traversal Diagram

    N1["1 | Visit 1"]
    N2["2 | Visit 2"]
    N3["3 | Visit 17"]
    N4["4 | Visit 3"]
    N5["5 | Visit 10"]
    N6["6 | Visit 18"]
    N7["7 | Visit 25"]
    N8["8 | Visit 4"]
    N9["9 | Visit 7"]
    N10["10 | Visit 11"]
    N11["11 | Visit 14"]
    N12["12 | Visit 19"]
    N13["13 | Visit 22"]
    N14["14 | Visit 26"]
    N15["15 | Visit 29"]
    N16["16 | Visit 5"]
    N17["17 | Visit 6"]
    N18["18 | Visit 8"]
    N19["19 | Visit 9"]
    N20["20 | Visit 12"]
    N21["21 | Visit 13"]
    N22["22 | Visit 15"]
    N23["23 | Visit 16"]
    N24["24 | Visit 20"]
    N25["25 | Visit 21"]
    N26["26 | Visit 23"]
    N27["27 | Visit 24"]
    N28["28 | Visit 27"]
    N29["29 | Visit 28"]
    N30["30 | Visit 30"]
    N31["31 | Visit 31"]

    N1 --> N2
    N1 --> N3
    N2 --> N4
    N2 --> N5
    N3 --> N6
    N3 --> N7
    N4 --> N8
    N4 --> N9
    N5 --> N10
    N5 --> N11
    N6 --> N12
    N6 --> N13
    N7 --> N14
    N7 --> N15
    N8 --> N16
    N8 --> N17
    N9 --> N18
    N9 --> N19
    N10 --> N20
    N10 --> N21
    N11 --> N22
    N11 --> N23
    N12 --> N24
    N12 --> N25
    N13 --> N26
    N13 --> N27
    N14 --> N28
    N14 --> N29
    N15 --> N30
    N15 --> N31

### flowchart In-order Traversal Diagram

    N1["1 | Visit 16"]
    N2["2 | Visit 8"]
    N3["3 | Visit 24"]
    N4["4 | Visit 4"]
    N5["5 | Visit 12"]
    N6["6 | Visit 20"]
    N7["7 | Visit 28"]
    N8["8 | Visit 2"]
    N9["9 | Visit 6"]
    N10["10 | Visit 10"]
    N11["11 | Visit 14"]
    N12["12 | Visit 18"]
    N13["13 | Visit 22"]
    N14["14 | Visit 26"]
    N15["15 | Visit 30"]
    N16["16 | Visit 1"]
    N17["17 | Visit 3"]
    N18["18 | Visit 5"]
    N19["19 | Visit 7"]
    N20["20 | Visit 9"]
    N21["21 | Visit 11"]
    N22["22 | Visit 13"]
    N23["23 | Visit 15"]
    N24["24 | Visit 17"]
    N25["25 | Visit 19"]
    N26["26 | Visit 21"]
    N27["27 | Visit 23"]
    N28["28 | Visit 25"]
    N29["29 | Visit 27"]
    N30["30 | Visit 29"]
    N31["31 | Visit 31"]

    N1 --> N2
    N1 --> N3
    N2 --> N4
    N2 --> N5
    N3 --> N6
    N3 --> N7
    N4 --> N8
    N4 --> N9
    N5 --> N10
    N5 --> N11
    N6 --> N12
    N6 --> N13
    N7 --> N14
    N7 --> N15
    N8 --> N16
    N8 --> N17
    N9 --> N18
    N9 --> N19
    N10 --> N20
    N10 --> N21
    N11 --> N22
    N11 --> N23
    N12 --> N24
    N12 --> N25
    N13 --> N26
    N13 --> N27
    N14 --> N28
    N14 --> N29
    N15 --> N30
    N15 --> N31

### flowchart Post-order Traversal Diagram

    N1["1 | Visit 31"]
    N2["2 | Visit 15"]
    N3["3 | Visit 30"]
    N4["4 | Visit 7"]
    N5["5 | Visit 14"]
    N6["6 | Visit 22"]
    N7["7 | Visit 29"]
    N8["8 | Visit 3"]
    N9["9 | Visit 6"]
    N10["10 | Visit 10"]
    N11["11 | Visit 13"]
    N12["12 | Visit 18"]
    N13["13 | Visit 21"]
    N14["14 | Visit 25"]
    N15["15 | Visit 28"]
    N16["16 | Visit 1"]
    N17["17 | Visit 2"]
    N18["18 | Visit 4"]
    N19["19 | Visit 5"]
    N20["20 | Visit 8"]
    N21["21 | Visit 9"]
    N22["22 | Visit 11"]
    N23["23 | Visit 12"]
    N24["24 | Visit 16"]
    N25["25 | Visit 17"]
    N26["26 | Visit 19"]
    N27["27 | Visit 20"]
    N28["28 | Visit 23"]
    N29["29 | Visit 24"]
    N30["30 | Visit 26"]
    N31["31 | Visit 27"]

    N1 --> N2
    N1 --> N3
    N2 --> N4
    N2 --> N5
    N3 --> N6
    N3 --> N7
    N4 --> N8
    N4 --> N9
    N5 --> N10
    N5 --> N11
    N6 --> N12
    N6 --> N13
    N7 --> N14
    N7 --> N15
    N8 --> N16
    N8 --> N17
    N9 --> N18
    N9 --> N19
    N10 --> N20
    N10 --> N21
    N11 --> N22
    N11 --> N23
    N12 --> N24
    N12 --> N25
    N13 --> N26
    N13 --> N27
    N14 --> N28
    N14 --> N29
    N15 --> N30
    N15 --> N31

### flowchart Level-order Traversal Diagram

N1["1 | Visit 1"]
N2["2 | Visit 2"]
N3["3 | Visit 3"]
N4["4 | Visit 4"]
N5["5 | Visit 5"]
N6["6 | Visit 6"]
N7["7 | Visit 7"]
N8["8 | Visit 8"]
N9["9 | Visit 9"]
N10["10 | Visit 10"]
N11["11 | Visit 11"]
N12["12 | Visit 12"]
N13["13 | Visit 13"]
N14["14 | Visit 14"]
N15["15 | Visit 15"]
N16["16 | Visit 16"]
N17["17 | Visit 17"]
N18["18 | Visit 18"]
N19["19 | Visit 19"]
N20["20 | Visit 20"]
N21["21 | Visit 21"]
N22["22 | Visit 22"]
N23["23 | Visit 23"]
N24["24 | Visit 24"]
N25["25 | Visit 25"]
N26["26 | Visit 26"]
N27["27 | Visit 27"]
N28["28 | Visit 28"]
N29["29 | Visit 29"]
N30["30 | Visit 30"]
N31["31 | Visit 31"]

    N1 --> N2
    N1 --> N3
    N2 --> N4
    N2 --> N5
    N3 --> N6
    N3 --> N7
    N4 --> N8
    N4 --> N9
    N5 --> N10
    N5 --> N11
    N6 --> N12
    N6 --> N13
    N7 --> N14
    N7 --> N15
    N8 --> N16
    N8 --> N17
    N9 --> N18
    N9 --> N19
    N10 --> N20
    N10 --> N21
    N11 --> N22
    N11 --> N23
    N12 --> N24
    N12 --> N25
    N13 --> N26
    N13 --> N27
    N14 --> N28
    N14 --> N29
    N15 --> N30
    N15 --> N31

## 2.6 Traversal Results

After implementing and executing the four traversal algorithms, the following results were obtained from the 31-node binary tree.

### A. Pre-order Traversal

Pre-order visits the root node first, followed by the left subtree and then the right subtree.

**Output:**

1, 2, 4, 8, 16, 17, 9, 18, 19, 5, 10, 20, 21, 11, 22, 23, 3, 6, 12, 24, 25, 13, 26, 27, 7, 14, 28, 29, 15, 30, 31

### B. In-order Traversal

In-order visits the left subtree first, followed by the root node and then the right subtree.

**Output:**

16, 8, 17, 4, 18, 9, 19, 2, 20, 10, 21, 5, 22, 11, 23, 1, 24, 12, 25, 6, 26, 13, 27, 3, 28, 14, 29, 7, 30, 15, 31

### C. Post-order Traversal

Post-order visits the left subtree first, followed by the right subtree and finally the root node.

**Output:**

16, 17, 8, 18, 19, 9, 4, 20, 21, 10, 22, 23, 11, 5, 2, 24, 25, 12, 26, 27, 13, 6, 28, 29, 14, 30, 31, 15, 7, 3, 1

### D. Level-order Traversal

Level-order visits the nodes level by level, starting from the root and moving from left to right. It uses a queue data structure.

**Output:**

1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31

## 2.7 Testing and Results

The binary tree traversal program was executed and tested using Python. All four traversal methods were checked to ensure that they visited all 31 nodes in the correct order.

| Test No. | Traversal Method | Expected Result                               | Status |
| -------- | ---------------- | --------------------------------------------- | ------ |
| 1        | Pre-order        | All 31 nodes visited in Root-Left-Right order | Passed |
| 2        | In-order         | All 31 nodes visited in Left-Root-Right order | Passed |
| 3        | Post-order       | All 31 nodes visited in Left-Right-Root order | Passed |
| 4        | Level-order      | All 31 nodes visited level by level           | Passed |

### Testing Observation

The program successfully displayed all 31 nodes for each traversal method without errors.

The results confirmed that:

- Pre-order traversal visits the root before its subtrees.
- In-order traversal visits the root between its left and right subtrees.
- Post-order traversal visits the root after both subtrees.
- Level-order traversal visits nodes level by level using a queue.

**Testing Conclusion:** All four traversal algorithms worked successfully.

## 2.8 Time and Space Complexity

Time complexity describes how the execution time of an algorithm increases as the number of nodes increases. Space complexity describes how much additional memory an algorithm requires.

Let **n** represent the total number of nodes in the binary tree and **h** represent the height of the tree.

### A. Pre-order Traversal

- **Time Complexity:** O(n), because every node is visited exactly once.
- **Space Complexity:** O(h), because recursive function calls are stored on the call stack.

### B. In-order Traversal

- **Time Complexity:** O(n), because every node is visited exactly once.
- **Space Complexity:** O(h), because the algorithm uses recursive function calls.

### C. Post-order Traversal

- **Time Complexity:** O(n), because every node is visited exactly once.
- **Space Complexity:** O(h), because recursive calls require memory on the call stack.

### D. Level-order Traversal

- **Time Complexity:** O(n), because every node is removed from the queue and visited once.
- **Space Complexity:** O(n) in the worst case, because the queue may need to store many nodes at the same level.

### Complexity Summary

| Traversal Method | Time Complexity | Space Complexity |
| ---------------- | --------------- | ---------------- |
| Pre-order        | O(n)            | O(h)             |
| In-order         | O(n)            | O(h)             |
| Post-order       | O(n)            | O(h)             |
| Level-order      | O(n)            | O(n)             |

### Explanation

All four traversal algorithms have O(n) time complexity because each node in the binary tree is visited once.

The first three methods use recursion, so their memory requirements depend on the height of the tree. Level-order traversal uses a queue to store nodes waiting to be visited.

For the complete binary tree used in this project, the height grows logarithmically with the number of nodes.

## 2.9 Conclusion

This project successfully demonstrated the implementation of four binary tree traversal techniques using Python: Pre-order, In-order, Post-order, and Level-order traversal.

A complete binary tree containing 31 nodes was constructed based on the structure provided in the assignment.

Each traversal algorithm was implemented and tested successfully. The program displayed the nodes in the correct visiting order for each traversal method.

The project also demonstrated the use of recursion, classes, objects, and the queue data structure in solving binary tree problems.

Through this exercise, we gained a better understanding of how binary trees are structured, how traversal algorithms work, and how different algorithms can be analyzed using time and space complexity.

**Final Result:** All four binary tree traversal algorithms were successfully implemented and executed using Python.
