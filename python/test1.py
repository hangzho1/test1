# nums =list(map(int,input().split()))
# #nums = [3 ,2 ,9 ,-1 ,18]
# def kkpd(nums,low,high):
#     ### 本质上还是一个递归问题，所以必须要有终止条件
    
#     if low >= high:
#         return nums
#     ##这里不能这么写，因为是递归的过程，一直会变化，所以不能赋值稳定的值
# #     i,j = 0,len(nums)-1
#     i,j = low,high
#     ### 基准参考线，随便取
#     base = nums[i]
#     while i < j:
#         ###以做为基准哨兵必须也从j开始，比如2 3 1 0 2 5 3，第一次遍历之后应该为 1 0 2 3 2 5 3
#         ### 而如果从i开始的话就会成为 3 0 1 2 2 5 3（因为不能保证i,j 相遇的值一定比基准值小）
#         while i<j and nums[j] >base:
#             j-=1
#         while i<j and nums [i] <= base:
#             i+=1

#         nums[i],nums[j] = nums[j],nums[i]
#     nums[low],nums[i] = nums[i],nums[low]
    
#     ### 下面两个递归的左右边界参数怎么是个问题
#     kkpd(nums,low,i-1)
#     kkpd(nums,i+1,high)
#     return nums
# kkpd(nums,0,len(nums)-1)



# arr = input().split(",")
# print(arr,type(arr))
# hashmap = {}
# for i in arr:
#     hashmap[i] = hashmap.get(0,i) + 1
# print(hashmap,len(hashmap))
# print(list(hashmap),len(list(hashmap)))


# s = 7
# nums = [2,3,1,2,4,3]
# def minSubArrayLen(s,nums):
#     if sum(nums) < s:
#         return 0
#     minLen = len(nums)
#     for i  in range(len(nums)):
#         for j in range(i,i+minLen):
#             if  sum(nums[i:j+1]) >= s:
#                 minLen = j-i+1
#     return minLen
# minSubArrayLen(s,nums)


# a = [1,2,4,2,4,5,6,5,7,8,9,0]
# b = {}
# b = b.fromkeys(a,1)
# print(b)
# print(list(b.keys()),b.values())



# num = "1000"
# def maxLexicographical( num ):
#     nums = list(num)
#     flag = False
#     for i in range(len(nums)):
#         if nums[i] == '0':
#             nums[i] = '1'
#             flag = True
#             continue
#         if flag and nums[i] == '1':
#             break
#     return "".join(nums)
# print(maxLexicographical(num))


# input1 = input()
# m  = int(input1.split(",")[0])
# k = int(input1.split(",")[1])
# # print(m,k)
# def jinzhi(n,k):
#     b = []
#     while True:
#         s = n//k
#         y = n%k
#         b = b + [y]
#         if s==0:
#             return b
#         n =s
# res,start = 0,1
# while res < m:

#     b = jinzhi(start,k)
#     for i in b:
#         strb = str(i)
#         for j in range(len(strb)):
#             if strb[j] == "1":
#                 res += 1
#     start +=1
# print(start-1)

# n  = int(input())
# preNums = list(map(int,input().split()))

# nums = sorted(preNums)
# left,right = len(nums),0
# for i in range(len(nums)):
#     if nums[i] != preNums[i]:
#         left = min(left,i)
#         right = i
# if right ==0:
#     print(0)
# else:
#     print((right - left+1)//2)



# nums = list(map(int,input().split()))
# print(nums)



# n = int(input())
# str1 = input()
# def count(str1):
#     if not str1:
#         return 0
#     if "B" not in str1 or "R" not in str1:
#         return 1
#     res = []
#     for i in range(len(str1)-1):
#         if str1[i+1] != str1[i] :
#             if i != len(str1) -2:
#                 res.append(str1[i])
#             else:
#                 res.extend([str1[i],str1[i+1]])
        
#         if str1[i+1] == str1[i] and i == len(str1)-2:
#             res.append(str1[i])
#     print(res)
#     hashmap ={}
#     for i in res:
#         hashmap[i] = hashmap.get(i,0) + 1
#     return min(1 + hashmap["B"],1 + hashmap["R"],hashmap["R"] + hashmap["B"])
# print(count(str1))

# heroes = [[60,35,20],[30,40,30],[40,50,40],[50,60,50],[55,45,60]]
# # heroes = [[4,5,1,1],[6,4,2,2],[7,3,3,3]]
# def count(heroes):
#     res = 0
#     m,n = len(heroes),len(heroes[0])
#     for i in range(m-1):
#         for j in range(i+1,m):
#             if heroes[i][0] > heroes[j][0]:
#                 res1 = 1
#             else:
#                 res1 = 0
#             for x in range(n):
#                 if heroes[i][x] > heroes[j][x]:
#                     res2 = 1
#                 else:
#                     res2 = 0
#                 if res1 != res2:
#                     break
#                 if x == n-1:
#                     res += 1
#     return res

# print(count(heroes))




# class TreeNode:
#     def __init__(self,x):
#         self.val = x
#         self.left = None
#         self.right = None

# # def preOrder(root):
# #     ans = []
# #     if not root:
# #         return ans
# #     ans.append(root.val)
# #     ans.extend(preOrder(root.left))
# #     ans.extend(preOrder(root.right))
# #     return ans


# def preOrder(root):
#     stack,ans = [root],[]
#     while stack:
#         i = stack.pop()
#         if isinstance(i,TreeNode):
#             stack.extend([i.right,i.left,i.val])
#         if isinstance(i,int):
#             ans.append(i)
#     return ans



# n,root = map(int,input().split())
# node = {root:TreeNode(root)}
# for _ in range(n):
#     fa,lch,rch = map(int,input().split())
#     if lch != 0:
#         node[lch] = TreeNode(lch)
#         node[fa].left = node[lch]
#     if lch != 0:
#         node[rch] = TreeNode(rch)
#         node[fa].right = node[rch]

# print(preOrder(node[root]))





# a = [1,2,3,4,5]
# b = a[1:3]
# print(a,b)
# b[1] = 100
# print(a,b)


# class TreeNode:
#     def __init__(self,x,left = None,right = None):
#         self.val = x
#         self.left = None
#         self.right = None

# def isValid(root):
#     if not root:
#         return True
#     def dfs(left, right):
#         if not(left or right):
#             return True
#         if not(left and right):
#             return False
#         if left.val != right.val:
#             return False
#         return dfs(left.left,right.right) and dfs(left.right,right.left)

#     return dfs(root.left,root.right)

# node = {1:TreeNode(1)}
# for i in range(3):
#     fa, lch, rch = map(int,input().split())
#     if lch != 0:
#         node[lch] = TreeNode(lch)
#         node[fa].left = node[lch]
#     if rch != 0:
#         node[rch] = TreeNode(rch)
#         node[fa].right = node[rch]
# print(node)
# print(isValid(node[1]))



# s = "abab"

# def number(str1):
#     i = res = 0
#     while "ab" in str1:
#         if str1[i:i+2] =="ab":
#             str1 = str1[:i] + "bba" + str1[i+2:]
#             res += 1
#             res %=1000000007
#             i -= 1
#         else:
#             i += 1
#     return res
# out = number(str1)               
# print(out)
# s = s.replace("ab","bba")
# print(s)



# def is_ab(s):
#     i= res = 0
#     for i in range(len(s)-1):
#         if s[i:i+2] == "ab":
#             res += 1
#             res %= 1000000007
#     return res
# s = input()
# num = is_ab(s)
# while is_ab(s) != 0:
#     s = s.replace("ab","bba")
#     num = num + is_ab(s)
# print(num)
        


# nums = [1,2,3,4,5,6]
# i,j = 1,len(nums)-1

# while i < j:
#     nums.insert(i,nums.pop(j))
#     print(nums)
#     i+=2
# print(nums)


# print ([[x for x in range(1,100)] [i:i+3] for i in range(0,100,3)])
# print ([[x for x in range(1,100)]])

# path1 = [1,3,4]
# a = 0
# def b():
#     # global a
#     # a += 1
#     # return path1
#     c = a +1
#     print(c)

# print(a,b(),path1,a)
# def main():
#     f = open('致橡树.txt', 'r', encoding='utf-8')
#     print(f.read())
#     f.close()


# if __name__ == '__main__':
#     main()

# def longestPalindrome(s):
#     if len(s) <=1:
#         return s 
        
#     def centerSpread(s,left,right):
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             left -= 1
#             right += 1
#         return s[left+1:right]

#     res = ""
#     for i in range(len(s)):
#         odd = centerSpread(s,i,i)
#         even = centerSpread(s,i,i+1)
#         res = max(odd,even,res,key = len)
#     return res 

# print(longestPalindrome("babad"))


# nums = [1,2,3]

# def permute(nums):
#     res,path,n ,boolea = [],[],len(nums),[False]*3

#     def dfs(path):
#         if len(path) == n:
#             return res.append(path[:])
#         for i in range(n):
#             if not boolea[i]:
#                 boolea[i] = True
#                 path.append(nums[i])
#                 dfs(path)
#                 path.pop()
#                 boolea[i] = False
#     dfs(path)
#     return len(res),res

# print(permute(nums))




# nums = [1,2,3]
# a = 100 
# def permute(nums):

#     res,path,n ,boolea = [],[],len(nums),[False]*3
#     def dfs(path):

#         if len(path) == n:
#             return res.append(path)
        

#         for i in range(n):
#             if not boolea[i]:
#                 boolea[i] = True
#                 # path.append(nums[i])
#                 dfs(path + [nums[i]])
#                 # path.pop()
#                 boolea[i] = False
#     dfs(path)
#     return len(res),res,a,n


# n = int(input())
# str1 = input()
# def count(str1):
#     if not str1:
#         return 0
#     if "B" not in str1 or "R" not in str1:
#         return 1
#     res = []
#     for i in range(len(str1)-1):
#         if str1[i+1] != str1[i] :
#             if i != len(str1) -2:
#                 res.append(str1[i])
#             else:
#                 res.extend([str1[i],str1[i+1]])
        
#         if str1[i+1] == str1[i] and i == len(str1)-2:
#             res.append(str1[i])

#     hashmap ={}
#     for i in res:
#         hashmap[i] = hashmap.get(i,0) + 1
#     print(hashmap)
#     return min(1 + hashmap["B"],1 + hashmap["R"],hashmap["R"] + hashmap["B"])
# print(count(str1))



# matrix = [[1,2,3],[4,5,6],[7,8,9]]

# def spiralOrder(matrix):
#     res = []
#     up,down,left,right = 0,len(matrix)-1,0,len(matrix[0])-1
#     while  1:
#         for i in range(left,right+1):
#             res.append(matrix[up][i])
#         up += 1
#         if up > down:
#             break
#         for i in range(up,down+1):
#             res.append(matrix[i][right])
#         right -= 1
#         if right < left:
#             break
#         for i in range(right,left-1,-1):
#             res.append(matrix[down][i])
#         down -= 1
#         if up > down:
#             break
#         for i in range(down,up-1,-1):
#             res.append(matrix[i][left])
#         left += 1
#         if left > right:
#             break
#     return res
# print(spiralOrder(matrix))




# nums = [-1,0,3,5,9,12]
# target=9

# ## 非递归
# def binarySearch():
#     left,right = 0,len(nums)-1
#     while left <= right:
#         mid = left + (right - left)//2
#         if nums[mid] ==target:
#             return  mid
#         if nums[mid] > target:
#             right = mid -1
#         else:
#             left = mid + 1
#     return -1
# print(binarySearch())


# nums = [10,9,2,5,3,7,101,18]

# def lengthOfLIS():
#     if len(nums)<=1:
#         return len(nums)
#     res = [1]*len(nums)
#     for i in range(1,len(nums)):
#         for j in range(i):
#             if nums[j] < nums[i]:
#                 res[i] = max(res[i],res[j]+1)
#     return max(res)

# print(lengthOfLIS())


# import os
# save_path = "G:/study/screencaptura/a/b"
# if not os.path.exists(save_path):
#     os.mkdir(save_path)
    

# a = 100 
# def abb():
    
#     # global a
#     def acc():
#         global a
#         a = 111
#     acc()






# need=collections.defaultdict(int)
# print(need)


# a = [1,2,4,2,4,5,6,5,7,8,9,0]
# b = {}
# b = b.fromkeys(a,1)
# print(b)
# print(list(b.keys()),b.values())


# t = "abc"
# need = {}
# for i in t:
#     # need[i] += 1
#     need[i] = need.get(i,0) + 1
# print(need)


# a = 3
# temp = ""
# temp += str(a) + " "
# temp += "b"
# print(temp)



#法二：理论都是一样的，但是Python 不需要输入那么多的参数
# n,td,tc = map(int,input().split())
# damage = list(map(int,input().split()))
# coin = list(map(int,input().split()))
# pathDamage,listDamage,listCoin,pathCoin = [],[],[],[]
# def fightMonster(td,tc):
#     if sum(damage) <= td:
#         return 0 
#     def dfs(pathDamage,pathCoin,begin,td,tc):
#         if tc <=0:
#             return 
#         if  td < 0:
#             listCoin.append(sum(pathCoin))
#             listDamage.append(pathDamage)
#             if begin < len(damage):
#                 dfs(pathDamage+[damage[begin]],pathCoin+ [coin[begin]],begin,td-damage[begin],tc-coin[begin])
#             return 
#         for index in range(begin,n):
#             dfs(pathDamage+[damage[index]],pathCoin+ [coin[index]],index+1,td-damage[index],tc-coin[index])

#     dfs(pathDamage,pathCoin,0,td,tc)
# fightMonster(td,tc)
# print(pathDamage,listDamage,listCoin,pathCoin,len(listDamage),len(listCoin))



##网易打怪兽

# n,td,tc = map(int,input().split())
# damage = list(map(int,input().split()))
# coin = list(map(int,input().split()))
# pathDamage,listDamage = [],[]
# def fightMonster(td,tc):
#     if sum(damage) <= td:
#         return 0 
#     def dfs(pathDamage,begin,td,tc):
#         if tc <=0:
#             return 
#         if  td < 0:
#             listDamage.append(pathDamage)
#             if begin < len(damage):
#                 dfs(pathDamage+[damage[begin]],begin,td-damage[begin],tc-coin[begin])
#             return 
#         for index in range(begin,n):
#             dfs(pathDamage+[damage[index]],index+1,td-damage[index],tc-coin[index])

#     dfs(pathDamage,0,td,tc)
# fightMonster(td,tc)
# print(pathDamage,listDamage,len(listDamage))



## noAc
# str1 = input()
# def number(str1):
#     i = res = 0
#     while "ab" in str1:
#         if str1[i:i+2] =="ab":
#             str1 = str1[:i] + "bba" + str1[i+2:]
#             res += 1
#             res %=1000000007
#             #这里必须加这个因为aaab第一次编程aabba了
#             i -= 1
#         else:
#             i += 1
#     return res
# out = number(str1)               
# print(out)




a = "Epoch: [0][0/915]	 lr:0.01000 Time 14.648 (14.648)	Loss 8.4618 (8.4618)	Prec@1 0.000 (0.000)"
b = a.split()
print(b)
print(b[-5])
print(b[-1].strip("()"))

# c = "(0.000)"
# print(c.strip("()"))

print("第一行\na")
changed_knobs=[['DelayedAuthenticationMode', 'Delayed Authentication Mode (DAM)', 'Enable/disable Delayed Authentication Mode (DAM)', '0x00', '0x01', 'Disabled: 0x0\nEnabled: 0x1'], ['SncEn', 'SNC', 'Disable supports 1-cluster and 4-IMC way\ninterleave. Enable SNC2 supports 2-clusters SNC\nand 2-way IMC interleave.  Enable SNC4 supports\n4-cluster and 1-IMC way interleave, Auto - Auto\ndecides based on Si Compatibility.', '0x0F', '0x00', 'AUTO: 0xF\nDisable: 0x0\nEnable SNC2 (2-clusters): 0x2\nEnable SNC4 (4-clusters): 0x4'], ['VTdSupport', 'Intel VT for Directed I/O', 'Enable/Disable Intel Virtualization Technology for\nDirected I/O (VT-d) by reporting the I/O device\nassignment to VMM through DMAR ACPI Tables. To\ndisable VT-d, X2APIC must also be disabled.', '0x01', '0x00', 'Enable: 0x1\nDisable: 0x0'], ['ProcessorX2apic', 'Extended APIC', 'Enable/disable extended APIC support    Note:\nWhen enabled, VT-d n Interrupt Remapping will be\nautomatically enabled.', '0x01', '0x00', 'Disable: 0x0\nEnable: 0x1']] 
print(changed_knobs[0],changed_knobs[0][0],changed_knobs[0][1])