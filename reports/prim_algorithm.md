# 5. Prim's Algorithm

## 5.1 Introduction

Prim's Algorithm is a greedy graph algorithm used to find the Minimum Spanning Tree (MST) of a connected, weighted, undirected graph.

A Minimum Spanning Tree is a collection of edges that connects all vertices in a graph without forming a cycle, while maintaining the minimum possible total edge weight.

Prim's Algorithm starts from a selected vertex and repeatedly chooses the smallest available edge that connects a visited vertex to an unvisited vertex. This process continues until all vertices have been included in the Minimum Spanning Tree.

In this project, Prim's Algorithm was implemented in Python and tested using the two weighted graphs provided in the DCOMP320 assignment.

The implementation uses a priority queue to select the edge with the smallest weight efficiently.

## 5.2 Objectives

The main objectives of implementing Prim's Algorithm in this project are:

1. To understand the operation of Prim's Greedy Algorithm.
2. To implement Prim's Algorithm using Python.
3. To identify the Minimum Spanning Tree for Figure 1 and Figure 2.
4. To connect all vertices while avoiding cycles.
5. To calculate the minimum total weight of the selected edges.
6. To demonstrate the use of a priority queue in graph algorithms.
7. To analyse the time and space complexity of the algorithm.
8. To compare the Minimum Spanning Tree results obtained from both graphs.

## 5.3 Graph Representation

The two weighted graphs provided in the assignment were represented using adjacency lists in Python.

An adjacency list stores each vertex together with its neighbouring vertices and the corresponding edge weights.

The graphs are undirected. Therefore, when two vertices are connected, the connection is stored in both directions.

### Figure 1

Figure 1 contains 12 vertices, labelled A to L. The graph is represented using the `graph` dictionary imported from the Dijkstra implementation.

### Figure 2

Figure 2 contains 10 vertices, labelled A to J. The graph is represented using the `graph2` dictionary imported from the Dijkstra implementation.

Both graph structures were reused to avoid duplicating the edge information and to ensure consistency between the Dijkstra and Prim implementations.

## 5.4 Python Implementation of Prim's Algorithm

Prim's Algorithm was implemented using Python's `heapq` module, which provides a priority queue.

The algorithm begins by selecting vertex A as the starting vertex. It then adds the available edges connected to A into the priority queue.

The edge with the smallest weight is selected first. If its destination vertex has not already been visited, the edge is added to the Minimum Spanning Tree.

The newly visited vertex is then used to discover additional edges. This process continues until all vertices have been visited or no more connecting edges are available.

The implementation uses the following variables:

- `visited`: A set containing vertices already included in the Minimum Spanning Tree.
- `mst_edges`: A list storing the edges selected for the Minimum Spanning Tree.
- `total_weight`: Stores the sum of the selected edge weights.
- `priority_queue`: Stores available edges in ascending order of weight.

### Main Steps

1. Select a starting vertex.
2. Mark the starting vertex as visited.
3. Insert its available edges into the priority queue.
4. Remove the edge with the smallest weight.
5. Check whether its destination vertex has already been visited.
6. If it has not been visited, add the edge to the Minimum Spanning Tree.
7. Add the edge weight to the total weight.
8. Insert the new vertex's available edges into the priority queue.
9. Repeat until all vertices are connected.

The algorithm avoids cycles by skipping edges whose destination vertices have already been visited.

## 5.5 Application of Prim's Algorithm to Figure 1

Prim's Algorithm was applied to Figure 1 using vertex A as the starting vertex.

Figure 1 contains 12 vertices, labelled A to L. Therefore, its Minimum Spanning Tree must contain exactly 11 edges.

### Selected Minimum Spanning Tree Edges

| Step | Selected Edge | Weight |
| ---- | ------------- | -----: |
| 1    | A – D         |      4 |
| 2    | D – G         |      3 |
| 3    | G – F         |      1 |
| 4    | G – K         |      4 |
| 5    | K – H         |      6 |
| 6    | H – I         |      3 |
| 7    | H – E         |      4 |
| 8    | E – J         |      2 |
| 9    | J – L         |      1 |
| 10   | E – C         |      5 |
| 11   | C – B         |      2 |

### Total Minimum Spanning Tree Weight

The total weight is calculated by adding all the selected edge weights:

4 + 3 + 1 + 4 + 6 + 3 + 4 + 2 + 1 + 5 + 2 = 35

**Total MST Weight = 35**

### Result

The algorithm successfully selected 11 edges and connected all 12 vertices without forming a cycle.

The Minimum Spanning Tree for Figure 1 has a total weight of 35.

## 5.6 Application of Prim's Algorithm to Figure 2

Prim's Algorithm was also applied to Figure 2 using vertex A as the starting vertex.

Figure 2 contains 10 vertices, labelled A to J. Therefore, its Minimum Spanning Tree must contain exactly 9 edges.

### Selected Minimum Spanning Tree Edges

| Step | Selected Edge | Weight |
| ---- | ------------- | -----: |
| 1    | A – B         |      2 |
| 2    | B – C         |      3 |
| 3    | B – D         |      5 |
| 4    | D – E         |      4 |
| 5    | D – G         |      6 |
| 6    | G – J         |      1 |
| 7    | J – I         |      1 |
| 8    | E – H         |      7 |
| 9    | E – F         |     13 |

### Total Minimum Spanning Tree Weight

The total weight is calculated as follows:

2 + 3 + 5 + 4 + 6 + 1 + 1 + 7 + 13 = 42

**Total MST Weight = 42**

### Result

The algorithm successfully selected 9 edges and connected all 10 vertices without forming a cycle.

The Minimum Spanning Tree for Figure 2 has a total weight of 42.

## 5.7 Time and Space Complexity Analysis

The implementation of Prim's Algorithm uses a priority queue implemented with Python's `heapq` module.

### Time Complexity

The priority queue allows the algorithm to select the smallest available edge efficiently.

The main operations include:

- Inserting an edge into the priority queue: O(log E).
- Removing the smallest edge: O(log E).
- Processing vertices and their neighbouring edges.

Using a binary heap and adjacency list, the overall time complexity is:

**O(E log E)**

Where:

- V represents the number of vertices.
- E represents the number of edges.

### Space Complexity

The algorithm uses additional memory to store:

- The visited vertices.
- The selected Minimum Spanning Tree edges.
- The priority queue.

The overall space complexity is:

**O(V + E)**

This includes the adjacency-list graph representation and the additional data structures used by the algorithm.

## 5.8 Testing and Results

Prim's Algorithm was tested using both weighted graphs provided in the assignment.

The program executed successfully and produced the following results:

| Test               |   Figure 1 |   Figure 2 |
| ------------------ | ---------: | ---------: |
| Number of vertices |         12 |         10 |
| Expected MST edges |         11 |          9 |
| Actual MST edges   |         11 |          9 |
| Total MST weight   |         35 |         42 |
| Execution status   | Successful | Successful |

### Testing Observations

1. The algorithm correctly selected the smallest available connecting edges.
2. All vertices were successfully included in their respective Minimum Spanning Trees.
3. No cycles were introduced.
4. The number of selected edges matched the expected V - 1 rule.
5. The total MST weights were calculated correctly.

Both graph tests passed successfully.

## 5.8 Testing and Results

Prim's Algorithm was tested using both weighted graphs provided in the assignment.

The program executed successfully and produced the following results:

| Test               |   Figure 1 |   Figure 2 |
| ------------------ | ---------: | ---------: |
| Number of vertices |         12 |         10 |
| Expected MST edges |         11 |          9 |
| Actual MST edges   |         11 |          9 |
| Total MST weight   |         35 |         42 |
| Execution status   | Successful | Successful |

### Testing Observations

1. The algorithm correctly selected the smallest available connecting edges.
2. All vertices were successfully included in their respective Minimum Spanning Trees.
3. No cycles were introduced.
4. The number of selected edges matched the expected V - 1 rule.
5. The total MST weights were calculated correctly.

Both graph tests passed successfully.

## 5.9 Conclusion

Prim's Algorithm was successfully implemented in Python and tested using the two weighted graphs provided in the DCOMP320 assignment.

The implementation demonstrated how a greedy algorithm can be used to construct a Minimum Spanning Tree by repeatedly selecting the smallest available edge that connects a visited vertex to an unvisited vertex.

For Figure 1, the algorithm produced a Minimum Spanning Tree with 11 edges and a total weight of 35.

For Figure 2, the algorithm produced a Minimum Spanning Tree with 9 edges and a total weight of 42.

The project also demonstrated the use of Python's priority queue through the `heapq` module.

Through this implementation, the group gained practical knowledge of weighted graphs, greedy algorithms, priority queues, Minimum Spanning Trees, and algorithm complexity.
