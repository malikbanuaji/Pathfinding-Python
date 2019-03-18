import time
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=2)

example_map = [
    ['0','0','#','0','0','0'],
    ['0','0','#','0','0','0'],
    ['0','0','#','0','0','0'],
    ['0','0','0','0','0','0'],
    ['0','0','#','0','0','0'],
    ['0','0','#','0','0','0'],
]

def startCoor(x,y):
    example_map[x][y] = 'S'
    return (x,y)

def endCoor(x,y):
    example_map[x][y] = 'E'
    return (x,y)

def findPath(startX, startY, endX, endY):
    start = startCoor(startX, startY)
    end = endCoor(endX, endY)
    pp.pprint(example_map)
    done = False

    to_explore = []
    explored = []
    explored_to_template = []
    step = 1

    while True:
        if done == True:
            print('found')
            for x,y,z in explored_to_template:
                example_map[x][y] = z

            pp.pprint(example_map)
            break

        top = None
        bottom = None
        left = None
        right = None
        if not to_explore:
            print('initiate four rectangle')
            explored.append(start)
            if start[0]-1 >= 0:
                if not example_map[start[0]-1][start[1]] == '#':
                    if (start[0]-1, start[1]) not in explored:
                        top = (start[0]-1, start[1], step)
                        explored.append((start[0]-1, start[1]))
                        to_explore.append((start[0]-1, start[1]))
                        explored_to_template.append(top)

            if start[0]+1 <= 5:
                if not example_map[start[0]-1][start[1]] == '#':
                    if (start[0]+1, start[1]) not in explored:
                        bottom = (start[0]+1, start[1], step)
                        explored.append((start[0]+1, start[1]))
                        explored_to_template.append(bottom)
                        to_explore.append((start[0]+1, start[1]))

            if start[1]-1 >= 0:
                if not example_map[start[0]][start[1]-1] == '#':
                    if (start[0], start[1]-1) not in explored:
                        left = (start[0], start[1]-1, step)
                        explored.append((start[0], start[1]-1))
                        explored_to_template.append(left)
                        to_explore.append((start[0], start[1]-1))

            if start[1]+1 <= 5:
                if not example_map[start[0]][start[1]+1] == '#':
                    if (start[0], start[1]+1) not in explored:
                        right = (start[0], start[1]+1, step)
                        explored.append((start[0], start[1]+1))
                        explored_to_template.append(right)
                        to_explore.append((start[0], start[1]+1))

        else:
            # Check four side of Node
            print('do calculating')
            for x,y in to_explore:
                #top
                if x-1 >= 0:
                    if not example_map[x-1][y] == '#':
                        if (x-1, y) not in explored:
                            top = (x-1, y, step)
                            explored.append((x-1, y))

                #bottom
                if x+1 <= 5:
                    if not example_map[x+1][y] == '#':
                        if (x+1, y) not in explored:
                            bottom = (x+1, y, step)
                            explored.append((x+1, y))
                #left
                if y-1 >= 0:
                    if not example_map[x][y-1] == '#':
                        if (x, y-1) not in explored:
                            left = (x, y-1, step)
                            explored.append((x, y-1))

                #right
                if y+1 <= 5:
                    if not example_map[x][y+1] == '#':
                        if (x, y+1) not in explored:
                            right = (x, y+1, step)
                            explored.append((x, y+1))

            # reset then add new node to explore
            to_explore = []
            four_e = list((top, bottom, left, right))
            for eachNode in four_e:
                if eachNode:
                    if (eachNode[0], eachNode[1]) == end:
                        done = True
                    else:
                        to_explore.append((eachNode[0], eachNode[1]))
                        explored_to_template.append((eachNode[0], eachNode[1], eachNode[2]))

            print(four_e)

            if [None] * 4 == four_e:
                done = True

        step += 1
        time.sleep(0.1)

findPath(0,0,0,5)
