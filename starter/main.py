from search.algorithms import CBS, CBSState, State
from search.map import Map

def read_instances(test_instances):
    problems = []
    with open(test_instances, 'r') as file:
        for line in file:
            starts_instances = []
            goals_instances = []

            list_instance = line.split(",")
            cost = None
            for i in range(0, len(list_instance), 4):
                if i == len(list_instance) - 1:
                    cost = int(list_instance[i])
                    problems.append((starts_instances, goals_instances, cost))
                    break
                start = State(int(list_instance[i]), int(list_instance[i + 1]))
                goal = State(int(list_instance[i + 2]), int(list_instance[i + 3]))

                starts_instances.append(start)
                goals_instances.append(goal)
    return problems

def test_cbs(map, test_instance):
    

    """
    Helper funtion to test the CBS algorithm on a given map using problem instances from a test .txt file.

    Parameters:
    - map: The map on which CBS algorithm will be tested.
    - test_instance: File containing problem instances for testing.

    The function prints information about the map, iterates through problem instances,
    applies the CBS algorithm, and checks if the obtained solution cost matches the expected cost.
    """


    print ("Testing Map: ", map,"\n")

    problems = read_instances(test_instance)
    gridded_map = Map(map)
    for problem in problems:
        cbs_state = CBSState(gridded_map, problem[0], problem[1])
        cbs_search = CBS()
        _, cost = cbs_search.search(cbs_state)

        if cost != problem[2]:
            print('There was a mismatch for problem: ')
            print(problem)
            print('Expected: ', problem[2])
            print('Obtained: ', cost)
            print()
        else:
            print('Correctly Solved: ', problem[2], cost)
pass



def main():

    gridded_map = Map("dao-map/test_map.map")
    starts = [State(1, 1), State(5, 1)]
    goals = [State(4, 1), State(2, 1)]
    cbs_state = CBSState(gridded_map, starts, goals)
    print("Cost:",cbs_state.compute_cost())

    cbs_search = CBS()
    paths, cost = cbs_search.search(cbs_state)
    print('Cost of the easy test: ', cost)
    if paths is not None:
        print('Solution paths encountered for the easy test: ')
        for agent, path in paths.items():
            print(agent, path)
        print()

    name_map = "dao-map/combat2.map"
    name_map1 = "dao-map/den009d.map"
    test_instances0 = "test-instances/instances.txt"
    test_instances1 = "test-instances/instances1.txt"

    test_cbs(name_map, test_instances0)
    test_cbs(name_map1, test_instances1)
    
    # problems = read_instances(test_instances)
    # gridded_map = Map(name_map)
    # for problem in problems:
    #     cbs_state = CBSState(gridded_map, problem[0], problem[1])
    #     cbs_search = CBS()
    #     _, cost = cbs_search.search(cbs_state)

    #     if cost != problem[2]:
    #         print('There was a mismatch for problem: ')
    #         print(problem)
    #         print('Expected: ', problem[2])
    #         print('Obtained: ', cost)
    #         print()
    #     else:
    #         print('Correctly Solved: ', problem[2], cost)


if __name__ == "__main__":
    main()