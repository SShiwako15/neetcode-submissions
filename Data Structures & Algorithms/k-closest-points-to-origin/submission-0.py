class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        output = []
        minHeap = []
        for point in points:
            x1, y1 = point[0], point[1]
            dist = math.sqrt((x1)**2 + (y1)**2)
            heapq.heappush(minHeap, [dist, point])
        while len(output) < k:
            output.append(heapq.heappop(minHeap)[1])
        return output