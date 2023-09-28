import heapq

def dijkstra(graph, start, end):
    distances = {location: float('inf') for location in graph}
    distances[start] = 0
    queue = [(0, start)]
    previous = {}

    while queue:
        current_distance, current_location = heapq.heappop(queue)

        if current_location == end:
            path = []

            while current_location in previous:
                path.append(current_location)
                current_location = previous[current_location]

            path.append(start)
            path.reverse()
            return path, distances[end]

        if current_distance > distances[current_location]:
            continue

        for neighbor, distance in graph[current_location]:
            new_distance = current_distance + distance

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))
                previous[neighbor] = current_location

    return None, float('inf')

locations = {
    "Home": [("Store A", 7), ("Store B", 14), ("Intersection", 25)],
    "Store A": [("Home", 7), ("Store B", 5)],
    "Store B": [("School", 7)],
    "School": [("Intersection", 7)],
    "Intersection": [("School", 7)]
}

start_location = "Home"
end_location = "School"

shortest_path, path_weight = dijkstra(locations, start_location, end_location)

if shortest_path:
    print("Shortest path:", shortest_path)
    print("Path weight:", path_weight)

else:
    print("No path found")

 
