rows = 5  # You can change this to any number for different pyramid heights
current_row = 1

while current_row <= rows:
    # Print spaces
    space_count = 1
    while space_count <= (rows - current_row):
        print(" ", end="")
        space_count += 1
    
    # Print stars
    star_count = 1
    while star_count <= (2 * current_row - 1):
        print("*", end="")
        star_count += 1
    
    # Move to the next line after finishing a row
    print()
    
    current_row += 1
