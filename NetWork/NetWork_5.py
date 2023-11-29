import math


def initialize(graph, source):
    # 初始化函数
    # 初始化节点的开销、前驱节点、未访问节点集合和已访问节点集合
    costs = {node: math.inf for node in graph}  # 节点的开销初始为无穷大
    previous_nodes = {node: None for node in graph}  # 前驱节点初始为None
    costs[source] = 0  # 源节点的开销为0
    unvisited_nodes = set(graph.keys())  # 未访问节点集合包含所有节点
    visited_nodes = set()  # 已访问节点集合为空

    return costs, previous_nodes, unvisited_nodes, visited_nodes


def get_min_cost_node(costs, unvisited_nodes):
    # 获取未访问节点中开销最小的节点
    min_cost = math.inf
    min_node = None
    for node in unvisited_nodes:
        if costs[node] < min_cost:
            min_cost = costs[node]
            min_node = node

    return min_node


def update_costs(graph, costs, previous_nodes, current_node):
    # 更新与当前节点相邻节点的开销
    for neighbor, cost in graph[current_node].items():
        new_cost = costs[current_node] + cost
        if new_cost < costs[neighbor]:
            costs[neighbor] = new_cost
            previous_nodes[neighbor] = current_node


def calculate_shortest_paths(graph, source):
    # 计算从源节点到其他节点的最短路径
    costs, previous_nodes, unvisited_nodes, visited_nodes = initialize(graph, source)

    while unvisited_nodes:
        current_node = get_min_cost_node(costs, unvisited_nodes)
        if current_node is None:
            break

        unvisited_nodes.remove(current_node)
        visited_nodes.add(current_node)

        update_costs(graph, costs, previous_nodes, current_node)

    return costs, previous_nodes


def generate_routing_table(costs, previous_nodes):
    # 生成路由表
    routing_table = {}
    for node, cost in costs.items():
        if node != source:
            next_hop = previous_nodes[node]
            routing_table[node] = {'next_hop': next_hop, 'cost': cost}

    return routing_table


def get_shortest_path(previous_nodes, destination):
    # 根据previous_nodes列表获取从源节点到目标节点的最短路径
    path = []
    current_node = destination
    while current_node is not None:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]
    return path


graph = {
    'A': {'B': 7, 'E': 1},
    'B': {'A': 7, 'E': 8, 'C': 1},
    'C': {'B': 1, 'D': 2},
    'D': {'E': 2, 'C': 2},
    'E': {'A': 1, 'B': 8, 'D': 2},
}
source = 'A'

# 计算A点到各点的最短路径距离和路径
costs, previous_nodes = calculate_shortest_paths(graph, source)
shortest_paths = {}
for node in graph:
    if node != source:
        shortest_path = get_shortest_path(previous_nodes, node)
        shortest_paths[node] = {'cost': costs[node], 'path': shortest_path}

# 生成A的路由表
routing_table = generate_routing_table(costs, previous_nodes)

# 输出A的路由表
print("A的路由表：")
for node, route in routing_table.items():
    print(f"节点：{node}，下一跳：{route['next_hop']}，开销：{route['cost']}")

# 输出从A到其他节点的最短路径
print("\n从A到其他节点的最短路径：")
for node, shortest_path in shortest_paths.items():
    print(f"目标节点：{node}，开销：{shortest_path['cost']}，路径：{shortest_path['path']}")
