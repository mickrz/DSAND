import math
import heapq as pq
import copy

def euclidean_distance(a, b, c, d):
    return math.sqrt(math.pow((c - a), 2) + math.pow((d - b), 2))

def calculate_hpath_cost(M, neighbor, goal):
    return euclidean_distance(M.intersections[neighbor][0],\
                              M.intersections[neighbor][1],\
                              M.intersections[goal][0],\
                              M.intersections[goal][1])
# (s,a,s') --> n
def calculate_step_cost(M, start, neighbor):
    return euclidean_distance(M.intersections[start][0],\
                              M.intersections[start][1],\
                              M.intersections[neighbor][0],\
                              M.intersections[neighbor][1])

def goal_test(state, goal):
    return state == goal

def start_test(start):
    return len(explored) == 0

def search_completed():
    return len(frontier_heap) == 0

def generate_final_path(goal):
    if goal in visited.keys():
        final_path.append(goal)
        return generate_final_path(visited[goal])

    final_path.append(goal)
    return final_path

def cleanup():
    frontier.clear()
    explored.clear()
    g_cost.clear()
    frontier_heap.clear()
    visited.clear()
    final_path.clear()

def get_final_path(goal):
    path = copy.deepcopy(generate_final_path(goal))
    path.reverse()
    cleanup()
    return path

    
frontier = set({})
explored = set({})
g_cost = dict({})
frontier_heap = list([])
visited = dict({})
final_path = list([])

def shortest_path(M,start,goal):
    if start_test(start) == True:
        frontier.add(start)
        g_cost[start] = 0
        
    if start in frontier:
        frontier.discard(start)
        explored.add(start)
    else:
        next_node = pq.heappop(frontier_heap)[1]
        return shortest_path(M,next_node,goal)

    if goal_test(start, goal):
        return get_final_path(goal)
    
    for neighbor in M.roads[start]:
        if neighbor not in explored:
            updated_g_cost = 0.0000
            if start in g_cost:
                updated_g_cost = g_cost[start]

            step = calculate_step_cost(M,start,neighbor)
            updated_g_cost += step
            
            if neighbor not in frontier:
                frontier.add(neighbor)

            if neighbor not in g_cost or updated_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = updated_g_cost
                h_cost = calculate_hpath_cost(M,neighbor,goal)
                f_cost = updated_g_cost + h_cost
                visited[neighbor] = start
                pq.heappush(frontier_heap, (f_cost,neighbor))
            
    if (len(frontier_heap)) < 1:
        print("No path is available!")
        return get_final_path(goal)

    next_node = pq.heappop(frontier_heap)[1]
    
    return shortest_path(M,next_node,goal)   