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
#         val = x
#         left = None
#         right = None

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
#         val = x
#         left = None
#         right = None

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




# a = "Epoch: [0][0/915]	 lr:0.01000 Time 14.648 (14.648)	Loss 8.4618 (8.4618)	Prec@1 0.000 (0.000)"
# b = a.split()
# print(b)
# print(b[-5])
# print(b[-1].strip("()"))
# print(150)

# # c = "(0.000)"
# # print(c.strip("()"))

# print("第一行\na")
# changed_knobs=[['DelayedAuthenticationMode', 'Delayed Authentication Mode (DAM)', 'Enable/disable Delayed Authentication Mode (DAM)', '0x00', '0x01', 'Disabled: 0x0\nEnabled: 0x1'], ['SncEn', 'SNC', 'Disable supports 1-cluster and 4-IMC way\ninterleave. Enable SNC2 supports 2-clusters SNC\nand 2-way IMC interleave.  Enable SNC4 supports\n4-cluster and 1-IMC way interleave, Auto - Auto\ndecides based on Si Compatibility.', '0x0F', '0x00', 'AUTO: 0xF\nDisable: 0x0\nEnable SNC2 (2-clusters): 0x2\nEnable SNC4 (4-clusters): 0x4'], ['VTdSupport', 'Intel VT for Directed I/O', 'Enable/Disable Intel Virtualization Technology for\nDirected I/O (VT-d) by reporting the I/O device\nassignment to VMM through DMAR ACPI Tables. To\ndisable VT-d, X2APIC must also be disabled.', '0x01', '0x00', 'Enable: 0x1\nDisable: 0x0'], ['ProcessorX2apic', 'Extended APIC', 'Enable/disable extended APIC support    Note:\nWhen enabled, VT-d n Interrupt Remapping will be\nautomatically enabled.', '0x01', '0x00', 'Disable: 0x0\nEnable: 0x1']] 
# print(changed_knobs[0],changed_knobs[0][0],changed_knobs[0][1])
import json
import os
import requests
import sys
import subprocess

# benchmark_runs = ['SPR_BoringSSL_7.json', 'ICX_Nginx_7_cloud.json']
# test_result_folder = "/home/hangz/validation/Infra_automation_08-10-2023_49_e31c5836"
os.environ['WORKSPACE'] = "/home/hangz/validation"
print(os.getenv('WORKSPACE'))
# sys.exit()
def get_platforms(run_folder):
    """
    get platform list from benchmark run
    :param run_folder:
    :return:
    """
    platform_list = []
    for run in os.listdir(run_folder):
        if run != 'execution.json':
            platform = run.split("_")[0]
            platform_list.append(platform)
    return list(set(platform_list))

def check_case_support_in_workload_execution(workload_execution, platform, workload):
    """
    check all test case in the execution to see if supported in current version or not, if not, remove the case info
    :param workload_execution:
    :param platform:
    :param workload:
    :return:
    """
    updated_workload_execution = workload_execution
    remove_case_list = []
    test_type = workload_execution['all_test_case'][0].split('_')[1]
    test_type = test_type.split('-')[0]

    support_case_list = []
    platform_name = platform.split('_')[0]
    cmd = "%s/script/automation/post-validation/workload.sh get_workload_case %s %s %s" % (
        os.environ['WORKSPACE'], platform_name, workload, test_type)
    p = subprocess.Popen(
        cmd,
        shell=True,
        cwd="%s/script/automation/post-validation" % os.environ['WORKSPACE'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    try:
        while True:
            line = p.stdout.readline()
            line_info = line.decode('ascii').strip().split('\n')[0]
            if "test_%s" % test_type in line_info:
                support_case_list.append(line_info)
            if not line:
                break
    except Exception as e:
        print(e)
    for case in workload_execution['all_test_case']:
        test_type = case.split('_')[1]
        case_name = test_type + case.split('test_%s' % test_type)[-1]
        real_ctest_case_name = "test_" + test_type.split('-')[0] + case.split('test_%s' % test_type)[-1]

        if real_ctest_case_name not in support_case_list:
            remove_case_list.append(case)
            workload_execution['Total'] = workload_execution['Total'] - 1
            if case in workload_execution['passed_test_case']:
                workload_execution['Attempted'] = workload_execution['Attempted'] - 1
                workload_execution['Passed'] = workload_execution['Passed'] - 1
                workload_execution['passed_test_case'].remove(case)
                if case_name in workload_execution['kpi']:
                    del workload_execution['kpi'][case_name]
            elif case in workload_execution['failed_test_case']:
                workload_execution['Attempted'] = workload_execution['Attempted'] - 1
                workload_execution['Failed'] = workload_execution['Failed'] - 1
                workload_execution['failed_test_case'].remove(case)
                if case_name in workload_execution['kpi']:
                    del workload_execution['kpi'][case_name]
            else:
                workload_execution['No_Run'] = workload_execution['No_Run'] - 1
                workload_execution['no_run_test_case'].remove(case)
    for case in remove_case_list:
        workload_execution['all_test_case'].remove(case)
    return updated_workload_execution


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
def check_result_exist(test_result_folder):
    '''
    check test result json exist or not, if yes, check the run_count
    :param test_result_folder:
    :return:
    '''
    json_file = os.path.join(test_result_folder, 'execution.json')
    if os.path.exists(json_file):
        benchmark_runs = os.listdir(test_result_folder)
        with open(json_file, 'r') as fp:
            execution = json.load(fp)
            if 'run_count' in execution.keys():
                if execution['run_count'] == len(benchmark_runs) - 1:
                    return True
                else:
                    return False
            else:
                return True
    else:
        return False

def get_infra_session_execution_info(session_id, forced=False):
    """
    get all cases and reserved machine info from test session
    :param session_id:
    :return: all execution info in the test session
    """
    session_info = {}
    session_info['all_test_case'] = []
    session_info['passed_test_case'] = []
    session_info['failed_test_case'] = []
    total_cases = 0
    passed_cases = 0
    failed_cases = 0

    test_result_folder = os.path.join(os.environ['WORKSPACE'], session_id)
    print("test_result_folder value %s" %test_result_folder)
    execution_json_file = os.path.join(test_result_folder, 'execution.json')

    if not os.path.exists(test_result_folder):
        return session_info

    if not check_result_exist(test_result_folder) or forced:
        commit_id = session_id.split('_')[-1]
        print(commit_id)
        session_info['revision'] = commit_id
        build_id = session_id.split('_')[-2]
        print(build_id)
        session_info['build_id'] = build_id
        os.system("rm -rf %s/execution.json" % test_result_folder)

        filtered_test = os.listdir(test_result_folder)
        session_info['run_count'] = len(filtered_test)
        benchmark_runs = []
        max_digit = {}
        for element in filtered_test:
            if element.endswith(".json"):
                parts = element.split(".")[0].split("_")
                key = "_".join(parts[:-1])
                value = int(parts[-1])
                if key not in max_digit or value > max_digit[key]:
                    max_digit[key] = value

        for key, value in max_digit.items():
            benchmark_runs.append(f"{key}_{value}.json")
        print("benchmark_run value %s" %benchmark_runs, len(benchmark_runs))

        total_cases = len(benchmark_runs)
        for run in benchmark_runs:
            if run != 'execution.json' and "dummy" not in run:
                json_file = os.path.join(test_result_folder, run)
                case_name = run.split(':')[0]
                workload = run.split(':')[1].split('_')[1]
                single_build_id = run.split(':')[1].split('_')[2]
                with open(json_file, 'r') as fp:
                    benchmark_execution = json.load(fp)
                if len(benchmark_execution['execution'].keys()) == 0:
                    continue

                for platform, execution_info in benchmark_execution['execution'].items():

                    if benchmark_execution['execution'][platform][workload]['Total'] == benchmark_execution['execution'][platform][workload]['Passed']:
                        session_info['passed_test_case'].append(case_name)
                        session_info['all_test_case'].append(case_name)
                        passed_cases += 1
                    else :
                        session_info['failed_test_case'].append(case_name)
                        session_info['all_test_case'].append(case_name)
                        failed_cases += 1

        session_info['total_cases'] = total_cases
        session_info['passed_cases'] = passed_cases
        session_info['failed_cases'] = failed_cases

        if total_cases == 0 :
            session_info['passed_rate'] = '0.00%'
        else:
            session_info['passed_rate'] = '{:.2f}%'.format(passed_cases / total_cases * 100)

        # dump to json file
        json_str = json.dumps(session_info, indent=4)
        with open('%s' % execution_json_file, 'w') as json_file:
            json_file.write(json_str)
        return session_info
    else:
        with open('%s' % execution_json_file, 'r') as json_file:
            execution = json.load(json_file)
            return execution

print(get_infra_session_execution_info("Infra_automation"))




# def update_development_report(session_id):
#     """
#     create validation report per week.
#     :param report:
#     :param session_id:
#     :return:
#     """

#     session_info = get_infra_session_execution_info(session_id)

#     if not os.path.exists(LOCAL_VALIDATION_FOLDER):
#         os.makedirs(LOCAL_VALIDATION_FOLDER)

#     validation_file = (
#     LOCAL_VALIDATION_FOLDER + '/' + 'validation-local-%s-ww%s.md' % (CURRENTLY_YEAR, CURRENTLY_WEEK))

#     if 'revision' not in session_info.keys():
#         revision_info = ''
#     else:
#         revision_info = 'Platform hero features revision: %s  \n' % session_info['revision']

    
#     validation_summary_info = '**Summary**   \n\n{}\n\nTotal {} tests, {} run, {} passed, {} failed.  \n\n'.format(
#         revision_info, session_info['total_cases'], session_info['attempted_cases'],
#         session_info['passed_cases'], session_info['failed_cases'])

#     execution_info = get_execution_status(session_info['execution'])
#     execution_summary = '| Summary | | %d | %d | %d | %d | %d | %d | %s | %s |  |' % (session_info['attempted_cases'],
#                                                                                       session_info['blocked_cases'],
#                                                                                       session_info['no_run_cases'],
#                                                                                       session_info['failed_cases'],
#                                                                                       session_info['passed_cases'],
#                                                                                       session_info['total_cases'],
#                                                                                       session_info['attempted_rate'],
#                                                                                       session_info['passed_rate'])

#     kpi_info = get_kpi_status(session_info['execution'])
#     date = sys.argv[2].replace('cloud_', '').replace('main_', '').replace('ali_', '').replace('tencent_', '').split("_")[0] + "_" + os.environ['BUILD_ID']
#     if not os.path.exists(validation_file):
#         os.system("touch %s" % validation_file)

#     with open(validation_file, 'r+') as f:
#         content = f.read()
#         f.seek(0, 0)
#         f.write('### %s\n%s  \n\n%s  \n%s  \n\n' % (
#             date, validation_summary_info, execution_info, execution_summary) + content)

#     if not os.path.exists(kpi_file):
#         os.system("touch %s" % kpi_file)

#     with open(kpi_file, 'r+') as f:
#         content = f.read()
#         f.seek(0, 0)
#         f.write('%s  \n\n' % kpi_info + content)

#     update_link_file(report, session_info)



    

