# num = list(map(int,input().split(r",")))
# num = [-1, 0, 1, 2, -1, -4]
# nums = sorted(num)
# result = []
# for a in range(len(nums)-2):
#     for b in range( a+1,len(nums)-1):
#         temp = nums[b+1:]
#         if -a-b in temp:
#             print(nums.index(-a-b))
#         result.append([nums[a],nums[b],-a-b])
# print(result)

# nums = list(map(int,input().split()))
# def max_sum(nums):
#     dp = [None]*len(nums)
#     res,dp[0] = nums[0],nums[0]
#     a,b = 0,0
#     hashmap = {}
#     for i in range(1,len(nums)):
#         if dp[i-1]+ nums[i] >= nums[i]:
#             dp[i] = dp[i-1] +nums[i]
#             b = i
#             hashmap[dp[i]] = nums[a:b+1]
#         else:
#             a = b =i
#             hashmap[dp[i]] = nums[a:b+1]
#             dp[i] = nums[i]
#         res = max(res,dp[i])
#     return res,hashmap[res]
# max_sum(nums)

# 1143
# text1 = str(input())
# text2 = str(input())
# text1 = "abcba"
# text2 = "abcbcba"
# def zvih(text1,text2):
#     m,n = len(text1),len(text2)
#     ## 这里定义的有问题，https://blog.csdn.net/yp736628082/article/details/87932962
#     ## 因为列表可以存放不同类型的数据，所以列表可以读取一行，但是不能读取一列
#     dp = [[0]*(n+1)]*(m+1)
#     for i in range(m):
#         for j in range(n):
#             if text1[i] ==text2[j]:
#                 dp[i+1][j+1] = dp[i][j] + 1
#             else:
#                 dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
#     return dp[-1][-1]
# zvih(text1,text2)


# nums = [1,2,3]
# nums = list(map(int,input().split()))
# def permute(nums):
#     def dfs(nums, size, depth, path, used, res):
#         if depth == size:
#             res.append(path[:])
#             return

#         for i in range(size):
#             if not used[i]:
#                 used[i] = True
#                 path.append(nums[i])

#                 dfs(nums, size, depth + 1, path, used, res)

#                 used[i] = False
#                 path.pop()

#     size = len(nums)
#     if len(nums) == 0:
#         return []

#     used = [False for _ in range(size)]
#     res = []
#     dfs(nums, size, 0, [], used, res)
#     print(res)
#     return res

# permute(nums)


# nums = list(map(int,input().split()))
# nums = [1 ,3 ,5  ,6  ,7 ,9 ,10]
# # target = int(input())
# def two_search(nums,low,high,target):
#     if low > high:return -1
#     mid = low + (high - low)//2
#     if nums[mid] == target:
#         # print(mid)
#         return mid
#     elif nums[mid] > target:
#         return two_search(nums,low,mid-1,target)
#     else:
#         return two_search(nums,mid+1,high,target)
# two_search(nums,0,len(nums)-1,5)

##正儿八经的快速排序
# nums = list(map(int,input().split()))
# nums = [3 ,2 ,9 ,-1 ,18]
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
#         while i<j and nums [i] < base:
#             i+=1

#         nums[i],nums[j] = nums[j],nums[i]
#     nums[low],nums[i] = nums[i],nums[low]
    
#     ### 下面两个递归的左右边界参数怎么是个问题
#     kkpd(nums,low,i-1)
#     kkpd(nums,i+1,high)
#     return nums
# kkpd(nums,0,len(nums)-1)



#
# nums = [1,2,4,4,4,5,6,7,7,8]

# if len(nums) <=1:print(len(nums))
# for i in range(1,len(nums)):
#     if nums[i] == nums[i-1]:
#         nums[i] = nums[i] +1 
# print(len(set(nums)))

## 808 分汤
# N = 101

# def soupServings(N):
#     Q, R = divmod(N, 25)
#     N = Q + (R > 0)
#     if N >= 500: return 1

#     memo = {}
#     def dp(x, y):
#         if (x, y) not in memo:
#             if x <= 0 or y <= 0:
#                 ans = 0.5 if x<=0 and y<=0 else 1.0 if x<=0 else 0.0
#             else:
#                 ans = 0.25 * (dp(x-4,y)+dp(x-3,y-1)+dp(x-2,y-2)+dp(x-1,y-3))
#             memo[x, y] = ans
#         return memo[x, y]
#     print(dp(N,N))
#     return dp(N, N)
# soupServings(N)


# n =int(input())
# nums = list(map(int,input().split()))
# import bisect
# n = 5
# l = [1,2,8,6,4]
# dp=[1]*n
# valueList=[l[0]]
# Max=1
# for i in range(1,n):
#     if l[i]>valueList[-1]:
#         Max+=1
#         dp[i]=Max
#         valueList.append(l[i])
#     else:
#         index=bisect.bisect(valueList, l[i])
#         dp[i]=index+1
#         valueList[index]=l[i]
# Max=max(dp)
# res=[]
# index=n-1-l[::-1].index(valueList[-1])
# for i in range(index,-1,-1):
#     if len(res)==0 or (l[i]<res[-1] and Max==dp[i]):
#         res.append(l[i])
#         Max-=1
# print(' '.join(map(str,res[::-1])))

# n = 7
# nums = [2,1,3,4,3,1,4]
# if n <=1:print(n)
# temp = [nums[0]]
# for i in range(1,len(nums)):
#     if nums[i] + temp[-1]==10:

#         del temp[-1]
#     else:
#         temp.append(nums[i])
# print(len(temp))
# a = "1345"

# print(list(map(int,list(a))))


# nums = list(map(int,input().split()))
# target = int(input())
'''
二分查找
nums  = [-3,-1,0.1,3,13]
target = 0.1

# def binarySearch(nums,target):
left,right = 0,len(nums)-1
while left <= right:
    mid = left + (right - left)//2
    if nums[mid] == target:
        print(mid)
        break

    elif nums[mid] > target:
        right -=1
    elif nums[mid] < target:
        left +=1
print(-1)
    # return -1
# binarySearch(nums,target)
'''


# x,y  = list(map(int,input().split()))
# x,y =2,6
# def lcm(x,y):
#     greater = max(x,y)
#     while 1:
#         if greater %x ==0 and greater %y ==0:
# #             lcm = greater
#             break
#         greater +=1
#     print(greater)
#     return "gg"
# lcm(x,y)
# print(lcm(x,y))
# print(5)



















'''
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
nums,pos = list(input().split(","))
head = list(map(int,nums.split()))
root = ListNode(head[0])
nodes = {head[0]:root}
for i in range(1,len(head)):
    nodes[head[i]] = ListNode(head[i])
#     print(type(ListNode(head[i])))
    nodes[head[i-1]].next = nodes[head[i]]
nodes[head[len(head)-1]].next = ListNode(list(nodes)[int(pos)])
print(type(list(nodes)[int(pos)]))

def hasCycle(head):
    if not head or not head.next:
        print(False)
        return 
    slow,fast = head,head.next
    while slow != fast:
        if not fast or not fast.next:
            print(False)
            return
        slow = slow.next
        fast =fast.next.next
    print(True)
if int(pos)==-1:
    print(False)
hasCycle(root)
'''

# n,m=map(int,input().split())
# # l=list(range(1,n+1))
# res=0
# for i in range(1,n+1):
#     res=(res+m)%i
# print(res+1)


'''
import bisect
# import bisect
A = [2,1,4,3,1,5,6]
n = 7
if n <=1:print(n)
dp  = [1]*n 
values = [A[0]]
for i in range(1,n):
    if A[i] > values[-1]:
        dp[i] = max(dp) +1 
        values.append(A[i])
    else:
        index = bisect.bisect(values,A[i])
        dp[i] = index +1
        values[index] = A[i]
print(max(dp))
'''

##1190
# str1 = input()
# stack = []
# word= ""
# for c in str1:
#     if c == "(":
#         stack.append(word)
#         word = ""
#     elif c == ")":
#         word = stack.pop(-1) +word[::-1]
#     else:
#         word += c
# print(word)






# ### 快速排序
# nums = list(map(int,input().split()))
# def quickSort(nums,low,high):
#     if low >= high:
#         # print(nums)
#         return
#     ##设置哨兵
#     i,j = low,high
#     ##nums[low]和nums[i]都一样
#     target = nums[low]
#     while i < j:
#         while i < j and nums[j] > target:
#             j-=1
#         while i< j and nums[i] <= target:
#             i+=1
#         nums[i],nums[j] = nums[j],nums[i]
#     nums[low],nums[i] = nums[i],nums[low]
#     quickSort(nums,low,i-1)
#     quickSort(nums,i+1,high)
#     print(nums)
#     return nums
# quickSort(nums,0,len(nums)-1)


# 把ab编程bba

# str1 = input()
# def number(str1):
#     res = 0
#     for i in range(len(str1)-1):
#         if "ab" not in str1:
#             return res
#         else:
#             if str1[i:i+2] =="ab":
#                 str1 = str1[:i] + "bba" + str1[i+2:]
#                 res += 1
#                 res %=1000000007
#     return res
# out = number(str1)               
# print(out)

## 2
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
        
# strs = input().split(",")
# def comonLength(strs):
#     res = ""
#     for i in zip(*strs):
#         if len(set(i)) == 1:
#             res += i[0]
#         else:
#             break
# #     print(res)
#     return res
# print(comonLength(strs))

























# nums = list(map(int,input().split()))

# print(sum(nums),type(nums[1]))
# a = 6
# b=4
# print(max(a,b))
# a = [1,3,5]
# b = []
# print(b.append(sum(a)))



# n = int(input())
# nums = list(map(int,input().split()))
# n = 10
# nums =[1,2,3,4,5,6,7,8,9,10]
# res = [0]
# def xibo(nums):
#     temp = []
#     for i in range(n):
#         a = nums[i]*(-1)**i
#         temp.append(a)
#     temp =sum(temp)
#     res.append(temp)
# for i in range(n):
#     for j in range(n):
#         xibo(nums[j:j+i])
# xibo(nums)
# print(max(res))
# a = []
# print(len(a))
# for i in range(len(a)):
#     print(5)


# a = 0
# for i in range(0):
#     for j in range(i):
#         print(j)

# a = [1,3,5]
# b = []
# b.append(sum(a))
# print(b)

# a = "abc"
# b = "abc"
# if a == b:
#     print(5)



# nums = list(map(int,input().split()))
# def heapSort(nums):
#     ##交换数组中的数字
#     def swap(nums,a,b):
#         nums[a],nums[b] = nums[b],nums[a]
#         return
#     ###堆化过程
#     def heap(nums,k,i):
#         while True:
#             max_index = i
#             if i*2 + 1 < k and nums[i*2+1] > nums[max_index]:
#                 max_index = i*2 + 1
#             elif i*2 + 2 < k and nums[i*2+2] > nums[max_index]:
#                 max_index = i*2 + 2
#             elif max_index == i:
#                 break
#             swap(nums,max_index,i)
#             i = max_index
#     ##建堆
#     for i in range(len(nums)//2,-1,-1):
#         heap(nums,len(nums),i)
#     ##排序过程
#     for i in range(len(nums)-1,0,-1):
#         swap(nums,i,0)
#         heap(nums,i,0)
#     return nums
# heapSort(nums)



# n = int(input())
# nums  = list(map(int,input().split()))
# n = 7
# temp = []
# res = []
# nums = [5,4,5,4,4,1,3]
# for i in range(1,len(nums)):
#     if nums[i] > nums[i-1]:
#         temp.append(i-1)
# print(temp)
# for i in range(n):
#     if i not in temp:
#         res.append(nums[i])
# print(*res)


# n  = int(input())
# hashmap = {}

# def mapAddress(x):
#     if x[0] == "Add":
#         hashmap[x[1]] = [x[2],x[3]]
#     elif x[0] == "Change":
#         hashmap[x[1]] = [x[2],x[3]]
#     elif x[0] == "Delete":
#         del hashmap[x[1]]
#     elif x[0] == "Query":
#         if x[1] in hashmap:
#             print("yes")
#             print(*hashmap[x[1]])
#         else:
#             print("no")
#     else:
#         return
# for i in range(n):
#     x = input().split()
#     mapAddress(x)



# ma = []
# x = list(map(int,input().split()))
# n,m,k,x1,y1 = x[0],x[1],x[2],x[3],x[4]
# for i in range(x[0]):
#     ix =list(map(int,input().split()))
#     ma.append(ix)
# sm = []
# xp,yp = x1 -1 ,y1-1

# def dfs(x,y,k,su,ma):
#     if x < 0 or x > n-1 or y < 0 or y > m-1 or ma[x][y] == -1 or k<0:
#         return
#     elif x == xp and y == yp and k>=0:
#         su += ma[x][y]
#         sm.append(su)
#         return 
#     else:
#         su +=ma[x][y]
#         ma[x][y] = 0
#         k-=1
#         dfs(x+1,y,k,su,ma)
#         dfs(x-1,y,k,su,ma)
#         dfs(x,y+1,k,su,ma)
#         dfs(x,y-1,k,su,ma)
# dfs(xp+ 1,yp,k,0,ma) 
# dfs(xp- 1,yp,k,0,ma) 
# dfs(xp,yp+1,k,0,ma) 
# dfs(xp,yp-1,k,0,ma) 
# print(max(sm))



# a= [5,4,5,4,4,1,3]
# def comp(a):
#     for i in range(len(a) -1 ):
#         if a[i+1] > a[i]:
#             del a[i]
#             return comp(a)
#     return a

# print(comp(a))




# m,n = map(int,input().split())
# matrix = []
# for _ in range(m):
#     matrix.append(list(map(int,input().split()))

# def matrixSet0(matrix):
#     ##放置为0 的行数和列数
#     set_i,set_j = set(),set()
#     ##第一吃遍历找出哪些行和列为0
#     for i in range(m):
#         for j in range(n):
#             if matrix[i][j]==0:
#                 set_i.add(i)
#                 set_j.add(j)
#     ###第二次遍历 赋值改变
#     for i in range(m):
#         for j in  range(n):
#             if i in set_i or j in set_j:
#                 matrix[i][j] =0
#     return matrix
# matrixSet0(matrix)



































# m,n = map(int,input().split())
# coun = []
# for i in range(m):
#     coun.append(list(map(str,input())))

# def dfs(coun,i,j,x):
#     if i < 0 or i>=m or j < 0 or j >=n or coun[i][j] != x:
#         return
#     coun[i][j] = "*"
#     dfs(coun,i+1,j,x)
#     dfs(coun,i-1,j,x)
#     dfs(coun,i,j+1,x)
#     dfs(coun,i,j-1,x)
# def num(coun):
#     if not coun:
#         return 0 
#     res =0 
#     for i in range(m):
#         for j in range(n):
#             if coun[i][j] != "*":
#                 dfs(coun,i,j,coun[i][j])
#                 res += 1
#     return res
# print(num(coun))

# a = [1,2,3]

# hashmap={}
# a = hashmap.fromkeys(a,[])

# print(hashmap,a)

# a ={1: [], 2: [], 3: []}
# print(len(a),a,hashmap)


# a = "k:1  |k1:2|k2:3|k3:4"
# a = a.replace(" ","")
# print(a)

# # # print(a)
# # # hashmap = {}
# # # for item in a.split("|"):
# # #     key,value = item.split(":")
# # #     hashmap[key] = value
# # # print(a,hashmap)
# # d = {k:v for t in a.split("|")for k,v in (t.split(":"),)}
# # print(a,d)





# from time import time, sleep
# def run_time(func):
#     def wrapper():
#         start = time()
#         func()
#         end = time()
#         cost_time = end - start
#         print("func three run time {}".format(cost_time))
#     return wrapper

# @run_time
# def fun_one():
#     sleep(1)
    
# @run_time
# def fun_two():
#     sleep(1)
    
# @run_time
# def fun_three():
#     sleep(1)
    
# fun_one()
# fun_two()
# fun_three()





# from distutils.command.config import config
# import yaml

# settings = yaml.safe_load(open(config, 'r'))['BIOS_CONFIG']
# if self._backend == "xmlcli": 
#     func = cli.CvRestoreModifyKnobs if restore else cli.CvProgKnobs
#     arg = ",".join(["{}={}".format(setting['knob'], setting['value']) for setting in settings])
#     cli.fwp.SecureProfileEditing = True
#     # cli.clb.AuthenticateXmlCliApis = True
#     ret = func(arg)
#     if ret != 0: handler.handle("ERROR with config: {}".format(arg), critical=True)
# elif self._backend == "syscfg":
#     with open("syscfg_run.sh", "w") as f:
#         if restore: 
#             changed_knobs = self.find_changed_knobs()
#             knobs_to_change = [setting['knob'] for setting in settings]
#             for knob_to_restore in changed_knobs:
#                 if knob_to_restore[0] in knobs_to_change: continue
#                 if knob_to_restore[1] not in self._syscfg_knobs_name: 
#                     handler.handle("Warning: {} not settable by syscfg.".format(knob_to_restore[0]))
#                     continue
#                 f.write("./syscfg /bcs \"\" \"{}\" {}\n".format(knob_to_restore[1], int(knob_to_restore[3], 16)))
#         for setting in settings:
#             if setting['prompt'] not in self._syscfg_knobs_name: handler.handle("Error: {} not settable by syscfg.".format(setting['prompt']), critical=True)
#             f.write("./syscfg /bcs \"\" \"{}\" {}\n".format(setting['prompt'], int(setting['value'], 16)))




# a = yaml.safe_load(open("/home/hangzhou/hangz/python/config.yaml", "r"))
# print(a)
# print("============================================")
# b=a.get("BIOS_CONFIG")
# print(b)
# d=a.get('BIOS_CONFIG')
# print(d)
# print("============================================")
# settings = yaml.safe_load(open("/home/hangzhou/hangz/python/config.yaml", 'r'))['BIOS_CONFIG']
# print(settings)
# print("============================================")
# arg = ",".join(["{}={}".format(setting['knob'], setting['value']) for setting in settings])
# print("value of arg {}".format(arg),len(arg))


# x = ["{}={}".format(setting['knob'], setting['value']) for setting in settings]
# print("value of x {}".format(x),len(x))



# knobs_to_change = [setting['knob'] for setting in settings]
# print("knobs_to_change {}".format(knobs_to_change),len(knobs_to_change))


# a = yaml.safe_load(open("/home/hangzhou/hangz/python/config.yaml", 'r'))
# print(a)
# print(a.get("gama"))
# print(a["sigma"])
# print("aaadf={}".format(a))
# c = "aaadf={}".format(a)
# print(c)
# arg = ",".join("aaadf={}".format(a))
# print(arg)

import json
import os
import re
import requests
import yaml
import subprocess
import pathlib
import operator
import hashlib
os.environ['WORKSPACE'] = "/home/hangz/validation"
print(os.getenv('WORKSPACE'))



def execute_cmd(cmd):
    """
    execute shell command
    :param cmd:
    :return: return exit code and output
    """
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    status = 1 if err else 0
    return status, output


def sha256(content=None):
    if content is None:
        return ''
    sha256gen = hashlib.sha256()
    sha256gen.update(content.encode())
    sha256code = sha256gen.hexdigest()
    sha256gen = None
    return sha256code

def generate_infra_benchmark_execution_info(session_id, platform, workload, config, infra_case):
    '''
    generate test result for each benchmark run
    :param platform:
    :param workload:
    :param config:
    :return:
    '''
    benchmark_execution_info = {}
    benchmark_execution_info['execution'] = {}
    build_id = os.getenv('BUILD_ID', '49')
    performance = os.getenv("performance", 'false')
    backend = os.getenv("backend", 'terraform')
    test_config = os.getenv("workload_test_config_yaml", '')

    items = session_id.split('_')
    test_config = test_config if test_config else 'default'

    if len(items) == 5:
        wiki_platform_commit = items[-2]
    else:
        wiki_platform_commit = 'master'

    test_result_folder = os.path.join(os.environ['WORKSPACE'], "result")
    customer = os.getenv('customer', 'main')
    if customer == 'ali':
        art_log_url = 'https://af01p-sh.devtools.intel.com/artifactory/platform_hero_ali-sh-local/benchmark_test_result/%s/%s_%s_%s/logs' % (
            session_id, platform, workload, build_id)
    elif customer == 'tencent':
        art_log_url = 'https://af01p-sh.devtools.intel.com/artifactory/platform_hero_tencent-sh-local/benchmark_test_result/%s/%s_%s_%s/logs' % (
            session_id, platform, workload, build_id)
    else:
        art_log_url = 'https://af01p-igk.devtools.intel.com/artifactory/platform_hero-igk-local/benchmark_test_result/%s/%s_%s_%s/logs' % (
            session_id, platform, workload, build_id)
    ctest_folder = os.path.join(test_result_folder, 'ctest')
    # check test case details from ctest folder, pass/fail
    failed_test_case = []
    #If test was aborted, the test log file name end with .tmp
    failed_test_log = os.path.join(ctest_folder, "LastTestsFailed.log")
    if not os.path.exists(failed_test_log):
        failed_test_log = os.path.join(ctest_folder, "LastTestsFailed.log.tmp")
    all_test_log = os.path.join(ctest_folder, "LastTest.log")
    if not os.path.exists(all_test_log):
        all_test_log = os.path.join(ctest_folder, "LastTest.log.tmp")
    if os.path.exists(failed_test_log):
        with open(failed_test_log, 'r') as fl:
            for line in fl:
                failed_case_name = line.strip("\n").split(":")[1]
                failed_test_case.append(failed_case_name)

    # get all test case info
    if os.path.exists(all_test_log):
        with open(all_test_log, 'r') as all:
            for line in all:
                if "Testing: test_" in line:
                    # for cloud case, case name is test_aws-machine-type_case
                    case_name = line.strip("\n").split(" ")[2]
                    cluster_type = case_name.split("_")[1]
                    if '-' in cluster_type:
                        cluster_type = cluster_type.split("-")[0]
                    logs_folder_name = "logs-" + case_name.split("test_")[-1]
                    test_platform = platform + '_' + cluster_type.upper()
                    if cluster_type == 'baremetal' or cluster_type == 'static':
                        test_platform = platform
                    if cluster_type in ['aws', 'gcp', 'azure']:
                        test_platform = platform + '_' + cluster_type.upper()
                    if cluster_type.lower() == 'gaudi':
                        test_platform = platform + '_AWS'
                    if cluster_type.lower() == 'inf':
                        test_platform = platform + '_AWS'
                    if cluster_type.lower() == 't4':
                        test_platform = platform + '_AWS'
                    if test_platform not in benchmark_execution_info['execution']:
                        benchmark_execution_info['execution'][test_platform] = {}
                        benchmark_execution_info['execution'][test_platform][infra_case] = {}
                        benchmark_execution_info['execution'][test_platform][infra_case][workload] = {}
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'] = {}
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['bom'] = {}
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Total'] = 0
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Passed'] = 0
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Failed'] = 0
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Blocked'] = 0
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Attempted'] = 0
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['No_Run'] = 0
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['all_test_case'] = []
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['passed_test_case'] = []
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['failed_test_case'] = []
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['no_run_test_case'] = []
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['Total'] = \
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Total'] + 1
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['Attempted'] = \
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Attempted'] + 1

                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['log_url'] = art_log_url
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['machine_config'] = config

                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['all_test_case'].append(
                        case_name)

                    # no_label_case as no_run case
                    label_not_found_file = os.path.join(test_result_folder, logs_folder_name, 'no_label_found')
                    emon_not_found_file = os.path.join(test_result_folder, logs_folder_name, 'no_emon_found')
                    timeout_wait_for_server_file = os.path.join(test_result_folder, logs_folder_name,
                                                                'timout_wait_for_server')
                    no_enough_workers_cluster_file = os.path.join(test_result_folder, logs_folder_name,
                                                                'no_enough_workers_cluster')
                    skip_specified_num_nodes_case_file = os.path.join(test_result_folder, logs_folder_name,
                                                                'skip_specified_num_nodes_case')

                    if os.path.exists(label_not_found_file) or os.path.exists(
                            emon_not_found_file) or os.path.exists(
                            timeout_wait_for_server_file) or os.path.exists(
                            no_enough_workers_cluster_file) or os.path.exists(skip_specified_num_nodes_case_file):
                        benchmark_execution_info['execution'][test_platform][infra_case][workload][
                            'no_run_test_case'].append(case_name)
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['No_Run'] = \
                            benchmark_execution_info['execution'][test_platform][infra_case][workload]['No_Run'] + 1
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Attempted'] = \
                            benchmark_execution_info['execution'][test_platform][infra_case][workload]['Attempted'] - 1
                    else:
                        if case_name in failed_test_case:
                            benchmark_execution_info['execution'][test_platform][infra_case][workload][
                                'failed_test_case'].append(case_name)
                            benchmark_execution_info['execution'][test_platform][infra_case][workload]['Failed'] = \
                                benchmark_execution_info['execution'][test_platform][infra_case][workload]['Failed'] + 1
                        else:
                            benchmark_execution_info['execution'][test_platform][infra_case][workload][
                                'passed_test_case'].append(
                                case_name)
                            benchmark_execution_info['execution'][test_platform][infra_case][workload]['Passed'] = \
                                benchmark_execution_info['execution'][test_platform][infra_case][workload]['Passed'] + 1

    # get kpi info
    for root, dirs, files in os.walk(os.path.join(test_result_folder)):
        if "pkb.log" in files or "tfplan.logs" in files:
            folder_name = os.path.basename(root)
            folder_list = root.split("/")
            for folder in folder_list:
                if 'logs-' in folder:
                    folder_name = folder
            benchmark_list = folder_name.split('logs-')
            if len(benchmark_list) == 1:
                benchmark_name = workload
                test_name = workload.lower()
            else:
                benchmark_name = benchmark_list[1]
                test_name = benchmark_name
            cluster_type = test_name.split("_")[0]
            # for cloud case, case name is test_aws-machine-type_case
            if '-' in cluster_type:
                cluster_type = cluster_type.split("-")[0]

            if backend == 'cumulus':
                f = open("%s/workload-config.yaml" % root.split('runs')[0], 'r')
            else:
                f = open("%s/workload-config.yaml" % root, 'r')
            result = f.read()
            case_workload_config = yaml.safe_load(result)
            case_sha256 = sha256(str(case_workload_config['tunables']))

            test_platform = platform + '_' + cluster_type.upper()
            if cluster_type == 'baremetal' or cluster_type == 'static':
                test_platform = platform
            if cluster_type in ['aws', 'gcp', 'azure']:
                test_platform = platform + '_' + cluster_type.upper()
            if cluster_type.lower() == 'gaudi':
                test_platform = platform + '_AWS'
            if cluster_type.lower() == 'inf':
                test_platform = platform + '_AWS'
            if cluster_type.lower() == 't4':
                test_platform = platform + '_AWS'

            if test_platform not in benchmark_execution_info['execution']:
                benchmark_execution_info['execution'][test_platform] = {}
                benchmark_execution_info['execution'][test_platform][infra_case] = {}
                benchmark_execution_info['execution'][test_platform][infra_case][workload] = {}
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'] = {}
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['bom'] = {}
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['Total'] = 0
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['Passed'] = 0
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['Failed'] = 0
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['Blocked'] = 0
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['Attempted'] = 0
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['No_Run'] = 0
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['all_test_case'] = []
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['passed_test_case'] = []
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['failed_test_case'] = []
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['no_run_test_case'] = []

            pkb_log = os.path.join(root, 'pkb.log')
            if os.path.exists("%s/intel_publisher/perfKitRuns.json" % root):
                with open("%s/intel_publisher/perfKitRuns.json" % root, 'r') as fp:
                    run_details = json.load(fp)
                run_uri = run_details['uri']
            else:
                run_uri = ''

            if backend == 'cumulus':
                cmd = "cat %s | grep 'End to End Runtime' | grep seconds | awk '{print $5}'" % pkb_log
                ret, output = execute_cmd(cmd)
                test_time = output.decode('ascii').strip().split('\n')
                if len(test_time) > 0:
                    execution_time = test_time[0]
                else:
                    execution_time = ''
            else:
                execution_time_log = os.path.join(root,'execution_time')
                if os.path.exists(execution_time_log):
                    with open(execution_time_log, 'r') as fl:
                        execution_time = fl.read().split("\n")[0]
                else:
                    execution_time = ''

            if test_name not in benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'].keys():
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name] = {}
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name]['metrics'] = {}
            cumulus_url = "https://wsf-dashboards.intel.com/services-framework/run_uri/%s" % run_uri

            benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name][
                'cumulus_url'] = cumulus_url
            benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name][
                'test_time'] = execution_time
            benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name]['sha256'] = case_sha256
            # get hw config
            hw_config_file = os.path.join(test_result_folder, folder_name, 'cluster_config')

            if os.path.exists(hw_config_file):
                with open(hw_config_file, 'r') as fl:
                    hw_config = fl.read().split("\n")[0]
            else:
                hw_config = '0'

            cumulus_config = os.path.join(test_result_folder, folder_name, 'cumulus-config.yaml')
            benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name]['config'] = hw_config
            benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name]['test_config'] = test_config
            benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name][
                'wiki_platform_version'] = wiki_platform_commit

            # add all kpi
            # kpi_log_name = "kpi_*%s.log" % (benchmark_name.lower())
            kpi_log_name = "kpi_*%s.log" % (benchmark_name)
            kpi_log = os.path.join(test_result_folder, "kpi/%s" % kpi_log_name)
            all_metrics_cmd = "cat %s" % (str(kpi_log))
            if performance == 'true':
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name]['itr'] = {}
            ret_code, metrics_info = execute_cmd(all_metrics_cmd)
            metrics = metrics_info.decode('ascii').strip().split('\n')

            for metric in metrics:
                if metric.startswith('*') and ':' in metric:
                    info = metric.split(':')
                    metric_name = info[0].replace('*', '')
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name]['metrics'][
                        metric_name] = info[1]
                else:
                    if performance == 'true':
                        if 'itr' in metric.split(' ')[0]:
                            itr = metric.split(' ')[0]
                            if ':' not in metric:
                                itr_value = ' '
                            else:
                                itr_value = metric.split(':')[1]
                            benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name]['itr'][itr] = itr_value

            # case return fail if no kpi
            if not bool(
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name]['metrics']) and os.getenv('type', 'workload') == 'workload':
                real_case_name = 'test_' + test_name
                if real_case_name in benchmark_execution_info['execution'][test_platform][infra_case][workload][
                    'passed_test_case']:
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['passed_test_case'].remove(
                        real_case_name)
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['failed_test_case'].append(
                        real_case_name)
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['Failed'] = \
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Failed'] + 1
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['Passed'] = \
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Passed'] - 1
                    os.system(
                        "echo %s >> %s/logs/ctest/LastTestsFailed.log" % (real_case_name, os.environ['WORKSPACE']))
    #if test failed with no pkb.log, also mark it as failed
    for item in os.listdir(test_result_folder):
        test_dir = os.path.join(test_result_folder, item)
        if os.path.isdir(test_dir) and item.startswith('logs-'):
            # test_dir = os.path.join(test_result_folder,item)
            # if not find pkb.log
            if not sorted(pathlib.Path(test_dir).glob('**/pkb.log')):
                test_name = item.replace('logs-','')
                cluster_type = test_name.split("_")[0]
                if '-' in cluster_type:
                    cluster_type = cluster_type.split("-")[0]
                test_platform = platform + '_' + cluster_type.upper()
                if cluster_type == 'baremetal' or cluster_type == 'static':
                    test_platform = platform
                if cluster_type in ['aws', 'gcp', 'azure']:
                    test_platform = platform + '_' + cluster_type.upper()
                if cluster_type.lower() == 'gaudi':
                    test_platform = platform + '_AWS'
                real_case_name = 'test_' + test_name
                if real_case_name in benchmark_execution_info['execution'][test_platform][infra_case][workload]['passed_test_case']:
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['passed_test_case'].remove(
                        real_case_name)
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['failed_test_case'].append(
                        real_case_name)
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['Failed'] = \
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Failed'] + 1
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['Passed'] = \
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Passed'] - 1
                    os.system(
                        "echo %s >> %s/logs/ctest/LastTestsFailed.log" % (real_case_name, os.environ['WORKSPACE']))
    # get bom info
    bom_folder = os.path.join(test_result_folder, "bom")
    if os.path.exists(bom_folder):
        for bom_file in os.listdir(bom_folder):
            bom = os.path.join(bom_folder, bom_file)
            with open(bom) as file:
                for line in file:
                    line = line.rstrip("\n")
                    bom_name = line.split(' ')[0]
                    bom_value = line.split(' ')[1]
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['bom'][bom_name] = bom_value

    print(benchmark_execution_info)

    json_str = json.dumps(benchmark_execution_info, indent=4)
    execution_json_file = os.path.join(os.environ['WORKSPACE'], "%s_%s.json" % (platform, workload))
    with open('%s' % execution_json_file, 'w') as json_file:
        json_file.write(json_str)

infra_case = "test_aws_icx_sanity"
print(generate_infra_benchmark_execution_info("Infra_automation_08-10-2023_49_e31c5836","ICX","Nginx","", infra_case))
def generate_infra_benchmark_execution_info(session_id, platform, workload, config, infra_case):
    '''
    generate test result for each benchmark run
    :param platform:
    :param workload:
    :param config:
    :return:
    '''
    benchmark_execution_info = {}
    benchmark_execution_info['execution'] = {}
    build_id = os.getenv('BUILD_ID', '49')
    performance = os.getenv("performance", 'false')
    backend = os.getenv("backend", 'terraform')
    test_config = os.getenv("workload_test_config_yaml", '')

    items = session_id.split('_')
    test_config = test_config if test_config else 'default'

    if len(items) == 5:
        wiki_platform_commit = items[-2]
    else:
        wiki_platform_commit = 'master'

    test_result_folder = os.path.join(os.environ['WORKSPACE'], "result")
    customer = os.getenv('customer', 'main')
    if customer == 'ali':
        art_log_url = 'https://af01p-sh.devtools.intel.com/artifactory/platform_hero_ali-sh-local/benchmark_test_result/%s/%s_%s_%s/logs' % (
            session_id, platform, workload, build_id)
    elif customer == 'tencent':
        art_log_url = 'https://af01p-sh.devtools.intel.com/artifactory/platform_hero_tencent-sh-local/benchmark_test_result/%s/%s_%s_%s/logs' % (
            session_id, platform, workload, build_id)
    else:
        art_log_url = 'https://af01p-igk.devtools.intel.com/artifactory/platform_hero-igk-local/benchmark_test_result/%s/%s_%s_%s/logs' % (
            session_id, platform, workload, build_id)
    ctest_folder = os.path.join(test_result_folder, 'ctest')
    # check test case details from ctest folder, pass/fail
    failed_test_case = []
    #If test was aborted, the test log file name end with .tmp
    failed_test_log = os.path.join(ctest_folder, "LastTestsFailed.log")
    if not os.path.exists(failed_test_log):
        failed_test_log = os.path.join(ctest_folder, "LastTestsFailed.log.tmp")
    all_test_log = os.path.join(ctest_folder, "LastTest.log")
    if not os.path.exists(all_test_log):
        all_test_log = os.path.join(ctest_folder, "LastTest.log.tmp")
    if os.path.exists(failed_test_log):
        with open(failed_test_log, 'r') as fl:
            for line in fl:
                failed_case_name = line.strip("\n").split(":")[1]
                failed_test_case.append(failed_case_name)

    # get all test case info
    if os.path.exists(all_test_log):
        with open(all_test_log, 'r') as all:
            for line in all:
                if "Testing: test_" in line:
                    # for cloud case, case name is test_aws-machine-type_case
                    case_name = line.strip("\n").split(" ")[2]
                    cluster_type = case_name.split("_")[1]
                    if '-' in cluster_type:
                        cluster_type = cluster_type.split("-")[0]
                    logs_folder_name = "logs-" + case_name.split("test_")[-1]
                    test_platform = platform + '_' + cluster_type.upper()
                    if cluster_type == 'baremetal' or cluster_type == 'static':
                        test_platform = platform
                    if cluster_type in ['aws', 'gcp', 'azure']:
                        test_platform = platform + '_' + cluster_type.upper()
                    if cluster_type.lower() == 'gaudi':
                        test_platform = platform + '_AWS'
                    if cluster_type.lower() == 'inf':
                        test_platform = platform + '_AWS'
                    if cluster_type.lower() == 't4':
                        test_platform = platform + '_AWS'
                    if test_platform not in benchmark_execution_info['execution']:
                        benchmark_execution_info['execution'][test_platform] = {}
                        benchmark_execution_info['execution'][test_platform][infra_case] = {}
                        benchmark_execution_info['execution'][test_platform][infra_case][workload] = {}
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'] = {}
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['bom'] = {}
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Total'] = 0
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Passed'] = 0
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Failed'] = 0
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Blocked'] = 0
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Attempted'] = 0
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['No_Run'] = 0
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['all_test_case'] = []
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['passed_test_case'] = []
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['failed_test_case'] = []
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['no_run_test_case'] = []
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['Total'] = \
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Total'] + 1
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['Attempted'] = \
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Attempted'] + 1

                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['log_url'] = art_log_url
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['machine_config'] = config

                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['all_test_case'].append(
                        case_name)

                    # no_label_case as no_run case
                    label_not_found_file = os.path.join(test_result_folder, logs_folder_name, 'no_label_found')
                    emon_not_found_file = os.path.join(test_result_folder, logs_folder_name, 'no_emon_found')
                    timeout_wait_for_server_file = os.path.join(test_result_folder, logs_folder_name,
                                                                'timout_wait_for_server')
                    no_enough_workers_cluster_file = os.path.join(test_result_folder, logs_folder_name,
                                                                'no_enough_workers_cluster')
                    skip_specified_num_nodes_case_file = os.path.join(test_result_folder, logs_folder_name,
                                                                'skip_specified_num_nodes_case')

                    if os.path.exists(label_not_found_file) or os.path.exists(
                            emon_not_found_file) or os.path.exists(
                            timeout_wait_for_server_file) or os.path.exists(
                            no_enough_workers_cluster_file) or os.path.exists(skip_specified_num_nodes_case_file):
                        benchmark_execution_info['execution'][test_platform][infra_case][workload][
                            'no_run_test_case'].append(case_name)
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['No_Run'] = \
                            benchmark_execution_info['execution'][test_platform][infra_case][workload]['No_Run'] + 1
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Attempted'] = \
                            benchmark_execution_info['execution'][test_platform][infra_case][workload]['Attempted'] - 1
                    else:
                        if case_name in failed_test_case:
                            benchmark_execution_info['execution'][test_platform][infra_case][workload][
                                'failed_test_case'].append(case_name)
                            benchmark_execution_info['execution'][test_platform][infra_case][workload]['Failed'] = \
                                benchmark_execution_info['execution'][test_platform][infra_case][workload]['Failed'] + 1
                        else:
                            benchmark_execution_info['execution'][test_platform][infra_case][workload][
                                'passed_test_case'].append(
                                case_name)
                            benchmark_execution_info['execution'][test_platform][infra_case][workload]['Passed'] = \
                                benchmark_execution_info['execution'][test_platform][infra_case][workload]['Passed'] + 1

    # get kpi info
    for root, dirs, files in os.walk(os.path.join(test_result_folder)):
        if "pkb.log" in files or "tfplan.logs" in files:
            folder_name = os.path.basename(root)
            folder_list = root.split("/")
            for folder in folder_list:
                if 'logs-' in folder:
                    folder_name = folder
            benchmark_list = folder_name.split('logs-')
            if len(benchmark_list) == 1:
                benchmark_name = workload
                test_name = workload.lower()
            else:
                benchmark_name = benchmark_list[1]
                test_name = benchmark_name
            cluster_type = test_name.split("_")[0]
            # for cloud case, case name is test_aws-machine-type_case
            if '-' in cluster_type:
                cluster_type = cluster_type.split("-")[0]

            if backend == 'cumulus':
                f = open("%s/workload-config.yaml" % root.split('runs')[0], 'r')
            else:
                f = open("%s/workload-config.yaml" % root, 'r')
            result = f.read()
            case_workload_config = yaml.safe_load(result)
            case_sha256 = sha256(str(case_workload_config['tunables']))

            test_platform = platform + '_' + cluster_type.upper()
            if cluster_type == 'baremetal' or cluster_type == 'static':
                test_platform = platform
            if cluster_type in ['aws', 'gcp', 'azure']:
                test_platform = platform + '_' + cluster_type.upper()
            if cluster_type.lower() == 'gaudi':
                test_platform = platform + '_AWS'
            if cluster_type.lower() == 'inf':
                test_platform = platform + '_AWS'
            if cluster_type.lower() == 't4':
                test_platform = platform + '_AWS'

            if test_platform not in benchmark_execution_info['execution']:
                benchmark_execution_info['execution'][test_platform] = {}
                benchmark_execution_info['execution'][test_platform][infra_case] = {}
                benchmark_execution_info['execution'][test_platform][infra_case][workload] = {}
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'] = {}
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['bom'] = {}
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['Total'] = 0
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['Passed'] = 0
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['Failed'] = 0
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['Blocked'] = 0
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['Attempted'] = 0
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['No_Run'] = 0
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['all_test_case'] = []
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['passed_test_case'] = []
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['failed_test_case'] = []
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['no_run_test_case'] = []

            pkb_log = os.path.join(root, 'pkb.log')
            if os.path.exists("%s/intel_publisher/perfKitRuns.json" % root):
                with open("%s/intel_publisher/perfKitRuns.json" % root, 'r') as fp:
                    run_details = json.load(fp)
                run_uri = run_details['uri']
            else:
                run_uri = ''

            if backend == 'cumulus':
                cmd = "cat %s | grep 'End to End Runtime' | grep seconds | awk '{print $5}'" % pkb_log
                ret, output = execute_cmd(cmd)
                test_time = output.decode('ascii').strip().split('\n')
                if len(test_time) > 0:
                    execution_time = test_time[0]
                else:
                    execution_time = ''
            else:
                execution_time_log = os.path.join(root,'execution_time')
                if os.path.exists(execution_time_log):
                    with open(execution_time_log, 'r') as fl:
                        execution_time = fl.read().split("\n")[0]
                else:
                    execution_time = ''

            if test_name not in benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'].keys():
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name] = {}
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name]['metrics'] = {}
            cumulus_url = "https://wsf-dashboards.intel.com/services-framework/run_uri/%s" % run_uri

            benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name][
                'cumulus_url'] = cumulus_url
            benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name][
                'test_time'] = execution_time
            benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name]['sha256'] = case_sha256
            # get hw config
            hw_config_file = os.path.join(test_result_folder, folder_name, 'cluster_config')

            if os.path.exists(hw_config_file):
                with open(hw_config_file, 'r') as fl:
                    hw_config = fl.read().split("\n")[0]
            else:
                hw_config = '0'

            cumulus_config = os.path.join(test_result_folder, folder_name, 'cumulus-config.yaml')
            benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name]['config'] = hw_config
            benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name]['test_config'] = test_config
            benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name][
                'wiki_platform_version'] = wiki_platform_commit

            # add all kpi
            # kpi_log_name = "kpi_*%s.log" % (benchmark_name.lower())
            kpi_log_name = "kpi_*%s.log" % (benchmark_name)
            kpi_log = os.path.join(test_result_folder, "kpi/%s" % kpi_log_name)
            all_metrics_cmd = "cat %s" % (str(kpi_log))
            if performance == 'true':
                benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name]['itr'] = {}
            ret_code, metrics_info = execute_cmd(all_metrics_cmd)
            metrics = metrics_info.decode('ascii').strip().split('\n')

            for metric in metrics:
                if metric.startswith('*') and ':' in metric:
                    info = metric.split(':')
                    metric_name = info[0].replace('*', '')
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name]['metrics'][
                        metric_name] = info[1]
                else:
                    if performance == 'true':
                        if 'itr' in metric.split(' ')[0]:
                            itr = metric.split(' ')[0]
                            if ':' not in metric:
                                itr_value = ' '
                            else:
                                itr_value = metric.split(':')[1]
                            benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name]['itr'][itr] = itr_value

            # case return fail if no kpi
            if not bool(
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['kpi'][test_name]['metrics']) and os.getenv('type', 'workload') == 'workload':
                real_case_name = 'test_' + test_name
                if real_case_name in benchmark_execution_info['execution'][test_platform][infra_case][workload][
                    'passed_test_case']:
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['passed_test_case'].remove(
                        real_case_name)
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['failed_test_case'].append(
                        real_case_name)
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['Failed'] = \
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Failed'] + 1
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['Passed'] = \
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Passed'] - 1
                    os.system(
                        "echo %s >> %s/logs/ctest/LastTestsFailed.log" % (real_case_name, os.environ['WORKSPACE']))
    #if test failed with no pkb.log, also mark it as failed
    for item in os.listdir(test_result_folder):
        test_dir = os.path.join(test_result_folder, item)
        if os.path.isdir(test_dir) and item.startswith('logs-'):
            # test_dir = os.path.join(test_result_folder,item)
            # if not find pkb.log
            if not sorted(pathlib.Path(test_dir).glob('**/pkb.log')):
                test_name = item.replace('logs-','')
                cluster_type = test_name.split("_")[0]
                if '-' in cluster_type:
                    cluster_type = cluster_type.split("-")[0]
                test_platform = platform + '_' + cluster_type.upper()
                if cluster_type == 'baremetal' or cluster_type == 'static':
                    test_platform = platform
                if cluster_type in ['aws', 'gcp', 'azure']:
                    test_platform = platform + '_' + cluster_type.upper()
                if cluster_type.lower() == 'gaudi':
                    test_platform = platform + '_AWS'
                real_case_name = 'test_' + test_name
                if real_case_name in benchmark_execution_info['execution'][test_platform][infra_case][workload]['passed_test_case']:
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['passed_test_case'].remove(
                        real_case_name)
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['failed_test_case'].append(
                        real_case_name)
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['Failed'] = \
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Failed'] + 1
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['Passed'] = \
                        benchmark_execution_info['execution'][test_platform][infra_case][workload]['Passed'] - 1
                    os.system(
                        "echo %s >> %s/logs/ctest/LastTestsFailed.log" % (real_case_name, os.environ['WORKSPACE']))
    # get bom info
    bom_folder = os.path.join(test_result_folder, "bom")
    if os.path.exists(bom_folder):
        for bom_file in os.listdir(bom_folder):
            bom = os.path.join(bom_folder, bom_file)
            with open(bom) as file:
                for line in file:
                    line = line.rstrip("\n")
                    bom_name = line.split(' ')[0]
                    bom_value = line.split(' ')[1]
                    benchmark_execution_info['execution'][test_platform][infra_case][workload]['bom'][bom_name] = bom_value

    print(benchmark_execution_info)

    json_str = json.dumps(benchmark_execution_info, indent=4)
    execution_json_file = os.path.join(os.environ['WORKSPACE'], "%s_%s.json" % (platform, workload))
    with open('%s' % execution_json_file, 'w') as json_file:
        json_file.write(json_str)

infra_case = "test_aws_icx_sanity"
print(generate_infra_benchmark_execution_info("Infra_automation_08-10-2023_49_e31c5836","ICX","Nginx","", infra_case))