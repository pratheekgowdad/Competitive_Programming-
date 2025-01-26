

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """


    if not nums: return []
    n = len(nums)
    res = []
    i = 0
    while i < n:
        for j in range(n):
            currentProduct = 1
            if i == j:
                continue
            elif nums[j] == 0:
                res.append(0)
                break
            else:
                currentProduct *= nums[j]
                res.append(currentProduct)

    return res







mylist = input().split()
print("your answer ->", productExceptSelf(mylist))