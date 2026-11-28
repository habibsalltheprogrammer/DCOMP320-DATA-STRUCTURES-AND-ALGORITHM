# Import the heapq module to manage edges using a priority queue.
import heapq

# Import the two weighted graphs from our Dijkstra implementation.
from dijkstra_algorithm import graph, graph2

# Define a function that uses Prim's Algorithm to find a Minimum Spanning Tree.
def prim_algorithm(current_graph, start_vertex):

    # Create a set to store vertices already included in the MST.
    visited = set()

    # Create a list to store the selected MST edges.
    mst_edges = []

    # Create a variable to calculate the total MST weight.
    total_weight = 0

    # Create a priority queue to store available edges by weight.
    priority_queue = []

    # Mark the starting vertex as visited.
    visited.add(start_vertex)

    # Examine all neighbours connected to the starting vertex.
    for neighbour, weight in current_graph[start_vertex].items():

        # Add each edge to the priority queue.
        heapq.heappush(priority_queue, (weight, start_vertex, neighbour))

    # Continue until the priority queue is empty or all vertices are connected.
    while priority_queue and len(visited) < len(current_graph):

        # Remove the edge with the smallest weight.
        weight, source, destination = heapq.heappop(priority_queue)

        # Skip the edge if its destination is already visited.
        if destination in visited:
            continue

        # Mark the destination vertex as visited.
        visited.add(destination)

        # Record the selected edge in the Minimum Spanning Tree.
        mst_edges.append((source, destination, weight))

        # Add the selected edge's weight to the total.
        total_weight += weight

        # Examine all neighbours of the newly visited vertex.
        for neighbour, edge_weight in current_graph[destination].items():

            # Only add edges leading to unvisited vertices.
            if neighbour not in visited:

                # Store the edge in the priority queue.
                heapq.heappush(
                    priority_queue,
                    (edge_weight, destination, neighbour)
                )

    # Return the selected MST edges and their total weight.
    return mst_edges, total_weight

# Define a function to display the Minimum Spanning Tree results.
def display_prim_results(graph_name, current_graph):

    # Select A as the starting vertex.
    start_vertex = "A"

    # Call Prim's Algorithm to calculate the MST.
    mst_edges, total_weight = prim_algorithm(current_graph, start_vertex)

    # Display the name of the graph.
    print(f"\n========== {graph_name} ==========")

    # Display the algorithm being used.
    print("Algorithm: Prim's Minimum Spanning Tree")

    # Display the starting vertex.
    print(f"Starting Vertex: {start_vertex}")

    # Display a heading for the selected edges.
    print("\nSelected MST Edges:")

    # Number each selected edge starting from 1.
    for number, (source, destination, weight) in enumerate(mst_edges, start=1):

        # Display the edge and its weight.
        print(f"{number}. {source} -- {destination} | Weight: {weight}")

    # Display the total number of selected edges.
    print(f"\nTotal Edges: {len(mst_edges)}")

    # Display the minimum total weight.
    print(f"Total MST Weight: {total_weight}")

    # Check whether all vertices were connected.
    if len(mst_edges) == len(current_graph) - 1:

        # Confirm that a complete Minimum Spanning Tree was found.
        print("Result: Minimum Spanning Tree completed successfully.")

    else:

        # Report that the graph is disconnected.
        print("Result: The graph is disconnected; a complete MST was not found.")

        # Check whether this file is being run directly.
if __name__ == "__main__":

    # Run Prim's Algorithm on Figure 1.
    display_prim_results("FIGURE 1 - PRIM'S ALGORITHM", graph)

    # Run Prim's Algorithm on Figure 2.
    display_prim_results("FIGURE 2 - PRIM'S ALGORITHM", graph2)