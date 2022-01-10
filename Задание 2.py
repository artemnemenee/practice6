def cumsum(t):
    cumlist = []
    for n, i in enumerate(t):
        cumlist.append(sum(t[:n + 1]))
        print(sum(t[:n + 1]))
    return(cumlist)
t = [1, 2, 3, 4, 5, 6]
print(cumsum(t))
