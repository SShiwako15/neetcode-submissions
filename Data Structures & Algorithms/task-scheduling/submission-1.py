class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for t in tasks:
            count[ord(t) - ord('A')] += 1
        maxf = max(count)
        freq_maxf = 0
        for i in count:
            freq_maxf += 1 if i == maxf else 0
        time = (maxf - 1)*(n+1) + freq_maxf
        return max(time,len(tasks))