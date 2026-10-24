def K_BEAM_SEARCH(graph, heuristics, k, s, goal, visited=None):
    if visited is None:
        visited = set()
    if s in visited:
        return None
    visited.add(s)

    if s == goal:
        return [s]

    expanding_node = s
    should_be_explored = []
    temp_heuristics = []
    k_best_heursitic = []


    for item in graph[expanding_node]:
        temp_heuristics.append(heuristics[item])
    temp_heuristics = sorted(temp_heuristics)

    k_best_heursitic = temp_heuristics[-k:]

    for item in graph[expanding_node]:
        if heuristics[item] in k_best_heursitic:
            if item not in should_be_explored:
                should_be_explored.append(item)

    if goal in should_be_explored:
        return [expanding_node, goal]

    for items in should_be_explored:
        result = K_BEAM_SEARCH(graph, heuristics, k, items, goal, visited)
        if result is not None:
            return [expanding_node] + result

    return None


if __name__ == "__main__":
    graph = {0: [1, 2], 1: [0, 3], 2: [0, 4], 3: [1], 4: [2]}
    heuristics = {0: 4, 1: 3, 2: 1, 3: 5, 4: 0}

    print(K_BEAM_SEARCH(graph, heuristics, 2, 0, 4))   # -> [0, 2, 4]
    print(K_BEAM_SEARCH(graph, heuristics, 1, 0, 4))   # -> [0, 2, 4]
    print(K_BEAM_SEARCH(graph, heuristics, 2, 0, 3))   # -> [0, 1, 3] or None (pruned)