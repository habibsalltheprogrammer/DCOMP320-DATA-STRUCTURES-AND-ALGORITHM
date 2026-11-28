# PROBLEM 4: DIJKSTRA'S ALGORITHM

## 4.1 Introduction

Dijkstra's Algorithm is a graph traversal algorithm used to find the shortest paths from a starting vertex to all other vertices in a weighted graph.

A weighted graph consists of vertices (also called nodes) connected by edges. Each edge has a numerical value called a weight or cost. These weights may represent distance, time, or another measurable cost.

Dijkstra's Algorithm works by starting at a selected vertex and repeatedly selecting the unvisited vertex with the smallest known distance. It then checks the neighbouring vertices and updates their distances whenever a shorter route is discovered.

In this project, Dijkstra's Algorithm is implemented using Python to solve the two weighted graph problems provided in the assignment. Both graphs use vertex A as the starting point.

The implementation calculates the shortest paths from A to every other vertex in each graph. It also identifies the lowest-cost path from A to L in Figure 1 and calculates its total cost.

## 4.2 Objectives

The objectives of this problem are:

1. To understand how Dijkstra's Algorithm works in weighted graphs.
2. To represent the provided graphs using Python adjacency lists.
3. To implement Dijkstra's Algorithm using Python.
4. To calculate the shortest paths from vertex A to all other vertices in both figures.
5. To identify the lowest-cost path from A to L in Figure 1.
6. To calculate and display the total cost of the shortest path.
7. To represent both graphs using adjacency matrices.
8. To explain the algorithm's execution step by step.

## 4.3 Graph Representation Using Adjacency Lists

An adjacency list is a method of representing a graph in which each vertex is stored together with a list of its neighbouring vertices and the weights of the connecting edges.

In this project, Python dictionaries are used to represent the adjacency lists. Each vertex serves as a dictionary key, while its neighbouring vertices and their corresponding edge weights are stored as nested dictionary entries.

Both graphs provided in the assignment are undirected weighted graphs. Therefore, every connection is represented in both directions using the same weight.

### 4.3.1 Figure 1 Adjacency List

The first graph contains twelve vertices, labelled A to L. The following adjacency list represents its connections and edge weights:

```python
graph = {
    "A": {"D": 4},
    "B": {"D": 8, "C": 2},
    "C": {"B": 2, "E": 5, "J": 10},
    "D": {"A": 4, "B": 8, "F": 6, "G": 3, "H": 9, "K": 6},
    "E": {"C": 5, "H": 4, "I": 9, "J": 2},
    "F": {"D": 6, "G": 1, "K": 7},
    "G": {"D": 3, "F": 1, "K": 4},
    "H": {"D": 9, "K": 6, "E": 4, "I": 3},
    "I": {"H": 3, "E": 9, "J": 7},
    "J": {"C": 10, "E": 2, "I": 7, "L": 1},
    "K": {"D": 6, "F": 7, "G": 4, "H": 6},
    "L": {"J": 1}
}
```

### 4.3.2 Figure 2 Adjacency List

The second graph contains ten vertices, labelled A to J. Its connections and edge weights are represented as follows:

```python
graph2 = {
    "A": {"B": 2, "D": 15, "I": 9},
    "B": {"A": 2, "C": 3, "D": 5, "E": 17},
    "C": {"B": 3, "E": 12, "F": 18},
    "D": {"A": 15, "B": 5, "E": 4, "G": 6},
    "E": {"B": 17, "C": 12, "D": 4, "F": 13, "G": 11, "H": 7},
    "F": {"C": 18, "E": 13, "H": 14},
    "G": {"D": 6, "E": 11, "H": 19, "I": 8, "J": 1},
    "H": {"E": 7, "F": 14, "G": 19, "J": 16},
    "I": {"A": 9, "G": 8, "J": 1},
    "J": {"G": 1, "H": 16, "I": 1}
}
```

The adjacency lists make it possible for the algorithm to access each vertex's neighbours and their corresponding weights when calculating the shortest paths.

## 4.4 Python Implementation of Dijkstra's Algorithm

Dijkstra's Algorithm was implemented in Python using dictionaries and sets to manage graph information and calculate the shortest paths.

The implementation uses the following variables:

- **distances:** Stores the shortest known distance from the starting vertex to every other vertex.
- **previous:** Stores the previous vertex in the shortest route. This information is later used to reconstruct the complete path.
- **unvisited:** Stores the vertices that have not yet been processed.
- **current:** Represents the vertex currently being examined.
- **neighbour:** Represents a vertex directly connected to the current vertex.
- **weight:** Represents the cost of travelling along an edge.

### 4.4.1 Dijkstra's Algorithm Code

The following Python function implements Dijkstra's Algorithm:

```python
def dijkstra(graph, start):

    # Set the initial distance of every vertex to infinity.
    distances = {vertex: float("inf") for vertex in graph}

    # Set the distance of the starting vertex to zero.
    distances[start] = 0

    # Store the previous vertex for each vertex.
    previous = {vertex: None for vertex in graph}

    # Place all vertices in the unvisited set.
    unvisited = set(graph)

    # Continue while there are unvisited vertices.
    while unvisited:

        # Find the unvisited vertex with the smallest distance.
        current = min(unvisited, key=lambda vertex: distances[vertex])

        # Stop if the remaining vertices cannot be reached.
        if distances[current] == float("inf"):
            break

        # Mark the current vertex as visited.
        unvisited.remove(current)

        # Examine every neighbour of the current vertex.
        for neighbour, weight in graph[current].items():

            # Calculate the new possible distance.
            new_distance = distances[current] + weight

            # Update the distance if a shorter route is found.
            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance

                # Record the previous vertex in the shortest route.
                previous[neighbour] = current

    # Return the shortest distances and previous vertices.
    return distances, previous
```

### 4.4.2 Explanation of the Algorithm

The algorithm operates as follows:

1. It assigns infinity to the initial distance of every vertex because no route has been calculated yet.
2. It assigns zero to the starting vertex A because the distance from A to itself is zero.
3. It creates a dictionary called `previous` to remember the previous vertex in each shortest path.
4. It places all vertices into an unvisited set.
5. It selects the unvisited vertex with the smallest known distance.
6. It examines the neighbours of that vertex and calculates possible new distances.
7. If a shorter route is found, the distance is updated and the previous vertex is recorded.
8. The current vertex is removed from the unvisited set.
9. The process continues until all reachable vertices have been processed.
10. Finally, the algorithm returns the shortest distances and the previous-vertex information.

### 4.4.3 Reconstructing the Shortest Path

After calculating the shortest distances, the program uses another function to reconstruct the actual route between the starting vertex and a destination.

```python
def reconstruct_path(previous, destination):

    # Create an empty list to store the path.
    path = []

    # Start from the destination vertex.
    current = destination

    # Follow the previous vertices until no previous vertex remains.
    while current is not None:

        # Add the current vertex to the path.
        path.append(current)

        # Move to the previous vertex.
        current = previous[current]

    # Reverse the path to obtain the route from start to destination.
    path.reverse()

    # Return the completed shortest path.
    return path
```

The function starts at the destination and follows the previous-vertex information backwards until it reaches the starting vertex. It then reverses the list to display the path in the correct order.

For example, the shortest route from A to L in Figure 1 is displayed as:

**A → D → H → E → J → L**

## 4.5 Step-by-Step Application of Dijkstra's Algorithm to Figure 1

The first graph contains twelve vertices, from A to L. Dijkstra's Algorithm was applied using A as the starting vertex.

At the beginning, the distance to A is set to zero, while the distances to all other vertices are set to infinity because no paths have been explored.

The algorithm then selects the unvisited vertex with the smallest known distance and examines its neighbouring vertices.

### 4.5.1 Algorithm Execution

The following table shows the order in which the vertices are processed and the distance updates made during execution.

| Step | Selected Vertex | Distance from A | Important Distance Updates            |
| ---- | --------------- | --------------: | ------------------------------------- |
| 1    | A               |               0 | D = 4                                 |
| 2    | D               |               4 | B = 12, F = 10, G = 7, H = 13, K = 10 |
| 3    | G               |               7 | F = 8, K remains 10                   |
| 4    | F               |               8 | No shorter route found                |
| 5    | K               |              10 | No shorter route found                |
| 6    | B               |              12 | C = 14                                |
| 7    | H               |              13 | E = 17, I = 16                        |
| 8    | C               |              14 | No shorter route found                |
| 9    | I               |              16 | No shorter route found                |
| 10   | E               |              17 | J = 19                                |
| 11   | J               |              19 | L = 20                                |
| 12   | L               |              20 | Destination reached                   |

The table shows how the algorithm progressively discovers shorter routes and updates the distances whenever a cheaper route is found.

### 4.5.2 Calculation of the Shortest Path from A to L

The shortest route from A to L is:

**A → D → H → E → J → L**

The individual edge weights are:

- A to D = 4
- D to H = 9
- H to E = 4
- E to J = 2
- J to L = 1

The total cost is calculated as follows:

Total Cost = 4 + 9 + 4 + 2 + 1

**Total Cost = 20**

Therefore, the shortest path from A to L is A → D → H → E → J → L, with a minimum total cost of 20.

### 4.5.3 Final Shortest Paths for Figure 1

After completing the algorithm, the following shortest paths and distances were obtained:

| Destination | Shortest Path from A  | Total Cost |
| ----------- | --------------------- | ---------: |
| A           | A                     |          0 |
| B           | A → D → B             |         12 |
| C           | A → D → B → C         |         14 |
| D           | A → D                 |          4 |
| E           | A → D → H → E         |         17 |
| F           | A → D → G → F         |          8 |
| G           | A → D → G             |          7 |
| H           | A → D → H             |         13 |
| I           | A → D → H → I         |         16 |
| J           | A → D → H → E → J     |         19 |
| K           | A → D → K             |         10 |
| L           | A → D → H → E → J → L |         20 |

These results were obtained by running the Python implementation and checking the shortest distances from the starting vertex A.

## 4.6 Adjacency Matrices of the Two Graphs

An adjacency matrix is a square matrix used to represent the connections and edge weights between vertices in a graph.

The rows and columns represent the vertices. Each entry indicates the weight of the direct connection between two vertices.

In this project:

- A numerical value represents the weight of a direct connection.
- Zero (0) represents the absence of a direct connection.
- The diagonal entries are zero because the distance from a vertex to itself is zero.
- Both matrices are symmetrical because the graphs are undirected.

### 4.6.1 Figure 1 Adjacency Matrix

Figure 1 contains twelve vertices, labelled A to L. Its adjacency matrix is shown below.

|     |   A |   B |   C |   D |   E |   F |   G |   H |   I |   J |   K |   L |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| A   |   0 |   0 |   0 |   4 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| B   |   0 |   0 |   2 |   8 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| C   |   0 |   2 |   0 |   0 |   5 |   0 |   0 |   0 |   0 |  10 |   0 |   0 |
| D   |   4 |   8 |   0 |   0 |   0 |   6 |   3 |   9 |   0 |   0 |   6 |   0 |
| E   |   0 |   0 |   5 |   0 |   0 |   0 |   0 |   4 |   9 |   2 |   0 |   0 |
| F   |   0 |   0 |   0 |   6 |   0 |   0 |   1 |   0 |   0 |   0 |   7 |   0 |
| G   |   0 |   0 |   0 |   3 |   0 |   1 |   0 |   0 |   0 |   0 |   4 |   0 |
| H   |   0 |   0 |   0 |   9 |   4 |   0 |   0 |   0 |   3 |   0 |   6 |   0 |
| I   |   0 |   0 |   0 |   0 |   9 |   0 |   0 |   3 |   0 |   7 |   0 |   0 |
| J   |   0 |   0 |  10 |   0 |   2 |   0 |   0 |   0 |   7 |   0 |   0 |   1 |
| K   |   0 |   0 |   0 |   6 |   0 |   7 |   4 |   6 |   0 |   0 |   0 |   0 |
| L   |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   1 |   0 |   0 |

### 4.6.2 Figure 2 Adjacency Matrix

Figure 2 contains ten vertices, labelled A to J. Its adjacency matrix is shown below.

|     |   A |   B |   C |   D |   E |   F |   G |   H |   I |   J |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| A   |   0 |   2 |   0 |  15 |   0 |   0 |   0 |   0 |   9 |   0 |
| B   |   2 |   0 |   3 |   5 |  17 |   0 |   0 |   0 |   0 |   0 |
| C   |   0 |   3 |   0 |   0 |  12 |  18 |   0 |   0 |   0 |   0 |
| D   |  15 |   5 |   0 |   0 |   4 |   0 |   6 |   0 |   0 |   0 |
| E   |   0 |  17 |  12 |   4 |   0 |  13 |  11 |   7 |   0 |   0 |
| F   |   0 |   0 |  18 |   0 |  13 |   0 |   0 |  14 |   0 |   0 |
| G   |   0 |   0 |   0 |   6 |  11 |   0 |   0 |  19 |   8 |   1 |
| H   |   0 |   0 |   0 |   0 |   7 |  14 |  19 |   0 |   0 |  16 |
| I   |   9 |   0 |   0 |   0 |   0 |   0 |   8 |   0 |   0 |   1 |
| J   |   0 |   0 |   0 |   0 |   0 |   0 |   1 |  16 |   1 |   0 |

The adjacency matrices provide a clear representation of the two graphs and can be used to identify the direct connections and their corresponding weights.

## 4.7 Step-by-Step Application of Dijkstra's Algorithm to Figure 2

The second graph contains ten vertices, labelled A to J. Dijkstra's Algorithm was applied using A as the starting vertex.

Initially, the distance to A is zero, while the distances to all other vertices are set to infinity.

The algorithm examines the neighbouring vertices and updates their distances whenever a shorter route is discovered.

### 4.7.1 Examples of Distance Calculations

**Calculation 1: Shortest path from A to B**

The direct connection from A to B has a weight of 2.

Therefore:

Distance = 2

Shortest path: A → B

**Calculation 2: Shortest path from A to C**

The route is A → B → C.

Total cost:

2 + 3 = 5

Shortest path: A → B → C

**Calculation 3: Shortest path from A to E**

The shortest route is A → B → D → E.

Total cost:

2 + 5 + 4 = 11

Shortest path: A → B → D → E

**Calculation 4: Shortest path from A to G**

The shortest route is A → I → J → G.

Total cost:

9 + 1 + 1 = 11

Shortest path: A → I → J → G

### 4.7.2 Final Shortest Paths for Figure 2

The Python implementation produced the following shortest paths and distances from vertex A:

| Destination | Shortest Path from A | Total Cost |
| ----------- | -------------------- | ---------: |
| A           | A                    |          0 |
| B           | A → B                |          2 |
| C           | A → B → C            |          5 |
| D           | A → B → D            |          7 |
| E           | A → B → D → E        |         11 |
| F           | A → B → C → F        |         23 |
| G           | A → I → J → G        |         11 |
| H           | A → B → D → E → H    |         18 |
| I           | A → I                |          9 |
| J           | A → I → J            |         10 |

The results show that Dijkstra's Algorithm successfully calculated the minimum distances from A to all ten vertices in Figure 2.

Unlike Figure 1, Figure 2 does not contain vertex L. Therefore, the A-to-L shortest-path requirement applies to Figure 1 only.

## 4.8 Time and Space Complexity Analysis

Algorithm complexity measures the amount of time and memory required by an algorithm to complete its operations.

### 4.8.1 Time Complexity

The implementation uses an adjacency list to represent the graph.

The algorithm repeatedly searches through the unvisited vertices to select the vertex with the smallest known distance.

The main operations include:

1. Initialising the distance and previous-vertex dictionaries: O(V).
2. Selecting the unvisited vertex with the smallest distance: O(V) per iteration.
3. Processing the neighbouring vertices: O(E) across the graph.

Since the selection operation is repeated for up to V vertices, the overall time complexity is:

**Time Complexity: O(V² + E)**

For a connected undirected graph, this is commonly expressed as:

**O(V²)**

Where:

- V represents the number of vertices.
- E represents the number of edges.

### 4.8.2 Space Complexity

The implementation uses additional memory to store:

- The adjacency list representing the graph.
- The distances dictionary.
- The previous-vertex dictionary.
- The unvisited vertices set.

The adjacency list requires O(V + E) space, while the additional dictionaries and set require O(V) space.

Therefore, the overall space complexity is:

**Space Complexity: O(V + E)**

This implementation is suitable for the two graphs in this assignment.

## 4.9 Testing and Results

The Python implementation was tested using both weighted graphs provided in the assignment.

The tests were performed by running the program in the Python terminal and checking the calculated shortest paths and their total costs.

### 4.9.1 Figure 1 Testing

The first graph contains twelve vertices, labelled A to L.

The program successfully calculated the shortest paths from A to all twelve vertices.

The shortest path from A to L was verified as:

**A → D → H → E → J → L**

The total cost was calculated as:

4 + 9 + 4 + 2 + 1 = 20

**Result: Successful.**

### 4.9.2 Figure 2 Testing

The second graph contains ten vertices, labelled A to J.

The program successfully calculated the shortest paths from A to all ten vertices.

Examples of verified results include:

- A to B: Cost = 2
- A to C: Cost = 5
- A to E: Cost = 11
- A to G: Cost = 11
- A to J: Cost = 10

**Result: Successful.**

### 4.9.3 Adjacency Matrix Testing

A separate Python file named `adjacency_matrices.py` was created to convert both adjacency lists into adjacency matrices.

The program successfully generated:

- A 12 × 12 adjacency matrix for Figure 1.
- A 10 × 10 adjacency matrix for Figure 2.

The matrices were checked to ensure that the connections and weights matched the original graph representations.

**Result: Successful.**

### 4.9.4 Overall Testing Summary

The following tests were completed:

| Test                 | Expected Result        | Actual Result            | Status |
| -------------------- | ---------------------- | ------------------------ | ------ |
| Figure 1 Dijkstra    | Calculate paths from A | Correct paths calculated | Passed |
| Figure 2 Dijkstra    | Calculate paths from A | Correct paths calculated | Passed |
| A to L shortest path | Minimum cost of 20     | Cost of 20               | Passed |
| Figure 1 matrix      | 12 × 12 matrix         | 12 × 12 matrix           | Passed |
| Figure 2 matrix      | 10 × 10 matrix         | 10 × 10 matrix           | Passed |

All implemented tests produced the expected results.

## 4.10 Conclusion

This project successfully demonstrated the implementation and application of Dijkstra's Algorithm using Python.

Two weighted graphs provided in the assignment were represented using adjacency lists and processed using the same Dijkstra function.

The program successfully calculated the shortest paths from vertex A to every other vertex in both graphs. It also identified the shortest route from A to L in Figure 1 as A → D → H → E → J → L, with a total cost of 20.

Furthermore, adjacency matrices were generated for both graphs to provide another method of representing their connections and edge weights.

Through this implementation, the project demonstrated the importance of graph representation, shortest-path calculations, algorithm analysis and Python programming in solving graph-related problems.
