def chop(t):
    t.pop(0)
    t.pop(len(t) - 1)
    print(t)
t = [1, 2, 3]
print(chop(t))
