def solution(nums):
    choose = len(nums) // 2
    nums = set(nums)

    answer = min(len(nums), choose)

    return answer

# Solution


def solution(ls):
    return min(len(ls)/2, len(set(ls)))

# think simple. choose shows the maximum number of pokemons that can be chosen if you were picking len(nums)//2 many.
# len(set(ls)) shows the number of unique pokemons in the list. return the minimum of the two.
