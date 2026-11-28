
# Import heapq to help us repeatedly select the two smallest frequencies.
import heapq

# Store the symbols and their frequencies from the assignment.
frequencies = {
    "a": 2,
    "b": 4,
    "c": 8,
    "d": 16,
    "e": 16
}

# Display the heading of our Huffman Coding program.
print("========== HUFFMAN CODING ==========")

# Display the original symbols and their frequencies.
print("\nOriginal Symbol Frequencies:")

# Loop through each symbol and its frequency.
for symbol, frequency in frequencies.items():

    # Display the symbol and its frequency.
    print(f"{symbol}: {frequency}")

# Define a class to represent each node in the Huffman tree.
class HuffmanNode:

    # This method initializes a new Huffman node.
    def __init__(self, symbol, frequency):

        # Store the symbol represented by this node.
        self.symbol = symbol

        # Store the frequency of the symbol or combined group.
        self.frequency = frequency

        # Create an empty reference for the left child.
        self.left = None

        # Create an empty reference for the right child.
        self.right = None

    # Define how Python compares two Huffman nodes by frequency.
    def __lt__(self, other):

        # Return True when this node has a smaller frequency.
        return self.frequency < other.frequency

# Define a function to build the Huffman tree from the frequencies.
def build_huffman_tree(frequencies):

    # Create an empty priority queue.
    priority_queue = []

    # Go through every symbol and its frequency.
    for symbol, frequency in frequencies.items():

        # Create a Huffman node for the current symbol.
        node = HuffmanNode(symbol, frequency)

        # Add the node to the priority queue.
        heapq.heappush(priority_queue, node)

    # Continue combining nodes until only one node remains.
    while len(priority_queue) > 1:

        # Remove the node with the smallest frequency.
        left_node = heapq.heappop(priority_queue)

        # Remove the node with the second-smallest frequency.
        right_node = heapq.heappop(priority_queue)

        # Calculate the combined frequency of both nodes.
        combined_frequency = left_node.frequency + right_node.frequency

        # Create a new parent node with no individual symbol.
        parent_node = HuffmanNode(None, combined_frequency)

        # Connect the first removed node as the left child.
        parent_node.left = left_node

        # Connect the second removed node as the right child.
        parent_node.right = right_node

        # Add the new parent node back into the priority queue.
        heapq.heappush(priority_queue, parent_node)

    # Return the final remaining node as the root of the Huffman tree.
    return priority_queue[0]

# Define a function to generate binary codes from the Huffman tree.
def generate_huffman_codes(root):

    # Create an empty dictionary to store each symbol and its binary code.
    huffman_codes = {}

    # Define a recursive helper function to travel through the tree.
    def generate_codes_recursive(node, current_code):

        # Check whether the current node is empty.
        if node is None:

            # Stop this recursive call if there is no node.
            return

        # Check whether the current node is a leaf containing a symbol.
        if node.symbol is not None:

            # Save the symbol and its generated binary code.
            huffman_codes[node.symbol] = current_code

            # Stop exploring because this symbol has been found.
            return

        # Move to the left child and add 0 to the current code.
        generate_codes_recursive(node.left, current_code + "0")

        # Move to the right child and add 1 to the current code.
        generate_codes_recursive(node.right, current_code + "1")

    # Start generating codes from the root with an empty code.
    generate_codes_recursive(root, "")

    # Return the dictionary containing all Huffman codes.
    return huffman_codes


# Define a function to calculate the total encoded file length.
def calculate_encoded_length(frequencies, huffman_codes):

    # Start the total encoded length at zero.
    total_length = 0

    # Go through every symbol and its frequency.
    for symbol, frequency in frequencies.items():

        # Get the number of bits in the symbol's Huffman code.
        code_length = len(huffman_codes[symbol])

        # Multiply the frequency by the code length.
        symbol_encoded_length = frequency * code_length

        # Add this symbol's encoded length to the total.
        total_length += symbol_encoded_length

    # Return the total encoded length in bits.
    return total_length


# Define a function to encode a text using the Huffman codes.
def encode_text(text, huffman_codes):

    # Create an empty string to store the encoded result.
    encoded_text = ""

    # Go through each character in the original text.
    for symbol in text:

        # Find the binary code assigned to the current symbol.
        code = huffman_codes[symbol]

        # Add the binary code to the encoded result.
        encoded_text += code

    # Return the complete encoded binary string.
    return encoded_text


# Run the main program only when this file is executed directly.
if __name__ == "__main__":

    # Build the Huffman tree using the assignment frequencies.
    root = build_huffman_tree(frequencies)

    # Generate binary codes from the completed Huffman tree.
    huffman_codes = generate_huffman_codes(root)

    # Display the generated Huffman codes.
    print("\nGenerated Huffman Codes:")

    # Display each symbol and its assigned binary code.
    for symbol, code in sorted(huffman_codes.items()):

        # Print the symbol and its binary code.
        print(f"{symbol}: {code}")

    # Create the original text using the given symbol frequencies.
    original_text = "".join(
        symbol * frequency for symbol, frequency in frequencies.items()
    )

    # Encode the original text using the generated Huffman codes.
    encoded_text = encode_text(original_text, huffman_codes)

    # Calculate the total encoded length in bits.
    total_length = calculate_encoded_length(frequencies, huffman_codes)

    # Display the original text.
    print("\nOriginal Text:")
    print(original_text)

    # Display the encoded binary string.
    print("\nEncoded Binary String:")
    print(encoded_text)

    # Display the total number of bits in the encoded string.
    print("\nTotal Encoded File Length:")
    print(total_length, "bits")

    # Display the number of bits in the actual encoded string.
    print("\nEncoded String Length:")
    print(len(encoded_text), "bits")

