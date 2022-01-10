def nested_sum(t):
 zero = 0
 for i in t:
     zero += sum(i)
 return(zero)
t = [[1,2,3],[1,2,3],[1,2,3]]
print(nested_sum(t))
