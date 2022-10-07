
LOWER_BOUND = 47
UPPER_BOUND = 58
import buildinginfrastructure as br
import path_finder as pf

def node_generator(num_of_node, node_type, level_number, building_number):
    """
    a general function to generate nodes, for each node we will name it as
    the index of the loop: node_type + i . exmaple: j1,r4,s1
    :param num_of_node: number of nodes to generate
    :param node_type:
    :param level_number: floor number
    :param building_number:
    :return: list of nodes
    """
    res = []
    for i in range(num_of_node):
        res.append(br.Node(node_type + "_" + str((i + 1)), level_number, building_number, {}))

    return res


def node_maker(f):
    """"
    creating a lists of nodes for rooms and junction
    :return junc_list, room_list
    """
    with open(f ,'r') as f:
        building_number, junc_number = int(f.readline()), int(f.readline())
        room_number, level_number = int(f.readline()), int(f.readline())
        room_list = node_generator(room_number, 'room', level_number, building_number)
        junc_list = node_generator(junc_number, 'junction', level_number, building_number)
        floor = br.floor(level_number, junc_list[0], junc_list, room_list)

    f.close()
    return junc_list, room_list, floor


def find_nib(nib_line):
    """
    nib_line: string according to the format
    spliting each object(junction or room) into a tuple with information about is
    number and weight
    """
    all_nib = []
    for i in range(3, len(nib_line)):
        if nib_line[i] == 'j' or nib_line[i] == 'r':
            for j in range(i + 1, len(nib_line)):
                if nib_line[j] == ' ':
                    for k in range(j + 1, len(nib_line) + 1):
                        if k == len(nib_line) - 1 or nib_line[k] == ' ':
                            all_nib.append(((nib_line[i]), nib_line[i + 1: j], nib_line[j + 1: k]))
                            break
                    break
    return all_nib

def node_nib_connector(junc_list, room_list, floor, f):
    """
    Connect each node to his neighbors
    :return first node
    """
    f = open(f, 'r')
    for _ in range(4):
        x = f.readline()

    for i in junc_list:
        all_nib = find_nib(str(f.readline()))
        for neighbor in all_nib:
            if neighbor[0] == 'j':
                i.neighbors["junction_" + neighbor[1]] = junc_list \
                    [int(neighbor[1]) - 1]
            if neighbor[0] == 'r':
                i.neighbors["room_" + neighbor[1]] = room_list \
                    [int(neighbor[1]) - 1]
            floor.edges[floor.who_first(neighbor[0] + str(neighbor[1]), "j" + i.type[9:])] = neighbor[2]

    for i in room_list:
        all_nib = find_nib(str(f.readline()))
        for neighbor in all_nib:
            if neighbor[0] == 'j':
                i.neighbors["junction_" + neighbor[1]] = junc_list\
                    [int(neighbor[1]) - 1]
            if neighbor[0] == 'r':
                i.neighbors["room_" + neighbor[1]] = room_list\
                    [int(neighbor[1]) - 1]
            floor.edges[floor.who_first(neighbor[0] + str(neighbor[1]), "r" + i.type[5:])] = neighbor[2]
    f.close()

    return junc_list[0]


def file_stairs_checker():
    pass


def floor_builder(f):
    "Taking a floor file and making from it a fully connected floor "
    junc_list, room_lists, floor = node_maker(f)
    node_nib_connector(junc_list, room_lists, floor, f)
    # floor_test(junc_list, floor, room_lists)
    return floor


#   0  1 2  3 4  5 6
# [s1 1 j1 3 2 j3 3]
def floor_combiner(f, floor_list, building):
    """
    Taking a list of floor and connecting the stairs in the building
    return: building object with connected floor
    """
    building_number = int(f.readline())
    num_of_stairs = int(f.readline())
    stairs_list = node_generator(num_of_stairs, 'stairs', 'NAN', building_number)
    line = f.readline()
    while line:
        stairs_line_to_connect = line.split()
        current_stairs_ptr = stairs_list[int(stairs_line_to_connect[0][1:]) - 1]
        for i in range(1, len(stairs_line_to_connect) - 2, 3):
            current_floor = floor_list[int(stairs_line_to_connect[i]) - 1]
            current_junc_ptr = current_floor.nodes[ 'j' +
            stairs_line_to_connect[i + 1][1:]]

            dic_key_new_edges = current_floor.who_first(
                stairs_line_to_connect[0], stairs_line_to_connect[i + 1])

            current_floor.edges[dic_key_new_edges] = int(
                stairs_line_to_connect[i + 2])

            current_floor.nodes[current_stairs_ptr.initial] \
                = current_stairs_ptr

            current_junc_ptr.neighbors\
                ['stairs_' + stairs_line_to_connect[0][1:]] \
                = current_stairs_ptr
            current_stairs_ptr.neighbors['junction_' + \
                        stairs_line_to_connect[i + 1]
                                         [1:]] = current_junc_ptr

        line = f.readline()


def building_maker(name, list_of_floor, stairs_file):
    """
    Here we will make each floor and connect them to 1
    list_of_floor: a list of floor file address
    stairs_file: file with instruction to where to place stairs
    """
    floor_list_object = [floor_builder(i) for i in list_of_floor]
    new_build = br.building(name, floor_list_object)
    floor_combiner(stairs_file, floor_list_object, new_build)

    return new_build


def main():
    list_floor = ['graph1.txt', 'graph2.txt', 'graph3.txt', 'graph4.txt'
        , 'graph5.txt']
    s = building_maker('bla', list_floor, open('stairs.txt'))
    print(pf.path_find(s))

if __name__=='__main__':
    main()