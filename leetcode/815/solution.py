"""
https://leetcode.com/problems/bus-routes/
815. Bus Routes
"""


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0

        route_to_buses = defaultdict(list)
        for bus, _routes in enumerate(routes):
            for route in _routes:
                route_to_buses[route].append(bus)

        queue = deque([(source, 1)])
        bus_seen = set([])
        while queue:
            route, steps = queue.popleft()
            # print(f"{route=}, {steps=}")
            if route == target:
                return steps
            for bus in filter(lambda b: b not in bus_seen, route_to_buses[route]):
                # print(f"{route=},{bus=}")
                bus_seen.add(bus)
                for new_routes in routes[bus]:
                    queue.append((new_routes, steps + 1))

        return -1
