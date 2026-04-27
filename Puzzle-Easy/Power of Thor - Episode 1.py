light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move.

    # Initialize direction of x and y
    x=""
    y=""

    # If light_x position != thor_x position
    if initial_tx < light_x:
        x="E"
        initial_tx+=1
    elif initial_tx > light_x:
        x="W"
        initial_tx-=1
        
    # If light_y position != thor_y position
    if initial_ty < light_y:
        y="S"
        initial_ty+=1
    elif initial_ty > light_y:
        y="N"
        initial_ty-=1
        
    print(f"{y}{x}")