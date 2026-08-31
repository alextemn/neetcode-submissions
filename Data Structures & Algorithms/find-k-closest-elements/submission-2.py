class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # use a max heap, we add tuples to it and heapify based on the first element
        out = []
        l, r = 0, len(arr) - 1
        closest = float('inf')
        pos = None

        while l <= r:
            mid = (l+r) // 2
            dif = abs(arr[mid] - x)
            if arr[mid] == x:
                pos = mid
                break
            if dif < closest:
                closest = dif
                pos = mid
            elif dif == closest and mid < pos:
                pos = mid

            if arr[mid] > x:
                r = mid - 1
            else:
                l = mid + 1
        out.append(arr[pos])
        l, r = pos - 1, pos + 1

        while len(out) < k:
            left, right = float('inf'), float('inf')
            if l >= 0:
                left = abs(arr[l] - x)
            if r < len(arr):
                right = abs(arr[r] - x)

            if left <= right:
                out.append(arr[l])
                l -= 1
            else:
                out.append(arr[r])
                r += 1
        return sorted(out)