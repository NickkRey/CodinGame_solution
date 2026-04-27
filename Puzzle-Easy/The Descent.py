# game loop
while True:

    # Initialize the highest mountain and shoot with -1 (We don't know which mountain)
    highest = -1
    shoot = -1

    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.

        # If mountain(i) height > highest mountain, set it into the highest
        if mountain_h > highest: 
            highest = mountain_h
            shoot = i
            
    # Then we shoot the position of highest mountain
    print(shoot)