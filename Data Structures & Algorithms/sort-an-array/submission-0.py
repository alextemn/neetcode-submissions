class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, left, mid, right):
            left_part = arr[left:mid + 1]
            right_part = arr[mid + 1:right + 1]

            i = 0
            j = 0
            k = left

            while i < len(left_part) and j < len(right_part):
                if left_part[i] <= right_part[j]:
                    arr[k] = left_part[i]
                    i += 1
                else:
                    arr[k] = right_part[j]
                    j += 1
                k += 1

            while i < len(left_part):
                arr[k] = left_part[i]
                i += 1
                k += 1

            while j < len(right_part):
                arr[k] = right_part[j]
                j += 1
                k += 1

        def merge_sort(arr, left, right):
            if left >= right:
                return

            mid = (left + right) // 2

            merge_sort(arr, left, mid)
            merge_sort(arr, mid + 1, right)
            merge(arr, left, mid, right)

        merge_sort(nums, 0, len(nums) - 1)
        return nums