nums = list(map(int,input().split()))
target = int(input())
son1 = -1
son2 = -1

for i in range(len(nums)):
    if nums[i] == target and son1 == -1:
        son1 = i
    elif nums[i] == target and son1 != -1: 
        son2 = i
print([son1,son2])