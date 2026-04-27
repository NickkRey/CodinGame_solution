# game loop
while True:
    enemy1 = input()  # name of enemy 1
    dist1 = int(input())  # distance to enemy 1
    enemy2 = input()  # name of enemy 2
    dist2 = int(input())  # distance to enemy 2

    # Check the distance of which enemy is closest
    if dist1 <= dist2:
        print(enemy1)
    else:
        print(enemy2)