class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        pair = [[p,s] for p,s in zip(position, speed)]
        pair.sort(reverse= True)
        num = 0
        time = []
        for p,s in pair:
            time.append((target - p) / s)
            if len(time) > 1 and time[-1] <= time[-2]:
                time.pop()
        return len(time)
            