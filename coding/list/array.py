class Array:

    def max_subarray(self, arr):
        if not arr:
            return 0

        max_sum, prev = arr[0], arr[0]
        for i in range(1, len(arr)):
            prev = max(arr[i], arr[i] + prev)
            max_sum = max(max_sum, prev)
        return max_sum


    def permute(self, arr):
        """
        1) Start from first index.
        2) Swap the current index with another index coming after and fix it.
        3) Move to the next index
        4) Repeat step 2
        :param arr:
        :return:
        """
        if not arr:
            return []
        return self.__permute(arr, 0)

    def __permute(self, nums, i):
        if i >= len(nums):
            return [nums[:]]
        else:
            result = []
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                result = result + self.__permute(nums, i + 1)
                nums[i], nums[j] = nums[j], nums[i]
            return result

    def three_sum(self, arr):
        """
        Find all values with unique index in arr that sum to 0
        :param arr:
        :return:
        """
        arr.sort()
        result = set()
        for i in range(len(arr)):
            k, j = i + 1, len(arr) - 1
            target = -arr[i]
            while k < j:
                sum = arr[k] + arr[j]
                if sum == target:
                    result.add((arr[i], arr[k], arr[j]))
                    k += 1
                    j -= 1
                elif sum < target:
                    k += 1
                else:
                    j -= 1
        return map(lambda x: [x[0], x[1], x[2]], list(result))

    def two_sum_sorted(self, arr, target):
        """
        Assuming Arr is sorted
        :param arr:
        :param target:
        :return:
        """
        result = set()
        i, j = 0, len(arr)-1
        while i < j:
            sum = arr[i] + arr[j]
            if sum == target:
                result.add((arr[i], arr[j]))
                i += 1
                j -= 1
            elif sum < target:
                i += 1
            else:
                j -= 1
        return list(result)

    def get_max_water(self, height):
        """
        We start with a pointer to the beginning and one pointer to end of the list.
        The accumulated water only increases if we find a column higher than the shorter two start/end columns.
        We step toward the higher columns at every point and keep track of max water.
        :param height: is the height of the columns.
        :return: max area of water.
        """
        n = len(height)
        i, j = 0, n - 1
        area = self.__cal_area(height, i, j)
        while i < j:
            if height[i] < height[j]:
                i = self.__find_next_height(height, i, j, 1)
                area = max(self.__cal_area(height, i, j), area)
            else:
                j = self.__find_next_height(height, j, i, -1)
                area = max(self.__cal_area(height, i, j), area)
        return area

    def __find_next_height(self, height, i, j, direction):
        cur = i
        h = height[cur]
        while direction * (j - cur) > 0:
            cur += direction
            if height[cur] > h:
                return cur
        return cur

    def __cal_area(self, height, i, j):
        return min(height[i], height[j]) * (j - i)


    def trap_water(self, height):
        n = len(height)
        left_collected, index = self.__trap(height, 0, n - 1, 1)
        right_collected, index = self.__trap(height, n - 1, index, -1)
        return left_collected + right_collected

    def __trap(self, height, i, j, direction):
        prev_max, prev_max_index, collected, sum = 0, -1, 0, 0

        while direction * (j - i) >= 0:
            h = height[i]
            # Important to change prev max even if the columns are equal to collect the water in case there are no
            # more columns higher.
            if prev_max <= h:
                prev_max = h
                prev_max_index = i
                collected += sum
                sum = 0
            else:
                sum += prev_max - h
            i += direction

        return collected, prev_max_index