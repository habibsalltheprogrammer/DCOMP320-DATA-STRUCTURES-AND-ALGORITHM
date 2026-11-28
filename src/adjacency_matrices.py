
# DCOMP320 - DATA STRUCTURES AND ALGORITHM
# ADJACENCY MATRICES FOR FIGURE 1 AND FIGURE 2

# Import the two graphs from our Dijkstra algorithm file.
from dijkstra_algorithm import graph, graph2


# This function converts an adjacency list into an adjacency matrix.
def create_adjacency_matrix(current_graph):

    # Get all vertices and arrange them alphabetically.
    vertices = sorted(current_graph.keys())

    # Create an empty matrix with rows and columns for every vertex.
    matrix = []

    # Visit each vertex to create one row.
    for vertex in vertices:

        # Create an empty row for the current vertex.
        row = []

        # Check the connection between the current vertex and every vertex.
        for neighbour in vertices:

            # If a direct connection exists, store its weight.
            if neighbour in current_graph[vertex]:
                row.append(current_graph[vertex][neighbour])

            # If no direct connection exists, store zero.
            else:
                row.append(0)

        # Add the completed row to the matrix.
        matrix.append(row)

    # Return the vertex labels and the completed matrix.
    return vertices, matrix


# This function displays an adjacency matrix in a readable table.
def display_matrix(graph_name, current_graph):

    # Generate the matrix for the selected graph.
    vertices, matrix = create_adjacency_matrix(current_graph)

    # Display the name of the graph.
    print(f"\n========== {graph_name} ==========")

    # Print the column headings.
    print("    " + " ".join(f"{vertex:>4}" for vertex in vertices))

    # Print each row with its vertex label.
    for index, row in enumerate(matrix):

        # Display the row label and all its values.
        print(f"{vertices[index]:>4}" + "".join(f"{value:>5}" for value in row))


# Run the program when this file is executed directly.
if __name__ == "__main__":

    # Display the adjacency matrix for Figure 1.
    display_matrix("FIGURE 1 ADJACENCY MATRIX", graph)

    # Display the adjacency matrix for Figure 2.
    display_matrix("FIGURE 2 ADJACENCY MATRIX", graph2)
