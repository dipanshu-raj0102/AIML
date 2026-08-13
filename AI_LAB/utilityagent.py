import sys 

def reach_goal(grid, source, goal, rewardBlock, penaltyBlock, obstacle):
    horizdist = goal["row"] - source["row"]
    vertdist = goal["col"] - source["col"]
    point = 0

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

    # show initial source position
    print(f'Initial position of Agent: {source["row"], source["col"]}\n')

    # till horizontal distance becomes zero, move to respective direction horizontally step by step
    
    while (horizdist != 0 or vertdist != 0):
        print("\n--- Starting horizontal row movement ---\n")
        while(horizdist > 0):
            if(flag["horizontal"]):
                next = source["row"] + 1
            else:
                next = source["row"] - 1

            if ((next == obstacle["row"]) and source["col"] == obstacle["col"]):
                 print("== obstacle detected in path changing direction ==")
                 break
            source["row"] = next
            print(f'Move {direction["horizontal"]}: Position{source["row"], source["col"]}')
            if (source['row'] == rewardBlock['row'] and source['col'] == rewardBlock['col']):
                print(f"Reached reward block !!!! points + {rewardBlock['value']}")
                point = point + rewardBlock['value']
                print(f"Current points: {point}")

            if (source['row'] == penaltyBlock['row'] and source['col'] == penaltyBlock['col']):
                print(f"Reached penalty block !!!! points - {penaltyBlock['value']}")
                point = point - penaltyBlock['value']
                print(f"Current points: {point}")

            horizdist -= 1

        if (horizdist == 0 and vertdist == 0):
             break
    
        # till vertical distance becomes zero, move to respective direction vertically step by step
        print("\n--- Starting vertical column movement ---\n")
        while(vertdist > 0):
            if(flag["vertical"]):
                next = source["col"] + 1
            else:
                next = source["col"] - 1

            if ((next == obstacle["col"]) and source["row"] == obstacle["row"]):
                print("== obstacle detected changing direction ==")
                break
            source["col"] = next
            print(f'Move {direction["vertical"]}: Position{source["row"], source["col"]}')
            if (source['row'] == rewardBlock['row'] and source['col'] == rewardBlock['col']):
                print(f"Reached reward block !!!! points + {rewardBlock['value']}")
                point = point + rewardBlock['value']
                print(f"Current points: {point}")

            if (source['row'] == penaltyBlock['row'] and source['col'] == penaltyBlock['col']):
                print(f"Reached penalty block !!!! points - {penaltyBlock['value']}")
                point = point - penaltyBlock['value']
                print(f"Current points: {point}")
            vertdist -= 1

    return 0


# function to get dimention. use"dimension of grid" for grid and position of source/goal for their position resp.
def get_dim(name):
    row, col = input(f"Enter {name} (row col): ").strip().split(" ")
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

    rewardBlock = {
        "row": 0,
        "col": 0,
        "value": 10,
    }

    penaltyBlock = {
        "row": 0,
        "col": 0,
        "value": 2,
    }

    obstacle = {
         "row": 0,
         "col": 0,
    }

    grid["row"], grid["col"] = get_dim("dimension of Grid")

    source["row"], source["col"] = get_dim("position of source")

    #checks whether the source is under the boundary of grid
    if ((source["row"] < 0 or source["row"] >= grid["row"]) or (source["col"] < 0 or source["col"] >= grid["col"])):
        print("Error!! Position of source cannot be less than 0 or greater than grid size")
        sys.exit(1)

    goal["row"], goal["col"] = get_dim("position of goal")
    
    # checks whether the goal is under the boundary of grid
    if ((goal["row"] < 0 or goal["row"] >= grid["row"]) or (goal["col"] < 0 or goal["col"] >= grid["col"])):
        print("Error!! Position of goal cannot be less than 0 or greater than grid size")
        sys.exit(1)

    rewardBlock["row"], rewardBlock["col"] = get_dim("position of reward block")

    if ((rewardBlock["row"] < 0 or rewardBlock["row"] >= grid["row"]) or (rewardBlock["col"] < 0 or rewardBlock["col"] >= grid["col"])):
            print("Error!! Position of rewardBlock cannot be less than 0 or greater than grid size")
            sys.exit(1)

    penaltyBlock["row"], penaltyBlock["col"] = get_dim("position of penalty block")

    if ((penaltyBlock["row"] < 0 or penaltyBlock["row"] >= grid["row"]) or (penaltyBlock["col"] < 0 or penaltyBlock["col"] >= grid["col"])):
                print("Error!! Position of penaltyBlock cannot be less than 0 or greater than grid size")
                sys.exit(1)

    obstacle["row"], obstacle["col"] = get_dim("position of obstacle")

    if ((obstacle["row"] < 0 or obstacle["row"] >= grid["row"]) or (obstacle["col"] < 0 or obstacle["col"] >= grid["col"])):
                    print("Error!! Position of obstacle cannot be less than 0 or greater than grid size")
                    sys.exit(1)

    print("\n=== Agent started ===\n")

    # calls function reach_goal() to perform agent movement
    status = reach_goal(grid, source, goal, rewardBlock, penaltyBlock, obstacle)

    print("\n=== Agent completed execution ===\n")

    # checks the return status of reach_goal() function. 0 == success
    if (status == 0):
        print(f'Reached Goal({goal["row"], goal["col"]})')
        print("Agent Shutting Down!! GoodBye!")
    else:
        print("Mission failed!! Agent could not reach the target goal")
        print("Shutting Down!!")
    
    sys.exit(0)

if __name__ == "__main__":
    main()