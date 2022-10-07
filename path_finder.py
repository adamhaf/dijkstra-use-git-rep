"""on this file we first generate the graph building,
 then we will take the use input and send him the shortest path """

from queue import PriorityQueue
import buildinginfrastructure

BULLDING_NAME = "Hey, please enter the name of the building: "
FLOOR_ADDRESS_LIST = "enter each address of floor file, separate them with " \
                     "space ' ': "
STARIES_ADDRESS = "Enter the address of the stairs: "
CURRENT_FLOOR = "Hey, please enter the level of the floor your in: "
INITIA_CURRENT = "Enter the initial of the room\junction you are in " \
                 "(for example j3,r2) :"
FLOOR_DEST = "Enter the lever of floor you are wishing to go: "
INITIAL_DEST = "Enter the initial of the room\junction you want to go" \
               "(for example j3,r2):"
ASSUMING_CURRENT_INPUT = "Note: we assuming correct input here"


def dijkstra(start_vertex, floor):
    """using algorithm dijkstra we will find the shortest path in
    the floor"""
    vertex_weights = {v: [float('inf'), 'NAN'] for v in floor.nodes}
    vertex_weights[start_vertex][0] = 0

    visited = []
    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited.append(current_vertex)

        for neighbor in floor.nodes[current_vertex].neighbors.values():
            # since we dont what him to got to other floor`s
            if 's' in current_vertex and floor.level != neighbor.level:
                continue
            if neighbor in visited:  # O(n)
                continue
            distance = floor.weight_function(current_vertex, neighbor.initial)
            old_cost = vertex_weights[neighbor.initial][0]
            new_cost = vertex_weights[current_vertex][0] + int(distance)
            if new_cost < old_cost:
                pq.put((new_cost, neighbor.initial))
                vertex_weights[neighbor.initial] = [new_cost, current_vertex]

    return vertex_weights


def graph_bulider():
    """
    here we will get from the user the address necessary to make the building
    graph.
    :return: building object
    """
    name = input(BULLDING_NAME)
    floor_list = input(FLOOR_ADDRESS_LIST)
    floor_list = floor_list.split()
    staires = input(STARIES_ADDRESS)
    return textToGraph.building_maker(name, floor_list, staires)


def user_question_location():
    """question about the current location of the user and his destination """
    print(ASSUMING_CURRENT_INPUT)
    current_floor = input(CURRENT_FLOOR)
    initial_current = input(INITIA_CURRENT)
    floor_dest = input(FLOOR_DEST)
    inital_dest = input(INITIAL_DEST)
    return int(current_floor), initial_current, int(floor_dest), inital_dest


def closest_staris(dijkstra_res):
    """
    finding the closest stairs to the starting point
    :param dijkstra_res:
    :return: initial of the stairs
    """
    min = float('inf')
    closest_staris_initial = ''
    for i in dijkstra_res:
        if 's' in i and dijkstra_res[i][0] < min:
            min = dijkstra_res[i][0]
            closest_staris_initial = i

    return closest_staris_initial


def shortest_path_finder(dijkstra_res, dest):
    """
    using recursion we will find the path to the destination
    :param dijkstra_res:
    :param dest:
    :return: string to the destination
    """
    if dest == 'NAN' or dijkstra_res[dest][0] == 0:
        return dest
    return shortest_path_finder(dijkstra_res, dijkstra_res[dest][1]) + ' ' + \
           dest


def path_str_maker(dijkstra_res, dest):
    """
    managing the recursive call
    :param dijkstra_res:
    :param dest:
    :return: path to destination
    """
    if dest == 's':
        dest = closest_staris(dijkstra_res)
    return shortest_path_finder(dijkstra_res, dest)


def path_find(building):
    """
    here will take the building object and ask the user question about is current
    location and is destination, then we will calculate the shortest path
    :param building:
    :return:
    """
    user_info = user_question_location()
    current_floor = building.floor_list[user_info[0] - 1]
    if user_info[0] == user_info[2]:  # same floor
        return path_str_maker(dijkstra(user_info[1], current_floor),
                              user_info[3])
    path_to_staris = path_str_maker(dijkstra(user_info[1], current_floor), 's')\
        .replace(' ',' -> ')
    dest_floor = building.floor_list[user_info[2] - 1]
    path_to_dest_from_staris = path_str_maker(
        dijkstra("s" + str(user_info[2] - 1), dest_floor), user_info[3])\
        .replace(' ',' -> ')
    return "current floor: " + path_to_staris + \
           "\nnext floor: " + path_to_dest_from_staris


def main():
    pass
