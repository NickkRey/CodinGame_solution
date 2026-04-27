import sys

##### THE IDEA #####
    # The solution use Binary Search for searching most effective pattern to move
    # There are two Search to code, X position and Y position
    # 1. Using input information, cut off the position that is definitely not the bomb position
    #    Ex: Given UR (Under Right), then the bomb is not on above or left
    # 2. Search for the mid position of X and Y, then teleport to the mid(x,y) coordinate
    # 3. Update start or end, and mid position
    # 4. Repeat from step 2 until u find the solution

##### SOLUTION #####
# NOTE THAT THIS MAY NOT BE THE MOST OPTIMAL SOLUTION, But it provides more easier solution to understand

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()] # -> position of batman (we'll use it as mid(x,y))

# Initialize the start, end position for Binary Search
start_x = 0
end_x = w-1

start_y = 0
end_y = h-1


# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    
    # Debug Command (ignore it)
    print("Debug message", file=sys.stderr,flush=True)
    # Find if the Y position changes
    if 'U' in bomb_dir:
        end_y = y0 - 1
    
    elif 'D' in bomb_dir:
        start_y = y0 + 1

    # Find if the X position changes 
    if 'L' in bomb_dir:
        end_x = x0 - 1
    
    elif 'R' in bomb_dir:
        start_x = x0 + 1

    # Calculate the mid position of X and Y (Or the positon of batman)
    x0 = (end_x + start_x) // 2
    y0 = (end_y + start_y) // 2
    
    # Finally print the mid(x,y) coordinate
    print(f"{x0} {y0}")