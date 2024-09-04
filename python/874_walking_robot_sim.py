def robotSim(commands, obstacles):
    coordinates = [0,0]
    directions = {0:[1,+1],1:[0,+1],2:[1,-1],3:[0,-1]}
    direction = 0
    distances = []
    
    for i in commands:
        if i==-1: direction = (direction+1)%4
        elif i==-2: direction = abs((direction-1)%4)
        else:
            for j in range(i):
                old_coords = coordinates[::]
                coordinates[directions[direction][0]]+=directions[direction][1]
                if coordinates in obstacles:
                    coordinates = old_coords
                    break
        distances.append(sum([i**2 for i in coordinates]))
    return max(distances)

def robotSim_2(commands, obstacles):
    x=y=d=dist=0
    obstacles=set(map(tuple,obstacles))
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    for i in commands:
        if i==-1:d=(d+1)%4
        elif i==-2:d=(d+3)%4
        else:
            for _ in range(i):
                new_x, new_y = x+directions[d][0], y+directions[d][1]
                if (new_x,new_y) in obstacles: break
                x, y = new_x, new_y
                dist = max(dist, x**2+y**2)
    return dist

    
print(robotSim_2([4,-1,4,-2,4],[[2,4]]))