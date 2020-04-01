
class Sort:

    def bubble_sort(self, nums):
        if not nums or len(nums) <= 1:
            return nums
        for i in range(len(nums)):
            for j in range(1, len(nums) - i):
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
        return nums

    def select_sort(self, nums):
        if not nums or len(nums) <= 1:
            return nums
        for i in range(len(nums)):
            index = i
            for j in range(i + 1, len(nums)):
                if nums[index] > nums[j]:
                    index = j
            if index != i:
                nums[index], nums[i] = nums[i], nums[index]
        return nums

    def insert_sort(self, nums):
        if not nums or len(nums) <= 1:
            return nums
        for i in range(1, len(nums)):
            cur = nums[i]
            j = i
            while j > 0 and nums[j - 1] > cur:
                nums[j] = nums[j - 1]
                j = j - 1
            nums[j] = cur
        return nums

    def shell_sort(self, nums):
        if not nums or len(nums) <= 1:
            return nums
        gap = len(nums) // 2
        while gap > 0:
            for i in range(gap, len(nums)):
                tmp = nums[i]
                j = i
                while j >= gap and nums[j - gap] > tmp:
                    nums[j] = nums[j - gap]
                    j = j - gap
                nums[j] = tmp
            gap = gap // 2
        return nums

    def heap_sort(self, nums):
        if not nums or len(nums) <= 1:
            return nums
        n = len(nums)
        for i in range((n-2)//2, -1, -1):
            self.head_adjust(nums, i, n-1)
        for i in range(n-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.head_adjust(nums, 0, i-1)
        return nums

    def head_adjust(self, nums, s, l):
        while True:
            child = 2 * s + 1
            if child > l:
                break
            if child < l and nums[child] < nums[child + 1]:
                child = child + 1
            if nums[s] < nums[child]:
                nums[s], nums[child] = nums[child], nums[s]
                s = child
            else:
                break

    def merge_sort(self, nums):
        if not nums or len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        if left:
            result = result + left
        if right:
            result = result + right
        return result

    def merge2(self, nums, low, mid, high):
        result = []
        left = nums[low:mid]
        right = nums[mid:high]
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        if left:
            result = result + left
        if right:
            result = result + right
        nums[low:high] = result

    #归并排序-非递归

    def merge_sort2(self, nums):
        length = len(nums)
        i = 1 #步长
        while i < length:
            low = 0
            while low < length:
                mid = low + i
                high = min(low + 2*i, length)
                if mid < high:
                    self.merge2(nums, low, mid, high)
                low += 2*i
            i = 2*i
        return nums

    def quick_sort(self, nums):
        if len(nums) <= 1:
            return nums
        point = nums[0]
        less = [i for i in nums[1:] if i <= point]
        greater = [i for i in nums[1:] if i > point]
        return self.quick_sort(less) + [point] + self.quick_sort(greater)


a = Sort()
nums = [1,5,3,6,8,3,4,1,6,0]
print(a.quick_sort(nums))
