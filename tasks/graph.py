from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        vis = []
        stek = []
        vis.append(self._root)
        stek += self._root.outbound
        while len(stek) != 0:
            if stek[0] not in vis:
                vis.append(stek[0])
            for c, x in enumerate(stek[0].outbound, 1):
                if x not in stek and x not in vis:
                    stek.insert(c, x)
            stek.pop(0)
        return vis

    def bfs(self) -> list[Node]:
        visited = []
        queue = []
        visited.append(self._root)
        queue += self._root.outbound
        while len(queue) != 0:
            visited.append(queue[0])
            queue.pop(0)
            for x in visited[-1].outbound:
                if x not in visited and x not in queue:
                    queue.append(x)

        return visited
