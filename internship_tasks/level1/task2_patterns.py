def print_pyramid_pattern():
    print("Number Pattern Generator (Pyramid)")
    try:
        rows = int(input("Enter the number of rows: "))
        
        for i in range(1, rows + 1):
            # Print leading spaces
            for j in range(rows - i):
                print(" ", end=" ")
            
            # Print numbers
            for k in range(1, 2 * i):
                print(k, end=" ")
            
            print() # Newline
            
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    print_pyramid_pattern()
