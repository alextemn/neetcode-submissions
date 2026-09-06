class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = ""
        heap = []
        count = 0

        if a > 0:
            heapq.heappush_max(heap, (a, 'a'))
        if b > 0:
            heapq.heappush_max(heap, (b, 'b'))
        if c > 0:
            heapq.heappush_max(heap, (c, 'c'))
        
        while heap:
            c, char = heapq.heappop_max(heap)
            if count < 2:
                s += char
                if len(heap) > 0 and (heap[0][0] > c - 1 or heap[0][0] == c-1 and heap[0][1] > char):
                    count = 0
                elif count + 1 < 3:
                    count += 1
                else:
                    break
                if c-1 != 0:
                    heapq.heappush_max(heap, (c - 1, char))
            elif count >= 2 and len(heap) > 0:
                newC, newChar = heapq.heappop_max(heap)
                heapq.heappush_max(heap, (c, char))
                
                s += newChar
                count = 0

                if newC-1 != 0:
                    heapq.heappush_max(heap, (newC - 1, newChar))
            else:
                break
            print(heap, count)
        return s