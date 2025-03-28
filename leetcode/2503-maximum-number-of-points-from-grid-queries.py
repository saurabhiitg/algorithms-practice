class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:

        #q = deque()
        from queue import PriorityQueue

        n, m = len(grid), len(grid[0])
        s_queries = sorted(zip(queries, [i for i in range(len(queries))]))

        visited = [[False]*m for _ in range(n)]

        pq = PriorityQueue()
        pq.put((grid[0][0],0,0))
        visited[0][0] = True
        points = 0
        res = [0]*len(queries)

        for q_val, q_idx in s_queries:
            while not pq.empty() and pq.queue[0][0]<q_val:
                _,x,y = pq.get()
                points+=1

                for a,b in [(x-1,y), (x,y-1), (x+1,y), (x, y+1)]:
                    if a<n and a>=0 and b<m and b>=0 and not visited[a][b]:
                        pq.put((grid[a][b],a,b))
                        visited[a][b] = True

            res[q_idx] = points
        
        return res