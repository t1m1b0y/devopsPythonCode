#map function


li = [1,2,3,4,5,6,7,8,9]

def func(x):
    return x**x

#lame version
newlist = []

for element in li:
    newlist.append(func(element))


#good version
print(list(map(func,li)))
    
