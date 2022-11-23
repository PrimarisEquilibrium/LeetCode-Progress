import collections

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        side = len(isConnected)
        adjList = {i:[] for i in range(side)}

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if (isConnected[i][j] == 1 and (i != j)):
                    adjList[i].append(j)

        visited = set()
        province = 0

        def bfs(adjList, s, visited):
            queue = collections.deque()
            queue.append(s)
            visited.add(s)
            while queue:
                node = queue.popleft()
                for neighbor in adjList[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        for node in range(side):
            if node not in visited:
                bfs(adjList, node, visited)
                province += 1
                
        return province

if __name__ == "__main__":
    print(Solution().findCircleNum([[1,0,0,1],
                                    [0,1,1,0],
                                    [0,1,1,1],
                                    [1,0,1,1]]))