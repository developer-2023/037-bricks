def main():
    print_square_c(10)

# Simplest version
def print_square_a(size):
    for i in range(size):
        print("?" * size)

# Nested loop
def print_square_b(size):
    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            # Print brick
            print("#", end="")
        print()

# Function in loop
def print_square_c(size):

    # Below function can be local or global
    def print_row(n):
        for i in range(n):
            print("#", end="")
        print()

    for i in range(size):
        print_row(size)

main()