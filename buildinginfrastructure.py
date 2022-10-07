def finding_initial(type):
    """
    for each node we define the initial to be the key for the node`s pointer,
    so when we initialize the node we will save the key of the node
    :param type: string
    :return: initial string
    """
    if type[0] == 'j':
        temp = 'j' + type[9:]
    elif type[0] == 's':
        temp = 's' + type[7:]
    else:
        temp = 'r' + type[5:]
    return temp


class Node:
    """
    using graph we will model building such that for each junction, stairs and
    rooms we will generate a node.
    """
    def __init__(self, type, level, building_number, neighbors=None):
        """
        :param type: junction, stairs, room
        :param level: witch level the node is in
        :param building_number:
        :param vertex: list of neighbors
        """
        self.type = type
        self.level = level
        self.building_number = building_number
        self.initial = finding_initial(type)
        self.neighbors = neighbors

    def __lt__(self, other):
        return True

def rooms_and_junc_to_dic(ptr_junc_list,ptr_room_list):
    nodes_list = {v.initial: v for v in ptr_junc_list}
    rooms_list = {v.initial: v for v in ptr_room_list}
    return {**nodes_list,**rooms_list}

class floor:
    """
    for each floor int the building we will make an object
    """
    def __init__(self, level, ptr_floor=None, ptr_junc_list=None,
                 ptr_room_list=None):
        """
        :param level: the number of floor
        :param ptr_floor:
        :param ptr_junc_list:
        :param ptr_room_list:
        """
        self.level = level
        self.ptr_floor = ptr_floor
        self.edges = {}
        self.nodes = rooms_and_junc_to_dic(ptr_junc_list,ptr_room_list)


    def weight_function(self, start, finish):
        """
        the weight function of the building that describe the distance between
        each node
        :param start:
        :param finish:
        :return: int with weighet of the floor
        """
        s = self.who_first(start, finish)
        return self.edges[self.who_first(start, finish)]

    def who_first(self, start, finish):
        """
        using the Ascii value of the sting we will find out how to connect
        The string of the 2 nodes b
        """
        ""
        if start > finish:
            return start + finish
        else:
            return finish + start


class building:
    def __init__(self, name, floor_list):
        self.name = name
        self.floor_list = floor_list

