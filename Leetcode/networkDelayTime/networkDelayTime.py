import collections
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # ------------------------------ Adjacency List Initialization ------------------------------ #

        edges = collections.defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))
        
        # ---------------------- Vars / Miniheap Initialization ---------------------- #

        minHeap = [(0, k)]
        visit = set()
        t = 0

        # ---------------------------- BFS / Miniheap loop --------------------------- #

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)

            # BFS
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1

if __name__ == "__main__":
    times, n, k = [[2,1,1],[2,3,1],[3,4,1]], 4, 2
    print(Solution().networkDelayTime(times, n, k))