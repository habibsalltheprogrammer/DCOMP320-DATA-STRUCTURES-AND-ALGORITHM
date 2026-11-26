
# Define a function that solves the Tower of Hanoi puzzle using recursion.
def solve_hanoi(number_of_disks, source, auxiliary, destination):

    # Check whether there is only one disk left to move.
    if number_of_disks == 1:

        # Display the movement of the single disk to its destination.
        print(f"Move disk 1 from {source} to {destination}")

    # Handle the situation where there is more than one disk.
    else:

        # Move the top disks from the source rod to the auxiliary rod.
        solve_hanoi(number_of_disks - 1, source, destination, auxiliary)

        # Display the movement of the largest disk to the destination rod.
        print(f"Move disk {number_of_disks} from {source} to {destination}")

        # Move the smaller disks from the auxiliary rod to the destination rod.
        solve_hanoi(number_of_disks - 1, auxiliary, source, destination)


# Define the main function that starts the Tower of Hanoi program.
def main():

    # Start a try block to handle invalid user input.
    try:

        # Ask the user to enter the number of disks and convert it to an integer.
        number_of_disks = int(input("Enter the number of disks: "))

        # Check that the user entered a positive number of disks.
        if number_of_disks <= 0:

            # Display an error message if the number is zero or negative.
            print("Please enter a number greater than zero.")

        # Continue if the user entered a valid positive number.
        else:

            # Display a heading before showing the disk movements.
            print("\nTower of Hanoi Solution:")

            # Call the recursive function using rods A, B and C.
            solve_hanoi(number_of_disks, "A", "B", "C")

    # Catch an error if the user enters something that is not a whole number.
    except ValueError:

        # Display a helpful message instead of allowing the program to crash.
        print("Invalid input! Please enter a whole number.")

# Check whether this Python file is being run directly.
if __name__ == "__main__":

    # Start the program by calling the main function.
    main()

