
# Store Figure 1 as an adjacency list.
# Each vertex contains its connected neighbours and their edge weights.

graph = {
    # Vertex A connects to D with weight 4.
    "A": {"D": 4},

    # Vertex B connects to D and C.
    "B": {"D": 8, "C": 2},

    # Vertex C connects to B, E and J.
    "C": {"B": 2, "E": 5, "J": 10},

    # Vertex D connects to A, B, F, G, H and K.
    "D": {"A": 4, "B": 8, "F": 6, "G": 3, "H": 9, "K": 6},

    # Vertex E connects to C, H, I and J.
    "E": {"C": 5, "H": 4, "I": 9, "J": 2},

    # Vertex F connects to D, G and K.
    "F": {"D": 6, "G": 1, "K": 7},

    # Vertex G connects to D, F and K.
    "G": {"D": 3, "F": 1, "K": 4},

    # Vertex H connects to D, K, E and I.
    "H": {"D": 9, "K": 6, "E": 4, "I": 3},

    # Vertex I connects to H, E and J.
    "I": {"H": 3, "E": 9, "J": 7},

    # Vertex J connects to C, E, I and L.
    "J": {"C": 10, "E": 2, "I": 7, "L": 1},

    # Vertex K connects to D, F, G and H.
    "K": {"D": 6, "F": 7, "G": 4, "H": 6},

    # Vertex L connects to J.
    "L": {"J": 1}
}



# GRAPH 2: Adjacency list representing the second weighted graph.
# Each vertex stores its directly connected neighbours and edge weights.
# The graph is undirected, so each connection appears in both directions.

graph2 = {
    "A": {"B": 2, "D": 15, "I": 9},  # A connects to B, D, and I.
    "B": {"A": 2, "C": 3, "D": 5, "E": 17},  # B connects to A, C, D, and E.
    "C": {"B": 3, "E": 12, "F": 18},  # C connects to B, E, and F.
    "D": {"A": 15, "B": 5, "E": 4, "G": 6},  # D connects to A, B, E, and G.
    "E": {"B": 17, "C": 12, "D": 4, "F": 13, "G": 11, "H": 7},  # E has six neighbours.
    "F": {"C": 18, "E": 13, "H": 14},  # F connects to C, E, and H.
    "G": {"D": 6, "E": 11, "H": 19, "I": 8, "J": 1},  # G connects to five vertices.
    "H": {"E": 7, "F": 14, "G": 19, "J": 16},  # H connects to E, F, G, and J.
    "I": {"A": 9, "G": 8, "J": 1},  # I connects to A, G, and J.
    "J": {"G": 1, "H": 16, "I": 1}  # J connects to G, H, and I.
}


# Define a function that finds the shortest paths from a starting vertex.
def dijkstra(graph, start):

    # Create a dictionary to store the shortest known distance to each vertex.
    distances = {vertex: float("inf") for vertex in graph}

    # Set the starting vertex distance to zero.
    distances[start] = 0

    # Create a dictionary to remember the previous vertex on each shortest path.
    previous = {vertex: None for vertex in graph}

    # Create a set containing all vertices that have not yet been visited.
    unvisited = set(graph)

    # Continue while there are still unvisited vertices.
    while unvisited:

        # Select the unvisited vertex with the smallest known distance.
        current = min(unvisited, key=lambda vertex: distances[vertex])

        # Stop if the remaining vertices cannot be reached.
        if distances[current] == float("inf"):
            break

        # Mark the selected vertex as visited by removing it.
        unvisited.remove(current)

        # Examine every neighbour connected to the current vertex.
        for neighbour, weight in graph[current].items():

            # Calculate the distance through the current vertex.
            new_distance = distances[current] + weight

            # Check whether this route is shorter than the known route.
            if new_distance < distances[neighbour]:

                # Update the shortest known distance to the neighbour.
                distances[neighbour] = new_distance

                # Record the current vertex as the neighbour's predecessor.
                previous[neighbour] = current

    # Return the shortest distances and predecessor information.
    return distances, previous


# Define a function to rebuild the shortest path to a destination.
def reconstruct_path(previous, destination):

    # Create an empty list to store the path.
    path = []

    # Start from the destination vertex.
    current = destination

    # Continue moving backwards until there is no previous vertex.
    while current is not None:

        # Add the current vertex to the path.
        path.append(current)

        # Move to the vertex that came before the current vertex.
        current = previous[current]

    # Reverse the list to show the path from start to destination.
    path.reverse()

    # Return the completed shortest path.
    return path



# Run the program only when this file is executed directly.
if __name__ == "__main__":

    # Store both graphs in a dictionary so we can process them one after another.
    graphs = {
        "GRAPH 1": graph,
        "GRAPH 2": graph2
    }

    # Process each graph separately.
    for graph_name, current_graph in graphs.items():

        # Display the name of the graph being processed.
        print(f"\n========== {graph_name} ==========")

        # Display the adjacency list of the current graph.
        print("\nADJACENCY LIST:")
        for vertex, neighbours in current_graph.items():
            print(f"{vertex}: {neighbours}")

        # Set A as the starting vertex.
        starting_vertex = "A"

        # Run Dijkstra's algorithm on the current graph.
        distances, previous = dijkstra(current_graph, starting_vertex)

        # Display the shortest paths from A to every other vertex.
        print("\nSHORTEST PATHS FROM VERTEX A:")
        for vertex in current_graph:

            # Reconstruct the shortest path to the current destination.
            path = reconstruct_path(previous, vertex)

            # Display the route and its total cost.
            print(f"A to {vertex}: {' -> '.join(path)} | Cost: {distances[vertex]}")

        # Display the shortest route from A to L for Figure 1 only.
        if graph_name == "GRAPH 1":

            # Reconstruct the shortest path from A to L.
            path_to_l = reconstruct_path(previous, "L")

            # Display the route and its total cost.
            print("\nSHORTEST PATH FROM A TO L:")
            print("Path:", " -> ".join(path_to_l))
            print("Total Cost:", distances["L"])
