import sys 

def reach_goal(grid, source, goal):
    horizdist = goal["row"] - source["row"]
    vertdist = goal["col"] - source["col"]

    direction = {
        "horizontal":"right",
        "vertical":"down",
    }
    
    flag = {
        "horizontal": True,
        "vertical": True,
    }

    # if distance is negative reverse direction and set flag to False for row
    if (horizdist < 0):
        flag["horizontal"] = False
        direction["horizontal"] = "left"
        horizdist = -horizdist

    # if distance is negative reverse vertical movement direction and set flag to false
    if (vertdist < 0):
        flag["vertical"] = False
        direction["vertical"] = "up"
        vertdist = -vertdist

    # till horizontal distance becomes zero, move to respective direction horizontally step by step
    while(horizdist > 0):
        if(flag["horizontal"]):
            source["row"] += 1
        else:
            source["row"] -= 1

        print(f"Move {direction["horizontal"]}: Position({source["row"], source["col"]})")
        horizdist -= 1
    
    # till vertical distance becomes zero, move to respective direction vertically step by step
    while(vertdist > 0):
        if(flag["vertical"]):
            source["col"] += 1
        else:
            source["col"] -= 1

        print(f"Move {direction["vertical"]}: Position({source["row"], source["col"]})")
        vertdist -= 1

    return 0


# function to get dimention. use"dimension of grid" for grid and position of source/goal for their position resp.
def get_dim(name):
    row, col = input(f"Enter {name} (row col): ").split(" ")
    row = int(row)
    col = int(col)

    return row, col


def main():
    grid = {
        "row": 0,
        "col": 0,
    }

    source = {
        "row": 0,
        "col": 0,
    }

    goal = {
        "row": 0,
        "col": 0,
    }

    grid["row"], grid["col"] = get_dim("dimension of Grid")

    source["row"], source["col"] = get_dim("position of source")

    #checks whether the source is under the boundary of grid
    if ((source["row"] < 0 or source["row"] > grid["row"]) or (source["col"] < 0 or source["col"] > grid["col"])):
        print("Error!! Position of source cannot be less than 0 or greater than grid size")
        sys.exit(1)

    goal["row"], goal["col"] = get_dim("position of goal")
    
    # checks whether the goal is under the boundary of grid
    if ((goal["row"] < 0 or goal["row"] > grid["row"]) or (goal["col"] < 0 or goal["col"] > grid["col"])):
        print("Error!! Position of goal cannot be less than 0 or greater than grid size")
        sys.exit(1)


    # calls function reach_goal() to perform agent movement
    status = reach_goal(grid, source, goal)

    # checks the return status of reach_goal() function. 0 == success
    if (status == 0):
        print(f"Reached Goal({goal["row"], goal["col"]})")
        print("Agent Shutting Down!! GoodBye!")
    else:
        print("Mission failed!! Agent could not reach the target goal")
        print("Shutting Down!!")
    
    sys.exit(0)

if __name__ == "__main__":
    main()


