from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        output = []
        queue = deque([(0, [0])])
        target = len(graph) - 1
        while queue:
            node, route = queue.popleft()
            if node == target:
                output.append(route)
            else:
                for n2 in graph[node]:
                    queue.append((n2, route + [n2]))
        return output

graph = [[1,2],[3],[3],[]]
print(Solution().allPathsSourceTarget(graph))