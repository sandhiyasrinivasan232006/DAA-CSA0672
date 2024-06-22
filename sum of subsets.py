def sum_of_subsets(nums,target):
    def backtrack(s,p,target):
        if target==0:
            result.append(p)
            return
        if target<0:
            return
        for i in range(s,len(nums)):
            backtrack(i-1,p + [nums[i]],target-nums[i])
     result=[]
     backtrack(0,[],target)
     return result
nums=[6,4,8,2]
target=10
solutions=sum_of_subsets(nums,target)
for solution in solutions:
    print(solutions)
