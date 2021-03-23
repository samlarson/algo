class Solution:
    @staticmethod
    def two_sum(nums: list, target: int) -> list:
        # Using both the index and value of list elements, append to a dictionary
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            # If the necessary second integer is in the dict, return, otherwise add to dict
            # Note that 'x in y' searches for index values, so dict index is value, and vice versa
            if m in d:
                return [d[m], i]
            else:
                d[n] = i

    @staticmethod
    def reverse_int(x: int) -> int:
        # Check if negative, strip negativity, set bounds
        neg_bool = False
        if x < 0:
            neg_bool = True
        x = abs(x)
        min_bound = -2 ** 31
        max_bound = 2 ** 31 - 1

        # Cast to string type and iterate in reverse
        z = str(x)
        reverse = ""
        for i in z[::-1]:
            reverse = reverse + i
        answer = int(reverse)

        # Check problem constraints, add back negativity if necessary
        if neg_bool is True:
            answer = -answer

        if answer < min_bound:
            return 0
        elif answer > max_bound:
            return 0
        else:
            return answer

    @staticmethod
    def int_palindrome(x: int) -> bool:
        # Base Case: convert the integer into a string, reverse it, check if order persists
        # x_str = str(abs(x))
        # reverse = ""
        # for i in x_str[::-1]:
        #     reverse = reverse + i
        # reverse_int = int(reverse)
        # if reverse_int == x:
        #     return True
        # else:
        #     return False

        # Optimization: convert to string faster
        # return str(x) == str(x)[::-1]

        # Optimization: no string conversion allowed
        if x < 0:
            return False
        input_num = x
        new_num = 0
        while x > 0:
            new_num = new_num * 10 + x % 10
            x = x // 10
        return new_num == input_num

    @staticmethod
    def search_arr_positions(self, nums: list, target: int) -> list:
        # # Brute Force, O(n) time
        # answer = [-1, -1]
        # if not nums:
        #     return answer
        # if target not in set(nums):
        #     return answer
        # if nums == [target]:
        #     return [0, 0]
        #
        # for i in range(len(nums)):
        #     if nums[i] == target and answer[0] == -1:
        #         answer[0] = i
        #         answer[1] = i
        #     if nums[i] == target and answer[0] != -1:
        #         answer[1] = i
        #     print(answer)
        #
        # return answer

        # Optimization: binary search implementation (come from both ends)
        answer = [-1, -1]

        if not nums:
            return answer
        if target not in set(nums):
            return answer

        answer[0] = self.find_lower(nums=nums, target=target)
        answer[1] = self.find_upper(nums=nums, target=target)
        return answer

    @staticmethod
    def find_lower(nums, target):
        index = 0
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                index = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return index

    @staticmethod
    def find_upper(nums, target):
        index = 0
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                index = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return index

    @staticmethod
    def min_temp_dist(times: list) -> int:
        int_list = []
        min_dist = 100000

        for item in times:
            time_h = int(item.split(":")[0]) * 60
            time_m = int(item.split(":")[1])
            time = time_h + time_m
            int_list.append(time)
            if time < 720:
                int_list.append(time + 1440)

        int_list.sort()
        print(int_list)

        for item in range(1, len(int_list)):
            curr_dist = int_list[item] - int_list[item - 1]
            if curr_dist < min_dist:
                min_dist = curr_dist

        return min_dist

