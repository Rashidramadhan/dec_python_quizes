
def maxXor(l,r):
    nums = []
    permute = []
    xor_set = []
    for i in range(l,r +1):
        nums.append(i)
    # print(nums)
    for i in range(len(nums)):
        permute.append(nums[i])
    # print(permute)
    for item in nums:
        for elem in permute:
            xor_set.append(elem ^ item)
    # print(set(xor_set))
    xor_list = list(set(xor_set))
    print(max(xor_list))
maxXor(11,12)

# def xor_num(num):
#     elem = num % 8
#     if elem == 0 or elem == 1:
#         return num
#     elif elem == 2 or elem == 3:
#         return 2
#     elif elem == 4 or elem == 5:
#         return num + 2
#     else:
#         return 0
# return xor_num(r) - xor_num(l)
# counting = 1
# while n:
#     b_state = n & 1
#     n >> = 1
#     if b_state == 0:
#         counting *= 2
# print(counting)