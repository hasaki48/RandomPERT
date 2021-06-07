from typing import List


# maps = [
#     [0, [0, 3, 250, 0], [0, 2, 500, 0], 0, [0, 5, 600, 0], 0, 0],
#     [0, 0, 0, 0, [0, 0, 0, 0], [0, 3, 350, 0], 0],
#     [0, 0, 0, [0, 4, 400, 0], 0, 0, [0, 4, 200, 0]],
#     [0, 0, 0, 0, 0, 0,  [0, 2, 700, 0]],
#     [0, 0, 0, 0, 0,  [0, 6, 450, 1000], 0],
#     [0, 0, 0, 0, 0, 0, [0, 3, 700, 5000]],
#     [0, 0, 0, 0, 0, 0, 0]
# ]

maps = [
    [0, [0, 3, -700, 0], 0, [0, 2, -700, 0], [0, 4, -200, 0], 0, 0],
    [0, 0, [0, 6, -450, -5000], 0, 0, [0, 3, -350, 0], 0],
    [0, 0, 0, 0, 0, [0, 0, 0, 0], [0, 5, -600, -1000]],
    [0, 0, 0, 0, [0, 4, -400, 0], 0, 0],
    [0, 0, 0, 0, 0, 0, [0, 2, -500, 0]],
    [0, 0, 0, 0, 0, 0, [0, 3, -250, 0]],
    [0, 0, 0, 0, 0, 0, 0]
]

time = 0
# money = 4500
money = 1100


def isend() -> bool:
    global maps
    for rows in maps:
        for element in rows:
            if isinstance(element, list):
                if element[0] == 0:
                    return False
    return True


def check_merge(one_paths: List[int], other_paths: List[int]):
    for node in one_paths:
        if node in other_paths:
            one_paths.remove(node)


def check_req(Node) -> bool:
    global maps
    req = True
    [i, j] = find_index(Node)
    for x in range(len(maps[0])):
        if isinstance(maps[x][i], list):
            req &= (maps[x][i][0] == 1)  # *等于1为完成，不等于1为未完成
    return req


def construct(Node: List[int]) -> None:
    global money
    if check_req(Node):
        if Node[1] == 0:
            Node[0] = 1
        else:
            Node[1] -= 1
            money -= Node[2]
            if Node[3] != 0:
                money += Node[3]
                Node[3] = 0


def work(first: List[int], second: List[int], third: List[int]):
    list(map(construct, first))
    list(map(construct, second))
    list(map(construct, third))


def find_index(Node):
    global maps
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == Node:
                return [i, j]


def get_next(Node):
    nodes = []
    [old_i, old_j] = find_index(Node)
    for node in maps[old_j]:
        if isinstance(node, list):
            construct(node)
            nodes.append(node)
    return nodes


def simulate():
    global time
    global money
    global maps
    # first_paths = [maps[0][1]]
    # second_paths = [maps[0][2]]
    # third_paths = [maps[0][4]]
    first_paths = [maps[0][1]]
    second_paths = [maps[0][3]]
    third_paths = [maps[0][4]]
    paths = [first_paths, second_paths, third_paths]
    while isend() == False and time <= 20:
        time += 1
        if time == 8:
            # money += 5000
            money -= 5000
        # if time == 15:
        #     money += 16000
        check_merge(first_paths, second_paths)
        check_merge(first_paths, third_paths)
        check_merge(second_paths, third_paths)
        work(first_paths, second_paths, third_paths)
        for each_paths in paths:
            for node in each_paths:
                if(node[0] == 1):
                    nodes = get_next(node)
                    each_paths.remove(node)
                    for each_node in nodes:
                        each_paths.append(each_node)
                    break
        print("第{}周结束，有{}钱".format(time, money))


if __name__ == "__main__":
    simulate()
