#function that takes a list and returns all possible permutations in the list
def permutation(elements):
    if len(elements)==0:
        return []
    elif len(elements)==1:
        return [elements]
    
    per=[]
    for i in range (len(elements)):
        a=elements[i]
        x=elements[:i] + elements[i+1:]
        
        for j in permutation(x):
            per.append([a]+j)
    return per

n = int(input("Enter the n : "))
data=[]
for x in range(n):
    data.append(int(input("")))

# data=[1,2,3,4]
for k in (permutation(data)):
    print(k)