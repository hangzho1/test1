# n,td,tc = map(int,input().split())
# damage = list1(map(int,input().split()))
# coin = list1(map(int,input().split()))
# count = 0
# def dfs(damage,begin,coin,count,td,tc):
#     if tc <=0:
#         return 
#     if  td < 0:
#         count += 1
#         return 
#     for index in range(begin,n):
#         dfs(damage,index + 1,coin,count,td-damage[index],tc-coin[index])

# dfs(damage,0,coin,count,td,tc)
# print(count)a




# def permute(nums):
#     """
#     :type nums: list1[int]
#     :rtype: list1[list1[int]]
#     """
#     ### size是数组的大小，depth是当前遍历的深度，它的大小和path大小一样
#     ##path是存储已遍历点的数组，used是用来判断原数组哪些点已经用了，还是否可用，res是返回最后的结果
#     def dfs(nums, size, depth, path, used, res):
#             if depth == size:
#                 ##这里着实不懂为什么不是path,而是path[:]呢
#                 res.append(path[:])
#                 return

#             for i in range(size):
#                 if not used[i]:
#                     used[i] = True
#                     path  += [nums[i]]
#                     # path.append(nums[i])

#                     dfs(nums, size, depth+1, path, used, res)

#                     used[i] = False
#                     path.pop()

#     size = len(nums)
#     if len(nums) == 0:
#         return []

#     used = [False for _ in range(size)]
#     res = []
#     dfs(nums, size, 0, [], used, res)
#     return res
# print(permute([1,2,3]))

# nums = list1(map(int,input().split()))
# target = int(input())


# nums = [2,3,6,7]
# target = 7
# def combinationSum(target):
#     def dfs(nums,count,begin,path,target):
#         if target < 0:
#             return 
#         elif target == 0:
#             count +=1
#             res.append(path[:])
#             return count
#         for i in range(begin,len(nums)):
#             path.append(nums[i])
#             dfs(nums,count,i,path,target - nums[i])
#             path.pop()
#         return count
#     res = []
#     path = []
#     if min(nums) > target:
#         return res

#     count = dfs(nums,0,0,path,target)
#     return res,count
# print(combinationSum(target))




    
# 360 烽火台
# n,m,x,k = 5,5,1,2
# nums = [4,4,2,4,4]
""" n,m,x,k = 5,5,1,2
nums = [4,4,2,4,4]
def combinationSum(nums):
    def jia(nums,i,x,k):
        for c in range(i-x,i+x+1):
            if 0 <= c < len(nums):
                nums[c] +=k
        return min(nums)
    def dfs(nums,depth,maxCount,path):
        if depth == m:
            res.append(path) ###输出路径
            count.append(maxCount) ##把每一种可能的结果算出来
            return 
        for i in range(len(nums)):
            nums1 = nums.copy() ## 这里的复制其实就是复制上一次
            maxCount = jia(nums1,i,x,k)
            dfs(nums1,depth + 1,maxCount,path + [i])
            nums1 = nums.copy()
        return count
    maxCount = 0
    res,path,count = [], [],[]
    dfs(nums,0,0,path)
    return count
    # return res,count
print(combinationSum(nums)) """

"""
思迈特组数之和 
n, target = map(int,input().split())
nums = [x for x in range(1,n+1)]
def dfs(nums,begin,path,res,target):
    if target == 0:
        res.append(path)
        return 
    for i in range(begin,n):
        if target < 0:
            break
        dfs(nums,i +1,path + [nums[i]],res,target - nums[i])

path,res = [],[]
dfs(nums,0,path,res,target)

for i in res:
    print(*i)
 """






# n,td,tc = map(int,input().split())
# damage = list1(map(int,input().split()))
# coin = list1(map(int,input().split()))
# pathDamage,list1Damage,list1Coin,pathCoin = [],[],[],[]
# def fightMonster(damage,td,tc):
#     if sum(damage) <= td:
#         return 0 
#     def dfs(damage,coin,list1Damage,list1Coin,pathDamage,pathCoin,begin,td,tc):
#         if tc <=0:
#             return 
#         if  td < 0:
#             list1Coin.append(sum(pathCoin))
#             list1Damage.append(pathDamage)
#             if begin < len(damage):
#                 dfs(damage,coin,list1Damage,list1Coin,pathDamage+[damage[begin]],pathCoin+ [coin[begin]],begin,td-damage[begin],tc-coin[begin])
#             return 
#         for index in range(begin,n):
#             dfs(damage,coin,list1Damage,list1Coin,pathDamage+[damage[index]],pathCoin+ [coin[index]],index+1,td-damage[index],tc-coin[index])

#     dfs(damage,coin,list1Damage,list1Coin,pathDamage,pathCoin,0,td,tc)
# fightMonster(damage,td,tc)
# print(pathDamage,list1Damage,list1Coin,pathCoin)

# n,td,tc = map(int,input().split())
# damage = list1(map(int,input().split()))
# coin = list1(map(int,input().split()))
# pathDamage,list1Damage,list1Coin,pathCoin = [],[],[],[]
# def fightMonster(td,tc):
#     if sum(damage) <= td:
#         return 0 
#     def dfs(pathDamage,pathCoin,begin,td,tc):
#         if tc <=0:
#             return 
#         if  td < 0:
#             list1Coin.append(sum(pathCoin))
#             list1Damage.append(pathDamage)
#             if begin < len(damage):
#                 dfs(pathDamage+[damage[begin]],pathCoin+ [coin[begin]],begin,td-damage[begin],tc-coin[begin])
#             return 
#         for index in range(begin,n):
#             dfs(pathDamage+[damage[index]],pathCoin+ [coin[index]],index+1,td-damage[index],tc-coin[index])

#     dfs(pathDamage,pathCoin,0,td,tc)
# fightMonster(td,tc)
# print(pathDamage,list1Damage,list1Coin,pathCoin)



























# import random
# nums = [random.randint(-10,101) for x in range(10)]
# print(nums)
# for i in range(len(nums) -1):
#     flag = True
#     for j in range(len(nums) - i -1):
#         if(nums[j+1] < nums[j]):
#             nums[j+1],nums[j] = nums[j],nums[j+1]
#             flag = False
#     if flag == True:
#         break
# print(nums)

# s = "hello"
# nums = list1(s)
# hashmap = {"a","e","i","o","u"}
# left,right =0,len(nums)-1
# while left < right:
#     while left <right and  nums[right] not in hashmap:
#         right -=1
#     while left < right and nums[left] not in hashmap:
#         left +=1
#     nums[left],nums[right] = nums[right],nums[left]
#     left+=1
#     right-=1
# print("".join(nums))


# s = "Let's take LeetCode contest"
# s = ["".join(reversed(x)) for x in s.split()]
# print(" ".join(s))










# import random
# nums = [random.randint(1,100) for _ in range(10)]
# print(nums)
# left,right = 0,len(nums)  -1
# while left < right:
#     while left < right and nums[right] % 2 == 0 :
#         right -=1
#     while left < right and nums[left] % 2 != 0:
#         left += 1 
#     nums[left],nums[right] = nums[right],nums[left]
# print(nums)






# n,l,r = map(int,input().split())
# nums = []
# nums.append(n)
# def dfs(nums):
#     flag = True
#     for i in range(len(nums)):
#         if(nums[i] > 1):
#             temp = nums.pop(i)
#             nums.insert(i,temp// 2)
#             nums.insert(i+1,temp % 2)
#             nums.insert(i+2,temp // 2)
#             flag = False
#     if flag:
#         return 
#     else:
#         dfs(nums)
# dfs(nums)
# print(sum(nums[l-1:r])

# nums = [2,1,2]
# print(sum(nums[1:3]))

# string = "abcdesAssayEaaassYyy"
# res,count = 0,0
# key_word = "easy"
# for s in string:
#     if s.lower() == key_word[count]:
#         count += 1
#     if count == 4:
#         count = 0
#         res += 1
# print(res)



# m,n  = map(int,input())
# list1 = [[] for _ in range(m)]

# list1[0][1] = 1
# print(list1)
# Scanner sc  = new Scanner(System.in);
# int m = sc.nextInt(), n = sc.nextInt();
# sc.nextLine();
# for (int i = 0; i < list1.length; i++) {
#     char[] a = sc.nextLine().toCharArray();
#     for (int j = 0; j < a.length; j++) {
#         list1[i][j] = a[j];
#     }
# }
#         System.out.println(redFlower(list1));

#     }
#     public static int redFlower(char[][] list1){
#         int redflower = 0,m = list1.length,n = list1[0].length;
#         for (int i = 0; i < list1.length; i++) {
#             for (int j = 0; j < list1[0].length; j++) {
# //                if(list1[i][i] == 'M'){
# //                    continue;
# //                }
#                   if(list1[i][j] == 'F'){
#                     if(i -1 >= 0 && list1[i-1][j] == 'F'){
#                         redflower++;
#                     }
#                     if(i -1 >= 0 && j+ 1 < n && list1[i-1][j+1] == 'F'){
#                         redflower++;
#                     }
#                     if(j + 1 < n && list1[i][j+1] == 'F'){
#                         redflower++;
#                     }
#                     if(i +1 < m && j+ 1 < n && list1[i + 1][j + 1] == 'F'){
#                         redflower++;
#                     }
#                     if(i +1 < m   && list1[i+1][j] == 'F'){
#                         redflower++;
#                     }
#                     if(i + 1 < m && j-1 >= 0 && list1[i+1][j-1] == 'F'){
#                         redflower++;
#                     }
#                     if(j -1 >= 0 && list1[i][j-1] == 'F'){
#                         redflower++;
#                     }
#                     if(i -1 >= 0  && j- 1 >=0 && list1[i-1][j-1] == 'F'){
#                         redflower++;
#                     }
#                 }
#             }
#         }
#         return redflower/2;
#     }
# }





# nums = [ [1,2], [2,3], [3,4], [1,3] ]
# nums.sort(key = lambda x:x[1])
# print(nums)
# end = -float("inf")
# cnt = 0
# for i in nums:
#     start = i[0]
#     if start >= end:
#         cnt +=1
#         end = i[1]
# print(len(nums) - cnt)

from PIL import Image,ImageOps


def resize_pic(in_name,size):
    img = Image.open(in_name)
    img  = ImageOps.fit(img,(34000,size),Image.ANTIALIAS)
    return img
image  = "E:\Desktop/微信图片_2022010414413817.jpg"
print(Image.open(image).size)
backgroud =  Image.new("RGB",Image.open(image).size,(255,255,255))
backgroud.save("E:/Desktop/back.jpg")
# img = resize_pic(image,20000)
# img.show()
# img.save("E:/Desktop/test2-1.jpg")