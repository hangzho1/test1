# nums = list(map(int,input().split()))
nums = [1,9,3,11,2]
def buffle(nums):
    
    ##外围循环最多只需要len(nums) - 1次
    for i in range(len(nums)-1):
        #提前退出标志位
        temp = False
        for j in range(len(nums)-i-1):
            if nums[j+1] < nums[j]:
                nums[j+1],nums[j] = nums[j],nums[j+1]
                temp = True
        if temp ==False:
            break    
    return nums
print(buffle(nums))