"""
def solution(number):
    totalSum = 0
    for i in range(2, number):
        if i % 3 == 0 or i % 5 == 0:
            totalSum += i
    return totalSum
        
solution(10)
"""
# -------------------------------------------------------------------------------------- #
"""
def likes(names):
    if (len(names) == 0):
        return "no one likes this"
    elif (len(names) == 1):
        return f"{names[0]} likes this"      
    elif (len(names) == 2):
        return f"{names[0]} and {names[1]} likes this"      
    elif (len(names) == 3):
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} likes this"
    
likes([])
likes(["Peter"])
likes(["Max", "John"])
likes(["Max", "John", "Mark"])
likes(["Alex", "Jacob", "Mark", "Max", "ola"])
"""
# -------------------------------------------------------------------------------------- #
def array_diff(a, b):
    array = []
    for i in a:
        if (i not in b):
            array.append(i)
    return array


array_diff([1,2], [1])
array_diff([1,2,2,2,2,3], [2])