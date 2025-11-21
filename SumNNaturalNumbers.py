# => Recursion is a programming technique where a function call itself directly or indirectly in order to solve a problem.
# => In a recursion function the function makes one or more calls to itself as a part of its execution.
# => The process continue until a base case is reach at which point function stop calling itself and returns our result.
# 1. make an assumption decide what your function does and trust that it will do it
# 2. main logic
# 3. solve the bigger problem using sub problem 
# 4. base case
# when the recursion stops


# num= int(input())
# sum= 0
# for i in range(1,num+1):
#     sum+= i
# print(sum)

def sum(N):
    if N== 1:
        return 1
    else:
        return sum(N-1) + N
N= int(input())
result= sum(N)
print(result)


