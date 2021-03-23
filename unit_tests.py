import pytest
import warnings
import functions

warnings.simplefilter("error", DeprecationWarning)


# Suppress internal Deprecation Warnings related to PyTest
@pytest.mark.filterwarnings('ignore::DeprecationWarning')
@pytest.mark.essential
@pytest.mark.parametrize("nums, target", [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6)
])
def test_two_sum(nums, target):
    result = functions.Solution.two_sum(nums=nums, target=target)
    answer = nums[result[0]] + nums[result[1]]
    print("\nTesting Two Sum: " + str(nums) + ", " + str(target))
    print("Answer: " + str(answer))
    assert answer == target

# TODO: Reverse Integer Test
# TODO: Integer Palindrome Test
# TODO: Search Array Positions Test


@pytest.mark.essential
@pytest.mark.parametrize("times, target", [
    (["12:00", "06:00", "14:30"], 150),
    (["23:59", "00:04", "22:00"], 5)
])
def test_temp_dist(times, target):
    answer = functions.Solution.min_temp_dist(times=times)
    print("\nTesting Minimum Temporal Distance: " + str(times))
    print("Answer: " + str(answer))
    assert answer == target
